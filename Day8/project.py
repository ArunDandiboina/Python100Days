li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(word, shift):
    for l in word:
        if not (l.isalpha() or l == '_'):
            print("Invalid character found. Only letters and underscores are allowed.")
            break
        # if underscore print space
        elif '_' == l:
            print(' ', end='')
        else:
            x = li.index(l)
            x = (x + shift) % 26
            print(li[x], end='')

def decrypt(word, shift):
    for l in word:
        if not (l.isalpha() or l == '_'):
            print("Invalid character found. Only letters and underscores are allowed.")
            break
        if '_' == l:
            print(' ', end='')
        else:
            x = li.index(l)
            x = (x - shift) % 26
            print(li[x], end='')

def ceaser_cipher():
    while True:
        choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").strip().lower()
        if choice not in ['encode', 'decode']:
            print("Invalid choice. Please type 'encode' or 'decode'.")
            continue
        message = input("Type your message: \n").strip().lower()
        shift = int(input("Type the shift number: \n"))

        if choice == 'encode':
            print("Here's the encoded message: ", end='')
            encrypt(message, shift)
        elif choice == 'decode':
            print("Here's the decoded message: ", end='')
            decrypt(message, shift)
        repeat = input("\nType 'yes' if you want to go again. Otherwise type 'no': ").strip().lower()
        if repeat == 'no':
            print("Goodbye!")
            break
        elif repeat == 'yes':
            continue

ceaser_cipher()


