class Cfg:
    def __init__(self, V, T, P, S):
        self.V = V
        self.T = T
        self.P = P
        self.S = S

    def __str__(self):
        val = ""
        for head in self.P:
            for bodies in self.P[head]:
                    val += "%s → %s\n" % (head, " ".join(bodies))
        return val
