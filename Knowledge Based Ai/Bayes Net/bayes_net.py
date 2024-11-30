class BayesNet:
    def __init__(self):
        self.network = {
            "Necronia flu": {"parents": [], "probabilities": {True: 0.8, False: 0.2}},
            "Typhonus worm": {"parents": [], "probabilities": {True: 0.05, False: 0.95}},
            "Scleraitis": {"parents": [], "probabilities": {True: 0.25, False: 0.75}},
            "Hydrophobia": {
                "parents": ["Necronia flu"],
                "probabilities": {
                    True: {True: 0.95, False: 0.05},
                    False: {True: 0.01, False: 0.99}
                }
            },
            "Fatigue": {
                "parents": ["Hydrophobia"],
                "probabilities": {
                    True: {True: 0.9, False: 0.1},
                    False: {True: 0.3, False: 0.7}
                }
            },
            "Cysts": {
                "parents": ["Typhonus worm"],
                "probabilities": {
                    True: {True: 0.6, False: 0.4},
                    False: {True: 0.5, False: 0.5}
                }
            },
            "Tumors": {
                "parents": ["Cysts", "Scleraitis"],
                "probabilities": {
                    (True, True): {True: 0.85, False: 0.15},
                    (True, False): {True: 0.7, False: 0.3},
                    (False, True): {True: 0.7, False: 0.3},
                    (False, False): {True: 0.15, False: 0.85}
                }
            },
            "Mania": {
                "parents": ["Hydrophobia", "Typhonus worm"],
                "probabilities": {
                    (True, True): {True: 0.99, False: 0.01},
                    (True, False): {True: 0.4, False: 0.6},
                    (False, True): {True: 0.7, False: 0.3},
                    (False, False): {True: 0.05, False: 0.95}
                }
            },
            "Skin lesions": {
                "parents": ["Scleraitis"],
                "probabilities": {
                    True: {True: 0.55, False: 0.45},
                    False: {True: 0.2, False: 0.8}
                }
            },
            "Necrosis": {
                "parents": ["Skin lesions", "Scleraitis"],
                "probabilities": {
                    (True, True): {True: 0.9, False: 0.1},
                    (True, False): {True: 0.25, False: 0.75},
                    (False, True): {True: 0.35, False: 0.65},
                    (False, False): {True: 0.1, False: 0.9}
                }
            }
        }

    def _get_probability(self, var, evidence):
        node = self.network[var]
        if not node['parents']:
            return node['probabilities'][evidence.get(var, True)]
            
        parent_values = [evidence.get(parent, False) for parent in node['parents']]
        
        if len(parent_values) == 1:
            return node['probabilities'][parent_values[0]][evidence.get(var, True)]
            
        return node['probabilities'][tuple(parent_values)][evidence.get(var, True)]

    def _enumerate_all(self, variables, evidence):
        if not variables:
            return 1.0
            
        var = variables[0]
        rest = variables[1:]
        
        if var in evidence:
            prob = self._get_probability(var, evidence)
            return prob * self._enumerate_all(rest, evidence)
            
        prob_sum = 0.0
        for val in [True, False]:
            new_evidence = evidence.copy()
            new_evidence[var] = val
            prob = self._get_probability(var, new_evidence)
            prob_sum += prob * self._enumerate_all(rest, new_evidence)
        return prob_sum

    def query(self, variable, evidence):
        if variable in evidence:
            return float(evidence[variable])
            
        # Get variables in topological order
        ordered_vars = []
        visited = set()
        
        def visit(var):
            if var in visited:
                return
            visited.add(var)
            # Visit parents first
            for parent in self.network[var]['parents']:
                visit(parent)
            ordered_vars.append(var)
            # Visit children
            for child, info in self.network.items():
                if var in info['parents']:
                    visit(child)
        
        visit(variable)
        for ev in evidence:
            visit(ev)
        
        # Calculate P(variable=True | evidence)
        evidence_true = evidence.copy()
        evidence_true[variable] = True
        numerator = self._enumerate_all(ordered_vars, evidence_true)
        
        # Calculate P(evidence)
        evidence_false = evidence.copy()
        evidence_false[variable] = False
        denominator = numerator + self._enumerate_all(ordered_vars, evidence_false)
        
        return numerator / denominator if denominator > 0 else 0.0
