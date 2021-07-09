title = """
    _    _                             _       
   / \\  | |__   ___  _ __ ___ __ _  __| | ___  
  / _ \\ | '_ \\ / _ \\| '__/ __/ _` |/ _` |/ _ \\ 
 / ___ \\| | | | (_) | | | (_| (_| | (_| | (_) |
/_/   \\_\\_| |_|\\___/|_|  \\___\\__,_|\\__,_|\\___/ 

"""



IMAGENES_AHORCADO = [
'''
    +---+
    |   |
        |
        |
        |
==========''',
'''
    +---+
    |   |
    O   |
        |
        |
==========''',
'''
    +---+
    |   |
    O   |
    |   |
        |
==========''',
'''
    +---+
    |   |
    O   |
   /|   |
        |
==========''',
'''
    +---+
    |   |
    O   |
   /|\\  |
        |
==========''',
'''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
==========''',
'''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
==========''',
'''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
==     ==='''
]

start_screen = title + IMAGENES_AHORCADO[7] + """

Presiona Enter para continuar

"""

text = {
  "title": title,
  "start_screen": start_screen
}