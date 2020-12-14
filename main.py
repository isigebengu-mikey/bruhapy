import bruhapy

choice = input("""
Which bruhapy endpoint would you like to use?
1. Autotranslate
2. Cleverbot
3. Joke
4. TTS
5. Spongebob TTS
> """)

choices = ['1','2','3','4','5']

if choice not in choices:
  print("You made an invalid option!")

elif choice == '1':
  trt = input("Enter the text you'd like to translate: ")
  tr = bruhapy.translate(trt)
  print(tr.tr)
  print(f"Translated from {tr.lang}")

elif choice == '2':
  n = ['cancel','end','stop','exit']
  while True:
    cbt = input("> ")
    if cbt in n:
      print("Goodbye!")
      break
    else:
      cb = bruhapy.cb(cbt)
      print(cb.res)

elif choice == '3':
  joke = bruhapy.joke()
  print(f"Your joke: {joke}")

elif choice == '4':
  text = input("What text would you like Spongebob to say? ")
  spongeurl = bruhapy.tts(text)
  print(spongeurl)

elif choice == '5':
  text = input("What text would you like to input? \n")
  spongeurl = bruhapy.sponge(text)
  print(spongeurl)
