"""
Author: Tyler J. Burgee
Last Modification Date: 2 April 2023
"""

# IMPORT MODULES
from Waves import Sine

# SET FUNDAMENTAL FREQUENCY FOR TRIANGLE WAVE
f = 250

# INSTANTIATE Sine OBJECT WITH fundamental_freq
triangle_wave = Sine(f)

for x in range (1, 200):
    # ONLY ADD ODD HARMONIC FREQUENCIES
    if x % 2 == 1:
        # INSTANTIATE Sine OBJECT
        sine = Sine(f * x)

        # ADD NEW Sine OBJECT TO triangle_wave
        triangle_wave += sine

        # INVERT EVERY OTHER ODD HARMONIC FREQUENCY
        if x % 2 == 0:
            sine.invert_amplitude()

# SAVE triangle_wave TO FILE
filename = "triangle.wav"
triangle_wave.save(filename)
print("Triangle wave with f={} has been saved to {}".format(f, filename))
