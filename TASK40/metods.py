from random import randint

def create_string (different_chars):
    symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    text = ''
    for i in range (different_chars):
        amount_symb = randint(1, 5)
        text += amount_symb * symbols[randint(0, 51)]
    return text

def inputs(message):
    num = int(input(message))
    return num