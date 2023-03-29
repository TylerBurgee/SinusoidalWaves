"""
Author: Tyler J. Burgee
Last Modification Date: 29 March 2023
"""

# IMPORT MODULES
from SinusoidalWaves.AbstractWave import Wave
import numpy as np

class Sine (Wave):
    """Class to represent a sine wave"""

    def __init__(self, freq: int, duration=1,  sample_rate=10000) -> None:
        """Defines the constructor for a Sine object"""
        super().__init__(freq, duration, sample_rate)

        # ASSIGN SINE WAVE COORDINATE POINTS TO self.wave
        self.wave = self._generate_()

    def __repr__(self) -> str:
        """Returns the string representation of a Sine object"""
        return "Sine Wave: {} hertz, {} seconds, {} sample rate.".format(
            self.freq, self.duration, self.sample_rate)

    def _generate_(self) -> None:
        """Generates a sine wave and returns its coordinate values"""
        x = np.linspace(0, self.duration, self.sample_rate * self.duration,
                        endpoint=False)
        frequencies = x * self.freq * self.inversion_factor
        y = np.sin((2 * np.pi) * frequencies + self.phase_shift)

        coords = {"x":x, "y":y}

        return coords

if __name__ == "__main__":
    # INSTANTIATE Sine OBJECT
    sine = Sine(2)

    # GRAPH SINE WAVE
    sine.graph()
