from sys import argv
#declare two arguments for the argv function
script, filename = argv 
#call the open function on the filename variable and assign it to variable txt
txt = open(filename)
#print a string with format %r
print "Here's your file %r:" % filename
print txt.read()
#print string
print "Type the filename again:"
file_again = raw_input("> ")
#call the open function on the file_again variable and assign it to variable txt_again
txt_again = open(file_again)
#call the read function on the txt_again variable and print it
print txt_again.read()

#Extra drill: call the close function on the txt and txt_again variables
txt.close()
txt_again.close()
