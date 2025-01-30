import numpy as np
import pymeshlab
from stl import mesh
import open3d as o3d

# Create a MeshSet object
ms = pymeshlab.MeshSet()

# Load the DAE file
ms.load_new_mesh('models/unitree_a1/unitree_a1/meshes/calf.dae')

# Save the mesh as STL
ms.save_current_mesh('models/unitree_a1/unitree_a1/stl/calf.stl')

# Load the STL file
your_mesh = mesh.Mesh.from_file('models/unitree_a1/unitree_a1/stl/calf.stl')

# initial properties 
vol_init, cog_init, inertia_init = your_mesh.get_mass_properties()

print("Initial volume: {}".format(vol_init))
print("Initial center of gravity: {}".format(cog_init))
print("Initial inertia: {}".format(inertia_init))


# Define the scaling factor
scale_factor = 1.5

# Scale the mesh
# your_mesh.x *= scale_factor
# your_mesh.y *= scale_factor
your_mesh.z *= scale_factor

# initial properties 
vol_init, cog_init, inertia_init = your_mesh.get_mass_properties()

print("Final volume: {}".format(vol_init))
print("Final center of gravity: {}".format(cog_init))
print("Final inertia: {}".format(inertia_init))

# Save the scaled STL file
your_mesh.save('models/unitree_a1/unitree_a1/stl/calf_modified.stl')

mesh = o3d.io.read_triangle_mesh('models/unitree_a1/unitree_a1/stl/calf_modified.stl')
o3d.io.write_triangle_mesh('models/unitree_a1/unitree_a1/assets/calf_modified.obj', mesh)

