# Opgave 5.1
from sympy import * 
init_printing(use_unicode=True)

x, y, z = symbols("x y z")
a, b, c = symbols("a b c")
eqx = - sin(pi*z/c)
eqy = - sin(pi*x/a)
eqz = - sin(pi*y/b)

diffx = diff(eqx, z)
diffy = diff(eqy, x)
diffz = diff(eqz, y)
print(diffx, diffy, diffz, sep = "\n")


# Opgave 8.36 
def opgave8_36(): 
    E0, omega, beta, r, t, z, mu, eps= symbols("E0 omega beta r t z u eps")
    r_vec = Matrix([1, 0, 0])
    k_vec = Matrix([0, 1, 0])
    E = (E0*cos(omega*t - beta*z) / r ) * r_vec
    print(E)
    H = (E0*cos(omega*t - beta*z)/(r*sqrt(mu/eps))) * k_vec
    Poyting = E.cross(H)
    pprint(Poyting)



def opgave9_6(): 
    omega, t, beta, y = symbols("omega t beta y")
    E_vec = Matrix([1.333*cos(omega * t - beta * y), 0, 0])
    H_vec = Matrix([0, 0, -4.243*cos(omega*t - beta * y)])
    cross = E_vec.cross(H_vec)
    print(cross)

def opgave11_1(): 
    V0, omega, t = symbols("V0 omega t")
    epsilon, mu, z = symbols("epsilon mu z", positive = True)
    beta = omega*sqrt(epsilon*mu)
    expres_freq = V0*exp(-1j*omega*sqrt(epsilon*mu)*z)
    expres_tids = laplace_transform(expres_freq, omega, t, noconds = True)
    pprint(expres_tids)

    # opgave b 
    r = symbols("r", positive = True)
    
    a = -1j*beta*z
    E_freq = 1/r * exp(a) # V0 = 1
    ln_E_freq = ln(1/r) * a 
    ln_E_tids = inverse_laplace_transform(ln_E_freq, omega, t, noconds = True)

    pprint(ln_E_tids)
    
    # E_tids = inverse_laplace_transform(E_freq, omega, t, noconds= True)

    # pprint(E_tids)
    # pprint(ln(exp(1+5j)))




opgave11_1()

