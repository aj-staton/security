'''
Written by Austin Staton

"jpeg_carve.py" will carve a JPEG image from a file. This is meant to be used as an introduction to the concept of File Carving for Data Recovery. 

To specify the file, give it as the first command line argument after the
execution argument.
'''
import os
import sys
import re
import commands
# JPG 
jpg_BOF = "fd8ffe0"
jpg_EOF = "ffd9"

# Get the file name from the command line input.
filename = sys.argv[1]
print("Finding the JPG in the file " + filename + ".....\n")

# Get a hex dump of the input file and put those bits into a string
hexdump = commands.getoutput("xxd -plain " + filename)
dump_file = hexdump.replace('\n', '')
# print(hexdump)

# Search for the '*.jpeg' file's "magic numbers" in the bit string. 
if (jpg_BOF in dump_file and jpg_EOF in dump_file):
    dump_file.replace(jpg_BOF, " " + jpg_BOF)
    dump_file.replace(jpg_EOF, jpg_EOF + " ")
    split = dump_file.split()
    #TODO:Place the found string into its own file.
'''
with open("image.jpg", "w+") as f:
    f.write(jpg_full_file)
    f.close()
read = open(sys.argv[1], 'rb')
'''
