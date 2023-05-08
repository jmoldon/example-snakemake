import sys
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import aplpy

moment0_file = sys.argv[-1]

# Read the moment0 file
moment0 = fits.open(moment0_file)[0]   # Select primary HDU

# Generate figure
mom0 = aplpy.FITSFigure(moment0)

# Re-centre and set size
mom0.recenter(32.45, -10.225, radius=0.2)

# Set colour map for moment 0
viridis_cmap = plt.cm.viridis_r
viridis_cmap.set_under(color='w')

# Add beam ellipse
mom0.add_beam()
mom0.beam.set_color('k')
mom0.beam.set_corner('bottom right')

# Display the data with the chosen colour map
mom0.show_colorscale(
    cmap=viridis_cmap, vmin=300, vmax=2.2e3, interpolation='none'
)

# Add gridlines
mom0.add_grid()
mom0.grid.set_color('black')
mom0.grid.set_alpha(0.25)

# Add arrows labelling features
mom0.show_arrows(
    [32.5650, 32.4848, 32.3674, 32.4498, 32.5119, 32.5367],
    [-10.3841, -10.3197, -10.1808, -10.0575, -10.1530, -10.2141],
    [0.0407, 0.0248, 0.0079, -0.0260, -0.0362, -0.0350],
    [0.0212, 0.0512, 0.0389, -0.0433, -0.0189, 0.0011],
    color='k',
    width=0.5,
)

mom0.add_label(32.5630, -10.3841, 'NGC848S tail', horizontalalignment='left')
# mom0.add_label(32.4828,-10.3197,'SE tail',horizontalalignment='left')
mom0.add_label(32.3654, -10.1808, 'NW tail', horizontalalignment='left')
mom0.add_label(32.4538, -10.0575, 'NE tail', horizontalalignment='right')
mom0.add_label(32.5139, -10.1530, 'E clump', horizontalalignment='right')
mom0.add_label(32.5387, -10.2141, 'S clump', horizontalalignment='right')

# Overlay contours
mom0.show_contour(moment0, colors=['black'], levels=np.linspace(300, 2000, 4))
#                     levels=[-0.025],linestyle='--')

mom0.save('results/publication/figures/moment0.png')
