from sounds import SoundWaves

new_sound = SoundWaves()
sentence = input("Hello there please type your message. "
                 "We will then encode the message into a beeping "
                 "file to send it to your friends for communication:")

convert_dict = {
    "A": [1, 2], "B": [2, 1, 1, 1], "C": [2, 1, 2, 1], "D": [2, 1, 1],
    "E": [1], "F": [1, 1, 2, 1], "G": [2, 2, 1], "H": [1, 1, 1, 1],
    "I": [1, 1], "J": [1, 2, 2, 2], "K": [2, 1, 2], "L": [1, 2, 1, 1],
    "M": [2, 2], "N": [2, 1], "O": [2, 2, 2], "P": [1, 2, 2, 1],
    "Q": [2, 2, 1, 2], "R": [1, 2, 1], "S": [1, 1, 1], "T": [2],
    "U": [1, 1, 2], "V": [1, 1, 1, 2], "W": [1, 2, 2], "X": [2, 1, 1, 2],
    "Y": [2, 1, 2, 2], "Z": [2, 2, 1, 1],
    "0": [2, 2, 2, 2, 2], "1": [1, 2, 2, 2, 2], "2": [1, 1, 2, 2, 2],
    "3": [1, 1, 1, 2, 2], "4": [1, 1, 1, 1, 2], "5": [1, 1, 1, 1, 1],
    "6": [2, 1, 1, 1, 1], "7": [2, 2, 1, 1, 1], "8": [2, 2, 2, 1, 1],
    "9": [2, 2, 2, 2, 1]
}


def return_sound(sound_dict: dict, convert: str) -> None:
    """returns the sound of the written letters and numbers.
    :param sound_dict: the dictionary containing letters and numbers
    :param convert: the actual string typed by the user to convert to morse code.
    :return None
    """

    convert = list(convert)

    for char in convert:
        char = char.capitalize()
        if char in sound_dict:
            value = sound_dict[char]
            new_sound.save_char(value)
        else:
            new_sound.add_longer_pause()


return_sound(convert_dict, sentence)
new_sound.save_wav_format()
