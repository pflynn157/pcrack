#!/usr/bin/python3

letters = "abcdefghijklmnopqrstuvwxyz"
letters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters += "~`1234567890-=!@#$%^&*()_+|}{:<>?[]\;,./"

def generate_chars(prefix, n):
	if n == 0:
		return
	for c in letters:
		current = prefix + c
		print(current)
		generate_chars(current, n - 1)
		
generate_chars("", 100)

#for c in letters:
#	print(c)
#	for c2 in letters:
#		print(c+c2)
#		for c3 in letters:
#			print(c+c2+c3)

