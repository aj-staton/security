'''
Written by Austin Staton
This will carve an image from a file that is in the same directory as this python script. 
-To specify the file, give it as the first command line argument after the
 execution argument
'''

import os
import sys
import re
import commands

jpg_begin = "fd8ffe0"
jpg_end = "ffd9"

# Get the file name
filename = sys.argv[1]
print("Finding the JPG in the file " + filename + ".....\n")

# Get a hex dump of file and put it into a string
hexdump = commands.getoutput("xxd -plain " + filename)
dump_file = hexdump.replace('\n', '')
print(hexdump)

# Search for Magic Numbers
if (jpg_begin in dump_file and jpg_end in dump_file):
    dump_file.replace(jpg_begin, " " + jpg_begin)
    dump_file.replace(jpg_end, jpg_end + " ")
    split = dump_file.split()
    # for i in split:
       # if (jpg_begin in i and jpg_end in i):
        #    print(i)
"""


# Copy that new chunk of data to another file (as a jpg)
#with open("image.jpg", "w+") as f:
    #f.write(jpg_full_file)
    #%f.close()


#read = open(sys.argv[1], 'rb')
