#!/usr/bin/env python3
import numpy as np
import struct
import sys

# Generate 7.83 Hz sine wave
frequency = 7.83
duration = 13
sample_rate = 44100

t = np.linspace(0, duration, int(sample_rate * duration), False)
wave = np.sin(2 * np.pi * frequency * t)

# Fade in/out
fade = int(0.1 * sample_rate)
wave[:fade] *= np.linspace(0, 1, fade)
wave[-fade:] *= np.linspace(1, 0, fade)

# Convert to 16-bit PCM
wave_integers = np.int16(wave * 32767)

# Output raw audio to stdout
sys.stdout.buffer.write(wave_integers.tobytes())
