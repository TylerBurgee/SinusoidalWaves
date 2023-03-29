from distutils.core import setup
setup(
  name = 'SinusoidalWaves',
  packages = ['SinusoidalWaves'],
  version = '0.1',
  license='MIT',
  description = 'Contains Sine and Cosine classes for generating and transforming sinusoidal waves.',
  author = 'Tyler Burgee',
  author_email = 'tylerburgee@gmail.com',
  url = 'https://github.com/TylerBurgee/SinusoidalWaves',
  download_url = 'https://github.com/TylerBurgee/SinusoidalWaves/archive/refs/tags/v_0.1.tar.gz',
  keywords = ['waves', 'sine', 'cosine', 'transformation', 'signal', 'processing'],
  install_requires=[
          'numpy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11'
  ],
)
