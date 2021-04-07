from caesar_logo import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = alphabet + alphabet

def caesar(plain_text, shift_amount):
    if shift_amount > 25:
        shift_amount = (shift_amount % 25)
    elif direction == 'encode':
        crypto_word = []
        for i in range(0, len(plain_text)):
            if plain_text[i] in alphabet:
                crypto_word += alphabet[((alphabet.index(plain_text[i])) + shift_amount)]
            else:
                crypto_word += plain_text[i]
        print(f"The encoded text is {''.join(crypto_word)}")
    elif direction == 'decode':
        decrypt_word = []
        for a in range(0, len(plain_text)):
            if plain_text[a] in alphabet:
                decrypt_word += alphabet[((alphabet.index(plain_text[a])) - shift_amount)]
            else:
                decrypt_word += plain_text[a]
        print(f"Your encrypted message is {''.join(decrypt_word)}")
    elif direction != 'encode' or direction != 'decode':
      print("You'll be write encode or decode, please try again")

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    caesar(plain_text = text, shift_amount=shift) 
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower()
    if restart == "no":
        should_end = True
        print("Goodbye")