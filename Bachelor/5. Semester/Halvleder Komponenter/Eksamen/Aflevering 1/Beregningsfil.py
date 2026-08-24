import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to define the plane from Miller indices
def plot_plane(ax, h, k, l, unit_cell_size, label):
    # Create a grid to plot over the unit cells
    xx, yy = np.meshgrid(np.linspace(0, unit_cell_size, 10), 
                         np.linspace(0, unit_cell_size, 10))
    
    # Plane equation: h/x + k/y + l/z = 1, solve for z
    if l != 0:
        zz = (1 - h * xx - k * yy) / l
    else:
        zz = np.zeros_like(xx)  # Planes parallel to z-axis
        
    # Plot the surface for this plane
    ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=100, cstride=100)
    ax.text(0, 0, 0, f'Plane {label}', color='black')

# Create figure and 3D axes
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Set plot limits based on 5 unit cells
unit_cells = 5
unit_cell_size = 1
ax.set_xlim([0, unit_cells * unit_cell_size])
ax.set_ylim([0, unit_cells * unit_cell_size])
ax.set_zlim([0, unit_cells * unit_cell_size])

plot_plane(ax, 1, -1, 0, unit_cell_size, label='(1,-1,0)')
plot_plane(ax, 2, -1, 0, unit_cell_size, label='(2,-1,0)')
# plot_plane(ax, -1, 0, 2, unit_cell_size, label='(-1,0,2)')
# Plot 5 unit cells
"""for i in range(unit_cells):
    # Define two planes on each unit cell with specified Miller indices
    if i == 0:
        plot_plane(ax, 1, -1, 0, unit_cell_size, label='(1,-1,0)')
        plot_plane(ax, -1, 0, 2, unit_cell_size, label='(-1,0,2)')
    elif i == 1:
        plot_plane(ax, 1, 1, -1, unit_cell_size, label='(1,1,-1)')
        plot_plane(ax, 2, -1, 0, unit_cell_size, label='(2,-1,0)')
    elif i == 2:
        plot_plane(ax, -2, -1, -2, unit_cell_size, label='(-2,-1,-2)')
        # Add more combinations if necessary...
"""
# Customize the view
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.title('Lattice Planes on Cubic Unit Cells')

# Show the plot
plt.show()