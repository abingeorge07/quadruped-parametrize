'''
Goal: convert the stl file according the the mujoco xml format
'''

import numpy as np
import collada
import aspose.threed as a3d

# Load the DAE file
dae = collada.Collada('models/unitree_a1/unitree_a1/meshes/trunk.dae')

# Access the mesh
mesh = dae.geometries[0].primitives[0]

# print(mesh)
# input("Press Enter to continue...")

# print(mesh.vertex)
# input("Press Enter to continue...")

# print(len(mesh.vertex))
# input("Press Enter to continue...")

# print(len(mesh.vertex[0]))
# input("Press Enter to continue...")



# Modify the vertices (example: translate all vertices by 1 unit in the x direction)
for i in range(0, len(mesh.vertex), 1):
    for j in range(0, len(mesh.vertex[i]), 1):
        mesh.vertex[i][j] = mesh.vertex[i][j] * 1.4  

# Save the modified mesh to a new DAE file
dae.write('models/unitree_a1/unitree_a1/meshes/trunk_modified.dae')

# converting to obj
scene = a3d.Scene.from_file('models/unitree_a1/unitree_a1/meshes/trunk_modified.dae')

save_options = a3d.formats.ObjSaveOptions()
save_options.enable_materials = True

scene.save('models/unitree_a1/unitree_a1/assets/trunk_modified.obj',  save_options)
