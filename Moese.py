def morse(Morse, key_input):
    lst = []
    result = ''
    lst = key_input.split()
    for code in lst:
        if code in Morse:
            result += Morse[code]
    return result

Morse = {
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9"
}

key_input = "..--- ----- .---- ---.."
print(morse(Morse, key_input))
