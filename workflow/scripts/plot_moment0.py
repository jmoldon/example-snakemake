import sys
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.wcs import WCS

moment0_file = snakemake.input[0]
outputfile = 'results/publication/figures/moment0.png'

hdu = fits.open(moment0_file)[0]
wcs = WCS(hdu.header)

plt.subplot(projection=wcs)

mask_threshold = 350
my_viridis = plt.cm.get_cmap('viridis_r', mask_threshold).with_extremes(
    under='white'
)
plt.imshow(
    hdu.data, cmap=my_viridis, vmin=mask_threshold, vmax=2.2e3, origin='lower'
)

# Overlay contours
plt.contour(
    hdu.data,
    levels=mask_threshold * np.array([1, 2, 3]),
    colors='black',
    alpha=0.5,
)

# Select region to plot
central_pixel_x = 201
central_pixel_y = 199
deg_per_pixel = 0.001111111111111
span = 0.4 / deg_per_pixel

plt.xlim(central_pixel_x - span / 2, central_pixel_x + span / 2)
plt.ylim(central_pixel_y - span / 2, central_pixel_y + span / 2)

plt.grid(color='black', alpha=0.25, ls='solid')
plt.xlabel('Right Ascension')
plt.ylabel('Declination')

plt.savefig(outputfile, bbox_inches='tight', dpi=200)
