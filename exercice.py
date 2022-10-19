#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	name = name.split("-")[0]
	name = name[0].upper() + name[1:].lower()
	return f'Bonjour, {name}'

def get_random_sentence(animals, adjectives, fruits):
	return f'Aujourd’hui, j’ai vu un {random.choice(animals)} s’emparer d’un panier {random.choice(adjectives)} plein de {random.choice(fruits)}.'


def encrypt(text, shift):
	letters = ""
	for i in text:
		if i.isalpha() == True:
			i = i.upper()
			if (ord(i) + shift) > 90:
				letters += chr(ord(i) + shift - 26)
			else:
				letters += chr(ord(i) + shift)
		else:
			letters += i

	return letters

def decrypt(encrypted_text, shift):
	lettres = ""
	for i in encrypted_text:
		if i.isalpha() == True:
			i = i.upper()
			if (ord(i) - shift) < 65:
				lettres += chr(ord(i) - shift + 26)
			else:
				lettres += chr(ord(i) - shift)
		else:
			lettres += i

	return lettres
if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
