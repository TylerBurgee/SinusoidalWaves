# SinusoidalWaves
Contains Sine and Cosine classes for generating and transforming sinusoidal waves.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install SinusoidalWaves.
```bash
pip install SinusoidalWaves
```

## Usage
```python
# IMPORT MODULES
from SinusoidalWaves import Sine, Cosine

# INITIALIZE WAVES WITH A GIVEN FREQUENCY
frequency = 5
sine = Sine(frequency)
cosine = Cosine(frequency)

# ROTATE WAVE 180° ABOUT THE Y-AXIS
sine.invert_amplitude()

# SHIFT WAVE 180° ALONG THE X-AXIS
cosine.shift_phase(3.14)

# SAVE WAVE TO FILE
filename = 'cosine.wav'
cosine.save(filename)

# MULTIPLY WAVE AMPLITUDE BY A GIVEN FACTOR
sine.mult_amplitude(0.5)

# GRAPH WAVE
sine.graph()
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
