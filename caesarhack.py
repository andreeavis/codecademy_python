message = 'GUVF VF ZL FRPERG ZRFFNTR.'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# loop through every key possible:
for key in range(len(LETTERS)):
	
	# it is important to set translated to blank string so that the 
	# previous iteration's value for translated is cleared
	translated = ''

	# run the encryption / decryption code on each symbol in the message:
	for symbol in message:
		if symbol in LETTERS:
			num = LETTERS.find(symbol) # get the number of the symbol
			num = num - key

			# handle the wrap-around if num is 26 or larger or less than 0
			if num < 0: 
				num = num + len(LETTERS)

			# add numbers' symbol at the end of 'translated'
			translated = translated + LETTERS[num]

		else:
			# just add the symbol without encrypting / decrypting
			translated += symbol

	print(translated)