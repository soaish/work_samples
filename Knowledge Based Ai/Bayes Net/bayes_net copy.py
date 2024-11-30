class BayesNet:
    """
    Feel free to add additional internal methods to this class.
    """

    def __init__(self):
        """
        Add any code to the constructor if you need.
        """
        pass

    def query(self, variable: str, evidence: dict[str, bool]) -> float:
        """
        This is the main function you need to implement.
        """

        return 0.0

if __name__ == "__main__":

    net = BayesNet()
    print(net.query('Typhonus worm', {'Mania': True, 'Tumors': False}))
