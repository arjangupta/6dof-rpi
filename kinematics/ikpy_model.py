import ikpy.chain
import numpy as np
import ikpy.utils.plot as plot_utils

# Create the chain
sixdof_chain = ikpy.chain.Chain.from_urdf_file("kinematics/sixdof_arm.urdf")

# Inverse kinematics
target_position = [6.1, 6.1, 1.1]
print("The angles of each joints are : ", sixdof_chain.inverse_kinematics(target_position))
real_frame = sixdof_chain.forward_kinematics(sixdof_chain.inverse_kinematics(target_position))
print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_position))

# Plot
import matplotlib.pyplot as plt
fig, ax = plot_utils.init_3d_figure()
sixdof_chain.plot(sixdof_chain.inverse_kinematics(target_position), ax, target=target_position)
plt.xlim(0, 10)
plt.ylim(0, 10)