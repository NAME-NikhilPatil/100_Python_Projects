import self
import sounddevice as sd
import soundfile as sf
import numpy as np
from scipy.io.wavfile import write

sd.default.samplerate = 44100


class SoundWaves:
    def __init__(self):
        # ' Hint: wave files are only usable if they autoplay, when opening
        # them
        # directly
        # with a sound tool in windows or MACOS
        # ' Hint: show your sound devices: print(sd.query_devices())

        self.short_beep = 'beep_short.wav'
        self.long_beep = 'beep_long.wav'
        self.sound_array = []
        self.pause = np.zeros([20000, 2], dtype="float32")
        self.longer_pause = np.zeros([120000, 2], dtype="float32")

    def save_char(self, value_encoder):
        """saves the morse sound of one char in list
            :param value_encoder: list of morse_digits for the respective char
            :return None
        """

        for code in value_encoder:
            if code == 1:
                data, fs = sf.read(self.short_beep)
            else:
                data, fs = sf.read(self.long_beep)

            self.sound_array.append(sd.playrec(data,
                                               fs,
                                               channels=2,
                                               dtype="float32",
                                               blocking=True))
            self.sound_array.append(self.pause)

    def save_wav_format(self) -> None:
        """saves the morse sound of one char in list
            :param None
            :return soundfile in wav-format (no real return value)
        """
        new = np.vstack(self.sound_array)
        write(f'output.wav', 44100, new)

    def add_longer_pause(self) -> None:
        """Adds a long pause after the word
            Is only hearable in the output not when recording
            :param None
            :return None
        """
        self.sound_array.append(self.longer_pause)
