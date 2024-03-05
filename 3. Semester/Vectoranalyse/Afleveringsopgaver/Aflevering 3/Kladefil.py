from sympy import * 

def opgave1():
    s, t = symbols("s t")
    l = Matrix([[1+2*t],
                [-1+4*t],
                [2+3*t]])
    m = Matrix([[1-s],
                [1+2*s],
                [4*s]])
    def opgaveA(): 
        eq = l.cross(m)
        pprint(simplify(eq))

    def proj(v1, v2): 
        # pprint(simplify(v1.dot(v2)))
        # pprint(simplify(v1.dot(v1)))

        return (v1.dot(v2))/(v1.dot(v1)) * v1 
    def opgaveB():
        v1m = proj(l, m)
        v2l = proj(m, l)
        sol1 = solve(v1m)
        sol2 = solve(v2l)
        pprint(sol1)
        pprint(sol2)
        # Projektion

    opgaveB()
opgave1()

