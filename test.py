import math
import mujoco
import mujoco_viewer
import time
import os

DELAY_MSEC 	= 5.0


# # set intial position for the quadruped
# def set_intial_pos(model, data):
    
#     for i in range(7, model.nq, 2):

#         if(i == 7 or i == 11):
#             model.qpos0[i] = 0.94
#         else:
#             model.qpos0[i] = 0.5
        
#         model.qpos0[i+1] = -1.6




model = mujoco.MjModel.from_xml_path("./models/unitree_a1/unitree_a1/scene_new.xml")
data = mujoco.MjData(model)
mujoco.mj_resetDataKeyframe(model, data, 0)



# create the viewer object
viewer = mujoco_viewer.MujocoViewer(model, data)

# simulate and render
mujoco.mj_step(model,data)
# t_start = time.time()

# set_intial_pos(model, data)

i = 0
while viewer.is_alive:

    simstart = data.time
    
    while(data.time - simstart < DELAY_MSEC/1000):
        mujoco.mj_step(model,data)
        mujoco.mj_kinematics(model, data)
        
    viewer.render()


  

mujoco.mj_deleteData(data)
mujoco.mj_deleteModel(model)

# close
# viewer.close()