import assets
import os
import sys
import random

def clear_screen():
  command = "clear"

  if sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    command = "cls"
  
  os.system(command)


def clean_latin_chars(word_string=""):
  latin_chars       = "ÁÉÍÓÚ"
  sustitution_chars = "AEIOU"
  result_word = [char for char in word_string]

  for word_char in range(0, len(word_string)):
    for lat_char in range(0, len(latin_chars)):
      if result_word[word_char] == latin_chars[lat_char]:
        result_word[word_char] = sustitution_chars[lat_char]

  return result_word



def render_start_screen():
  print(assets.text["start_screen"])
  input()



def load_and_format_words():
  words = []
  with open('./archivos/data.txt', "r", encoding="utf-8") as f:
      for line in f:
          words.append(clean_latin_chars(line.strip().upper()))

  words.sort(key=len)
  return words



def run():
  data = load_and_format_words()
  errors = 0
  running = True
  word = random.choice(data)
  underscore_word = ['_'] * len(word)

  clear_screen()
  render_start_screen()

  while running:
    clear_screen()
    print(assets.IMAGENES_AHORCADO[errors])
    print()

    for char in underscore_word:
      print(" "+char, end='')

    if errors == 7:
      print("\n\n")
      print("PERDISTE!")
      print("La palaba era "+ ''.join(word))
      input("Presiona Enter para salir")
      clear_screen()
      running = False

    if not '_' in underscore_word:
      print("\n\n")
      print("GANASTE!")
      print("La palaba es "+ ''.join(word))
      input("Presiona Enter para salir")
      clear_screen()
      running = False


    if running:
      print("\n\n")
      letter = input('Ingresa una letra: ').strip().upper()

      if letter in word:
        for indx in range(0, len(word)):
          if letter == word[indx]:
            underscore_word[indx] = word[indx]

      else:
        errors = errors + 1





if __name__ == "__main__":
  run()