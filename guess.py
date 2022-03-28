#!/usr/bin/python3

import sys

# Options
input_file = list()
rc_intensity = 0		# Random character intensity
rc_random_syms = False
rc_random_upper = False
word_rand = 1

# Parse command line arguments
if len(sys.argv) == 1:
	print("Warning: No input file. Genearting random character sequences.")
	rc_intensity = 3
	
skip_next = False
for i in range(1, len(sys.argv)):
	if skip_next:
		skip_next = False
		continue
	
	item = sys.argv[i]
	if item == "-rc-upper":
		rc_random_upper = True
	elif item == "-rc-syms":
		rc_random_syms = True
	elif item == "-rc-int":
		rc_intensity = int(sys.argv[i+1])
		skip_next = True
	elif item == "-rc-words":
		word_rand = int(sys.argv[i+1])
		skip_next = True
	else:
		if item[0] == '-':
			print("Error: Unknown command line option.")
		else:
			input_file.append(item)

# Symbol maps
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '~']
letters = "abcdefghijklmnopqrstuvwxyz"

if rc_random_upper:
	letters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if rc_random_syms:
	letters += "~`1234567890-=!@#$%^&*()_+|}{:<>?[]\;,./"

def generate_chars(writer, prefix, n):
	if n == 0:
		return
	for c in letters:
		current1 = prefix + c
		current2 = c + prefix
		
		writer.write(current1 + "\n")
		writer.write(current2 + "\n")
		
		generate_chars(writer, current1, n - 1)
		generate_chars(writer, current2, n - 1)

def generateSymbolVariants(writer, word2):
	for j in range(0, len(symbols)):
		word3 = ''.join(word2) + symbols[j]
		word4 = symbols[j] + ''.join(word2)
		
		writer.write(word3 + "\n")
		writer.write(word4 + "\n")
		generate_chars(writer, word3, word_rand)
		generate_chars(writer, word4, word_rand)
		
	for i in range(0, 10):
		word3 = ''.join(word2) + str(i)
		word4 = str(i) + ''.join(word2)
		
		writer.write(word3 + "\n")
		writer.write(word4 + "\n")
		
		generate_chars(writer, word3, word_rand)
		generate_chars(writer, word4, word_rand)
		
def generate_file(current):
	with open(current, "r") as reader:
		for word in reader:
			word = word.strip()
			#if word[0] == '#' and word[1] == '!':
			#	continue
			writer.write(word + "\n")
			generate_chars(writer, word, word_rand)
			
			word = word.lower()
			writer.write(word + "\n")
			generate_chars(writer, word, word_rand)
			
			# Now, generate variants of the words
			# All uppercase
			writer.write(word.upper() + "\n")
			generate_chars(writer, word.upper(), word_rand)
			
			# Variants with each character uppercase
			for i in range(0, len(word)):
				word2 = list(word)
				word2[i] = word[i].upper()
				writer.write(''.join(word2) + "\n")
				generate_chars(writer, ''.join(word2), word_rand)
				
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

#		
# Create a writer and start generating
#
writer = open("words_out.txt", "w")

if rc_intensity > 0:
	generate_chars(writer, "", rc_intensity)

if len(input_file) > 0:
	print("Generating based on following inputs:")
	for current in input_file:
		print(current)
		generate_file(current)
			
print("Done generating!")
