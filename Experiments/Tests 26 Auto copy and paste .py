import pyperclip as pc

text = input("Text: ")
pc.copy(text)
text2 = pc.paste()

print(text2)
