from sys import argv
script, filename= argv
txt= open(filename)
print(f"Here's your file {filename}:")
print(txt.read())
print("Type the folename again:")
file_again = input("> ")
