import emodeconnection as emc
def simulate(wavelength, grid, w_trench, w_core, h_core, h_clad, mat_core, mat_clad): 
    em = emc.EMode()
    ## Draw shapes
    ## Settings
    
    em.settings(
        wavelength = wavelength, x_resolution = grid, y_resolution = grid,
        window_width = w_core + w_trench*2, window_height = h_core + h_clad*2,
        num_modes = 2, background_material = 'Air')
    em.shape(name = 'BOX', material = mat_clad, height = h_clad)
    em.shape(name = 'core', material = mat_core, width = w_core, height = h_core)
    ## Launch FDM solver
    em.FDM()

    ## Display the effective indices, TE fractions, and core confinement
    em.report()

    ## Plot the field and refractive index profiles
    em.plot()
    em.close()