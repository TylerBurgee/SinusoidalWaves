"""
Author: Tyler J. Burgee
Date: 10 March 2023
"""

# IMPORT MODULES
import numpy as np
import matplotlib.pyplot as plt

class SineWave:
    """Class to represent a sine wave"""

    def __init__(self, freq: int, duration=1,  sample_rate=10000) -> None:
        """Defines the constructor for a SineWave object"""
        self.freq = freq
        self.duration = duration
        self.sample_rate = sample_rate
        self.inversion_factor = 1
        self.phase_shift = 0

        # ASSIGN SINE WAVE COORDINATE POINTS TO self.wave
        self.wave = None
        self._generate_()

    def __repr__(self) -> str:
        """Returns the string representation of a SineWave object"""
        return "Sine Wave: {} hertz, {} seconds, {} sample rate.".format(self.freq, self.duration, self.sample_rate)

    def _generate_(self) -> None:
        """Generates a sine wave and returns its coordinate values"""
        x = np.linspace(0, self.duration, self.sample_rate * self.duration, endpoint=False)
        frequencies = x * self.freq * self.inversion_factor
        y = np.sin((2 * np.pi) * frequencies + self.phase_shift)

        coords = {"x":x, "y":y}

        self.wave = coords

    def graph(self) -> None:
        """Displays a graph of a SineWave object"""
        plt.plot(self.wave["x"], self.wave["y"])
        plt.show()

    def invert_amplitude(self) -> None:
        """Inverts the amplitude of a SineWave object"""
        self.inversion_factor = -self.inversion_factor
        self._generate_()

    def shift_phase(self, factor: float) -> None:
        """Shifts the phase of a SineWave object by the given factor"""
        self.phase_shift += factor
        self._generate_()

    def set_freq(self, freq: float) -> None:
        """Sets the frequency of a SineWave object"""
        self.freq = freq
        self._generate_()

    def set_duration(self, duration: float) -> None:
        """Sets the duration of a SineWave object"""
        self.duration = duration
        self._generate_()

    def set_sample_rate(self, sample_rate: int) -> None:
        """Sets the sample rate of a SineWave object"""
        self.sample_rate = sample_rate
        self._generate_()

    def get_freq(self) -> int:
        """Gets the frequency of a SineWave object"""
        return self.freq

    def get_duration(self) -> int:
        """Gets the duration of a SineWave object"""
        return self.duration

    def get_sample_rate(self) -> int:
        """Gets the sample rate of a SineWave object"""
        return self.sample_rate

if __name__ == "__main__":
    # IMPORT MODULES
    from matplotlib import pyplot as plt

    # INSTANTIATE SineWave OBJECT
    sine = SineWave(2)

    # ROTATE SINE WAVE ABOUT X-AXIS
    sine.invert_amplitude()

    # SHIFT SINE WAVE PHASE BY 180°
    sine.shift_phase(np.pi)

    # GRAPH SINE WAVE
    sine.graph()
