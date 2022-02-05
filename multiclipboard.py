import sys
import clipboard
import json

# data = clipboard.paste()
# print(data)

#print(sys.argv)   # Adds arguments to the python file when running it

if len(sys.argv) == 2:
    command = sys.argv[1]
    print(command)