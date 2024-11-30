
def is_var(x):
    """
    A helper function that checks if the provided expression x is a variable,
    i.e., a string that starts with ?.

    >>> is_variable('?x')
    True
    >>> is_variable('x')
    False
    """
    return isinstance(x, str) and len(x) > 0 and x[0] == "?"

def substitute(s: dict, x: tuple):
    """
    A helper function that substitute the bindings from s into the expression x.

    >>> substitute({'?x': 'Chris', '?y': 'Dog'}, ('likes', '?x', '?y'))
    ('likes', 'Chris', 'Dog')

    >>> substitute({'?x': 'Dog', '?y': ('owner', '?x')}, ('likes', '?y', '?x'))
    ('likes', ('owner', 'Dog'), 'Dog')

    >>> substitute({'?x': 'Dog'}, '?x')
    'Dog'
    """
    if x in s:
        return substitute(s, s[x])
    elif isinstance(x, tuple):
        return tuple(substitute(s, xi) for xi in x)
    else:
        return x

def unify(x, y, s=()):
    """
    Unify expressions x and y given a provided substitution s.  By default s is
    (), which gets recognized and replaced with an empty dictionary.  Return a
    substitution (a dict) that will make x and y equal or, if this is not
    possible, then it returns None.

    >>> unify(('likes', '?a', 'B'), ('likes', 'A', 'B'), {})
    {'?a': 'A'}

    >>> unify(('likes', '?a', 'B'), ('likes', 'A', '?b'), {})
    {'?a': 'A', '?b': 'B'}
    """
    if s == ():
        s = {}

    if x == y:
        return s
    
    if is_var(x):
        return unify_var(x, y, s)
    
    if is_var(y):
        return unify_var(y, x, s)
    
    if isinstance(x, tuple) and isinstance(y, tuple):

        if len(x) != len(y):
            return None
        
        for X, Y in zip(x, y):

            s = unify(X, Y, s)

            if s is None:
                return None
            
        return s
    
    return None


def unify_var(var, x, s):
    
    if var in s:
        return unify(s[var], x, s)
    
    if is_var(x):
        return unify(x, var, s)
    
    s[var] = x

    return s

def pattern_match(query, kb, substitution=None):
    """
    Similar to unify, but operates over multiple predicates. A query is a list
    of predicates, some of which may contain variables. A knowledge base (kb) is
    a list of predicates without any variables. Substitutions is a dictionary
    mapping variable to values.

    >>> pattern_match([('likes', '?x', 'Dog'), ('has', '?x', 'food')], [('likes', 'Chris', 'Dog'), ('likes', 'Fred', 'Dog'), ('likes', 'Elizabeth', 'Dog'), ('has', 'Chris', 'food'), ('has', 'Elizabeth', 'food')])
    [{'?x': 'Chris'}, {'?x': 'Elizabeth'}]
    """
    if substitution is None:
        substitution = {}

    results = []

    for predicate in kb:
        s = unify(query[0], predicate, substitution.copy())

        if s is not None:

            if len(query) == 1:
                results.append(s)
                
            else:
                recursive_result = pattern_match(query[1:], kb, s)

                if recursive_result:
                    results.extend(recursive_result)

    return results