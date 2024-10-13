morse_code_rules = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
                    '-': '-....-', '(': '-.--.', ')': '-.--.-'}

ans = input('Morse Code Converter\nType text to convert to Morse Code!\n')
output_list = []


def text_to_morse():
    for letter in ans:
        if letter.upper() in morse_code_rules:
            output_list.append(morse_code_rules[letter.upper()])
        else:
            output_list.append('')  # Handle unsupported characters


text_to_morse()

result = ' '.join(output_list)
print(f'The Morse Code of {ans} is {result}')
