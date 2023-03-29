"""
Author: Tyler J. Burgee
Last Modification Date: 29 March 2023
"""

# IMPORT MODULES
import matplotlib.pyplot as plt
import sys
import math

class Wave:
    """Class to represent a wave of non-specified type"""

    def __init__(self, freq: int, duration=1,  sample_rate=10000) -> None:
        """Defines the constructor for a Wave object"""
        self.freq = freq
        self.duration = duration
        self.sample_rate = sample_rate
        self.inversion_factor = 1
        self.phase_shift = 0

        # ASSIGN ABSTRACT WAVE COORDINATE POINTS TO self.wave
        self.wave = self._generate_()

    def __repr__(self) -> str:
        """Returns the string representation of a Wave object"""
        return "Wave: {} hertz, {} seconds, {} sample rate.".format(
            self.freq, self.duration, self.sample_rate)

    def _generate_(self) -> None:
        """Sets abstract wave coordinates to NoneType"""
        coords = None
        return coords

    def graph(self) -> None:
        """Displays a graph of a Wave object"""
        if self.wave is not None:
            plt.plot(self.wave["x"], self.wave["y"])
            plt.show()

    def invert_amplitude(self) -> None:
        """Inverts the amplitude of a Wave object"""
        self.inversion_factor = -self.inversion_factor
        self.wave = self._generate_()

    def shift_phase(self, factor: float) -> None:
        """Shifts the phase of a Wave object by the given factor"""
        self.phase_shift += factor
        self.wave = self._generate_()

    def is_inverted(self) -> bool:
        """Returns true if a Wave object is rotated about the y-axis"""
        return self.inversion_factor == -1

    def is_shifted(self) -> bool:
        """Returns true if a Wave object is shifted along the x-axis"""
        return self.phase_shift % 2*math.pi != 0

    def set_freq(self, freq: float) -> None:
        """Sets the frequency of a Wave object"""
        self.freq = freq
        self.wave = self._generate_()

    def set_duration(self, duration: float) -> None:
        """Sets the duration of a Wave object"""
        self.duration = duration
        self.wave = self._generate_()

    def set_sample_rate(self, sample_rate: int) -> None:
        """Sets the sample rate of a Wave object"""
        self.sample_rate = sample_rate
        self.wave = self._generate_()

    def get_freq(self) -> int:
        """Gets the frequency of a Wave object"""
        return self.freq

    def get_duration(self) -> int:
        """Gets the duration of a Wave object"""
        return self.duration

    def get_sample_rate(self) -> int:
        """Gets the sample rate of a Wave object"""
        return self.sample_rate

if __name__ == "__main__":
    message = """
        "Wave" module only provides backend functionality for
        SineWave and CosineWave modules. Therefore, it cannot be run
        as a main script."""

    sys.exit(message)
