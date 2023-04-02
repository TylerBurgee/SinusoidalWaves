"""
Author: Tyler J. Burgee
Last Modification Date: 2 April 2023
"""

# IMPORT MODULES
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import sys
import math

class Wave:
    """Class to represent a wave of non-specified type"""

    def __init__(self, freq: float, duration=1,  sample_rate=10000, components=None) -> None:
        """Defines the constructor for a Wave object"""
        self.freq = freq
        self.duration = duration
        self.sample_rate = sample_rate
        self.components = components

        self.inversion_factor = 1
        self.phase_shift = 0
        self.amplitude_factor = 1

        # ASSIGN ABSTRACT WAVE COORDINATE POINTS TO self._wave_
        self._wave_ = None
        self._wave_ = self._generate_()

    def __str__(self) -> str:
        """Returns the string representation of a Wave object"""
        return "Wave: {} hertz, {} seconds, {} sample rate.".format(
            self.freq, self.duration, self.sample_rate)

    def __add__(self, other: object) -> object:
        """
        Adds two Wave objects, returns a new Wave object representing
        the sum of their amplitudes.
        """
        y = self._wave_["y"]
        y += other._wave_["y"]

        x = np.linspace(0, self.duration, self.sample_rate * self.duration,
                        endpoint=False)
        y = np.float64(y)

        coords = {"x":x, "y":y}

        wave = Wave(2*math.pi, components=[self, other])
        wave._wave_ = coords

        return wave

    def __sub__(self, other: object) -> object:
        """
        Subtracts two Wave objects, returns a new Wave object representing
        the difference of their amplitudes.
        """
        y = self._wave_["y"]
        y -= other._wave_["y"]

        x = np.linspace(0, self.duration, self.sample_rate * self.duration,
                        endpoint=False)
        y = np.float64(y)

        coords = {"x":x, "y":y}

        wave = Wave(2*math.pi, components=[self, other])
        wave._wave_ = coords

        return wave

    def _generate_(self) -> None:
        """
        Generates a wave of non-specified type,
        returns its coordinate values
        """

        x = np.linspace(0, self.duration, self.sample_rate * self.duration,
                        endpoint=False)
        frequencies = x * self.freq

        # INITIALIZE AMPLITUDES TO 0
        y = np.sin((0) * frequencies)

        if self.components is not None:
            for i, component in enumerate(self.components):
                if self.is_shifted():
                    component.shift_phase(self.phase_shift)
                if self.is_inverted():
                    component.invert_amplitude(self.inversion_factor)
                # ADD AMPLITUDES OF COMPONENT WAVES
                y += component._wave_["y"] * self.inversion_factor

            y = np.float64(y) * self.amplitude_factor

        coords = {"x":x, "y":y}

        return coords

    def graph(self) -> None:
        """Displays a graph of a Wave object"""
        if self._wave_ is not None:
            plt.plot(self._wave_["x"], self._wave_["y"])
            plt.show()

    def save(self, filename: str) -> None:
        """Saves a Wave object to .wav file"""
        if ".wav" in filename:
            signal = np.int16((self._wave_["y"] / self._wave_["y"].max()) * 32767)
            wavfile.write(filename, self.sample_rate, signal)
        else:
            raise Exception("Filename must include .wav extension.")

    def invert_amplitude(self, inversion_factor=None) -> None:
        """Inverts the amplitude of a Wave object"""
        if inversion_factor is None:
            self.inversion_factor = -self.inversion_factor
        else:
            self.inversion_factor = -inversion_factor
        self._wave_ = self._generate_()

    def mult_amplitude(self, factor: float) -> None:
        """Multiplies the amplitude of a Wave object by a given factor"""
        self.amplitude_factor = factor
        self._wave_ = self._generate_()

    def shift_phase(self, x: float) -> None:
        """Shifts the phase of a Wave object by the given factor"""
        self.phase_shift += x
        self._wave_ = self._generate_()

    def is_inverted(self) -> bool:
        """Returns true if a Wave object is rotated about the y-axis"""
        return self.inversion_factor == -1

    def is_shifted(self) -> bool:
        """Returns true if a Wave object is shifted along the x-axis"""
        return self.phase_shift % 2*math.pi != 0

    def set_freq(self, freq: float) -> None:
        """Sets the frequency of a Wave object"""
        self.freq = freq
        self._wave_ = self._generate_()

    def set_duration(self, duration: float) -> None:
        """Sets the duration of a Wave object"""
        self.duration = duration
        self._wave_ = self._generate_()

    def set_sample_rate(self, sample_rate: int) -> None:
        """Sets the sample rate of a Wave object"""
        self.sample_rate = sample_rate
        self._wave_ = self._generate_()

    def get_freq(self) -> float:
        """Gets the frequency of a Wave object"""
        return self.freq

    def get_duration(self) -> int:
        """Gets the duration of a Wave object"""
        return self.duration

    def get_sample_rate(self) -> int:
        """Gets the sample rate of a Wave object"""
        return self.sample_rate


class Sine (Wave):
    """Class to represent a sine wave"""

    def __init__(self, freq: float, duration=1,  sample_rate=10000) -> None:
        """Defines the constructor for a Sine object"""
        super().__init__(freq, duration, sample_rate)

    def __str__(self) -> str:
        """Returns the string representation of a Sine object"""
        return "Sine Wave: {} hertz, {} seconds, {} sample rate.".format(
            self.freq, self.duration, self.sample_rate)

    def _generate_(self) -> dict:
        """Generates a sine wave and returns its coordinate values"""
        x = np.linspace(0, self.duration, self.sample_rate * self.duration,
                        endpoint=False)
        y = np.sin((2 * np.pi) * (x * self.freq * self.inversion_factor) + self.phase_shift) * self.amplitude_factor

        coords = {"x":x, "y":y}

        return coords


class Cosine (Wave):
    """Class to represent a cosine wave"""

    def __init__(self, freq: float, duration=1,  sample_rate=10000) -> None:
        """Defines the constructor for a Cosine object"""
        super().__init__(freq, duration, sample_rate)

    def __str__(self) -> str:
        """Returns the string representation of a Cosine object"""
        return "Cosine Wave: {} hertz, {} seconds, {} sample rate.".format(
            self.freq, self.duration, self.sample_rate)

    def _generate_(self) -> dict:
        """Generates a cosine wave and returns its coordinate values"""
        x = np.linspace(0, self.duration, self.sample_rate * self.duration,
                        endpoint=False)
        y = np.cos((2 * np.pi) * (x * self.freq * self.inversion_factor) + self.phase_shift) * self.amplitude_factor

        coords = {"x":x, "y":y}

        return coords


if __name__ == "__main__":
    sin = Sine(2)
    cos = Cosine(5)

    wav = sin + cos

    wav.graph()
