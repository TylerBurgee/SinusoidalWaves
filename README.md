# SinusoidalWaves
Contains Sine and Cosine classes for generating and transforming sinusoidal waves.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install SinusoidalWaves.
```bash
pip install SinusoidalWaves
```

## Usage
```python
# IMPORT MODULE
from SinusoidalWaves import Sine
from SinusoidalWaves import Cosine

# INITIALIZE WAVES WITH A GIVEN FREQUENCY
frequency = 5
sine = Sine(frequency)
cosine = Cosine(frequency)

# ROTATE SINE WAVE 180° ABOUT THE Y-AXIS
sine.invert_amplitude()
# SHIFT COSINE WAVE 180° ALONG THE X-AXIS
cosine.shift_phase(3.14)

# GRAPH WAVES
sine.graph()
#cosine.graph()
```

## Future Update
I am creating \_\_add__() and \_\_sub__() methods for the Wave class, enabling the generation of complex waves.

## License
[MIT](https://choosealicense.com/licenses/mit/)
