from ikpy.chain import Chain
from ikpy.link import Link
from ikpy.utils import plot
from mpl_toolkits.mplot3d import Axes3D;

# Declare links
link_1 = Link("link_1", length=3)

# Build the whole chain
main_chain = Chain(name='main_chain', links=[link_1])

# Plot
fig, ax = plot.init_3d_figure()
main_chain.plot([0] * (len(main_chain)), ax)
ax.legend()