import random
from time import sleep

dictionary  = 'abcdefghijklmnopqrstuvwxyz'
numbers     = '0123456789'
symbols     = '{}[]()@#$%&-+*!^~?/'

word        = dictionary + dictionary.upper() + numbers + symbols

try:
    length      = int(input("Quantos caracteres sua senha deve conter? "))
    password    = "".join(random.sample(word, length))
    print('Gerando senha...')
    sleep(3)
    print(f'Sua senha é: {password}')
except:
    print(f'O tamanho da sua senha deve ser menor que {len(word)}')
