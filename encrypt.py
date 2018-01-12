alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = input('What is the encryption key?')
newMessage = ''
message = input('Please enter a message: ')
for character in message:
	if character in alphabet:
		position = alphabet.find(character)
		new_position = (position + int(key)) % 26
		new_chracter = alphabet[new_position]
		newMessage += new_chracter
	else: 
		newMessage +=character

		
print('Your encrypted message is ' , newMessage)
