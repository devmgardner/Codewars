alphabet = input('enter the alphabet> ')
finalalphtable = [alphabet[i:] + alphabet[:i] for i in range(len(alphabet))]
#for table in range(len(alphabet)):
#    finalalphtable.append(alphabet[table:] + alphabet[:table])
print(finalalphtable)