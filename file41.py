file = open('finally.txt', 'w')
try:
   file.write("Hello World")
   print("Writing to file.")
except IOError:
   print("Could not write to file.")
else:
   print("Write successful.")
finally:
   file.close()
   print("File closed.")
