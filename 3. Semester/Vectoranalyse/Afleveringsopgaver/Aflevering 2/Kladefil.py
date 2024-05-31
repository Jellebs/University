from sympy import *

def fluxFdrParametricering(r, theta, r_vec, F_vec, r_grænse, theta_grænse ): 
    dr_r = diff(r_vec, (r, 1))
    dr_theta = diff(r_vec, (theta, 1))

    cross = dr_r.cross(dr_theta)
    print(cross)

    flux = integrate(integrate(F_vec.dot(cross),
                            r_grænse),
                            theta_grænse
        )
    return cross, flux

def opgave1(): 
    r, theta = symbols("r theta")
    r_vec = Matrix([r*cos(theta), r*sin(theta), 0])
    F_vec = Matrix([4*cos(theta)*sin(theta)**2, 4*cos(theta)**2 * sin(theta), 1/2])
    dr_r = diff(r_vec, (r, 1))
    dr_theta = diff(r_vec, (theta, 1))

    cross = dr_r.cross(dr_theta)
    print(cross)
    # fluxFdrParametricering(r, theta, r_vec, F_vec, )

def opgave2(): 
    r, theta = symbols("r theta")
    r_vec = Matrix([r*cos(theta), r*sin(theta), sqrt(1-r**2)])
    F_vec = Matrix([3*cos(theta), 2*sin(theta), -sqrt(1-r**2)])
    flux = fluxFdrParametricering(r, theta, r_vec, F_vec)
    pprint(flux)


def opgave3(): 
    r, R, theta = symbols("r R theta", positive = True)
    theta = symbols("theta")
    r_vec = Matrix([r*cos(theta), r*sin(theta), sqrt(R**2 - r**2)])
    F_vec = Matrix([2*cos(theta)/R**2, 2*sin(theta)/R**2, 2*sqrt(R**2 - r**2)/R**2])
    r_grænse = (r, 0, R)
    theta_grænse = (theta, 0, 2*pi)
    cross, Flux = fluxFdrParametricering(r, theta, r_vec, F_vec, r_grænse, theta_grænse)
    pprint(simplify(Flux))


opgave1()
