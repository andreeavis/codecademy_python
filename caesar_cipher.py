# MAX_KEY_SIZE = 26

# # def getMode():
# # 	while True:
# # 		print('Do you wish to encryipt or decrypt a message?')
# # 		mode = input().lower()
# # 		if mode in "encrypt e decrypt d".split(): # ['encrypt', 'e', 'decrypt', 'd']
# # 			return mode
# # 		else:
# # 			print('Enter either "encrypt" or "e" or "decrypt" or "d".')



# # def getMessage():
# # 	print('Enter your message: ')
# # 	return input()


# # def getKey():
# # 	key = 0 
# # 	while True:
# # 		print(f'Enter the key number (1 - {MAX_KEY_SIZE}): ')
# # 		key = int(input())
# # 		if (key >= 1 and key <= MAX_KEY_SIZE):
# # 			return key

# print('Enter your message to be decrypted here: ')
			
# message = input()
# key = 1 
# def getTranslatedMessage(message, key):
	
# 	translated = ''

# 	for symbol in message:
# 		if symbol.isalpha():
# 			num = ord(symbol)
# 			num + key

# 			if symbol.isupper():
# 				if num > ord('Z'):
# 					num -= 26
# 			elif symbol.islower():
# 				if num > ord('z'):
# 					num -= 26
# 				elif num < ord('a'):
# 					num += 26

# 			translated += chr(num)
# 		else:
# 			translated += symbol
# 	return translated


# print('Your translated text is: ')
# print(getTranslatedMessage(message, key))

import pyperclip

message = "This is my secret message!"
key = 1
mode = 'encrypt'

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

translated = ''

for symbol in message:
	if symbol in SYMBOLS:
		symbolIndex = SYMBOLS.find(symbol)

		if mode == 'encrypt':
			translatedIndex = symbolIndex + key
		elif mode == 'decrypt':
			translatedIndex = symbolIndex - key

		if translatedIndex >= len(SYMBOLS):
			translatedIndex = translatedIndex - len(SYMBOLS)
		elif translatedIndex < 0:
			translatedIndex = translatedIndex + len(SYMBOLS)

		translated = translated + SYMBOLS[translatedIndex]
	else:
		translated = translated + symbol


print(translated)
paperclip.copy(translated)

































