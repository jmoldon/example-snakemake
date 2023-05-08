import sys
from spectral_cube import SpectralCube
input_file = sys.argv[-1]

# Read the cube
cube = SpectralCube.read(input_file)

# Create and save moment0 map on disk
moment_0 = cube.moment(order=0, axis=0)
moment_0.write('results/data/moment0.fits', overwrite=True)
