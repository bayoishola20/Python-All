f = open("lorem.txt", "r")
text = f.read()
print "Length of lorem text is: %d" % len(text)
print "FULL TEXT IS >>> %s" % text
print "LAST CHARACTER IS >>> %s" % text[-1]

every_word = text.split() # default splits when it sees a space character

for i in every_word:
    print i

lowercase = text.lower()

print lowercase

uppercase = text.upper()

print uppercase

print text.find("lorem")

print text.count("o")

# print text.replace("lorem", "bayo")