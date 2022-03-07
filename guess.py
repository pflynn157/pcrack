#!/usr/bin/python3

writer = open("words_out.txt", "w")

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '~']

def generateSymbolVariants(writer, word2):
	for j in range(0, len(symbols)):
		word3 = ''.join(word2) + symbols[j]
		word4 = symbols[j] + ''.join(word2)
		
		writer.write(word3 + "\n")
		writer.write(word4 + "\n")
		
	for i in range(0, 10):
		word3 = ''.join(word2) + str(i)
		word4 = str(i) + ''.join(word2)
		
		writer.write(word3 + "\n")
		writer.write(word4 + "\n")

with open("words.txt", "r") as reader:
	for word in reader:
		word = word.strip()
		#if word[0] == '#' and word[1] == '!':
		#	continue
		writer.write(word + "\n")
		
		word = word.lower()
		writer.write(word + "\n")
		
		# Now, generate variants of the words
		# All uppercase
		writer.write(word.upper() + "\n")
		
		# Variants with each character uppercase
		for i in range(0, len(word)):
			word2 = list(word)
			word2[i] = word[i].upper()
			writer.write(''.join(word2) + "\n")
			
			generateSymbolVariants(writer, word2)
			
			for i in range(0, len(word2)):
				if word2[i] == 'A' or word2[i] == 'a':
					word3 = word2
					word3[i] = '@'
					writer.write(''.join(word3) + "\n")
					generateSymbolVariants(writer, word3)
				elif word2[i] == 'o' or word2[i] == 'O':
					word3 = word2
					word3[i] = '0'
					writer.write(''.join(word3) + "\n")
					generateSymbolVariants(writer, word3)
			
print("Done generating!")
