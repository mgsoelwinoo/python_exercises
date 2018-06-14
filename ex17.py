from sys import argv
from os.pash import exists
script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")
in_file = open(from_file)
indata = in_file.read()
print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exits? {exits(to_file)}")
print()
