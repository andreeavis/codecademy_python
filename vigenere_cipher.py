# import pyperclip

# LETTERS = 'abcdefghijklmnopqrstuvwxyz'

# def main():
# 	myMessage = 'dfc jhjj ifyh yf hrfgiv xulk? vmph bfzo! qtl eeh gvkszlfl yyvww kpi hpuvzx dl tzcgrywrxll!'
# 	myKey = 'friends'
# 	myMode = 'decrypt' # set to encrypt or decrypt

# 	if myMode == 'encrypt':
# 		translated = encryptMessage(myKey, myMessage)
# 	elif myMode == 'decrypt':
# 		translated = decryptMessage(myKey, myMessage) 

# 	# print('%sed message:'%(myMode.title()))
# 	# print(translated)
# 	# pyperclip.copy(translated)
# 	# print()
# 	# print("The message has been copied to the clipboard.")

# def encryptMessage(key, message):
# 	return translateMessage(key, message, 'encrypt')

# def decryptMessage(key, message):
# 	return translateMessage(key, message, 'decrypt')
# 	# print()

# def translateMessage(key, message, mode):
# 	translated = [] #stores the encrypted / decrypted message string 

# 	keyIndex = 0
# 	key = key.lower()

# 	for symbol in message: # loop through each character in message
# 		num = LETTERS.find(symbol.lower())
# 		if num != -1: # -1 means symbol.lower() was not found in LETTERS
# 			if mode == 'encrypt':
# 				num += LETTERS.find(key[keyIndex]) # add if encrypting
# 			elif mode == 'decrypt':
# 				num -= LETTERS.find(key[keyIndex]) # substract if decrypting

# 			num %= len(LETTERS) # handle potential wrap-around

# 			# add the encrypted/decrypted symbol to the end of translated.
# 			if symbol.isupper():
# 				translated.append(LETTERS[num])
# 			elif symbol.islower():
# 				translated.append(LETTERS[num].lower())

# 			keyIndex += 1 # move to the next leter in the key
# 			if keyIndex == len(key):
# 				keyIndex = 0
# 		else:
# 			# the symbol was not in LETTERS, so add it to translated as is.
# 			translated.append(symbol)
# 	return ''.join(translated)
# 	print(''.join(translated))


# if __name__=='__main__':
# 	main()




def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext

ciphertext = 'dfc jhjj ifyh yf hrfgiv xulk? vmph bfzo! qtl eeh gvkszlfl yyvww kpi hpuvzx dl tzcgrywrxll!'
key = 'friends'
print(decrypt(ciphertext, key))















