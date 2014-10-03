# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

# every possible symbol that can be encrypted
LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

MAX_KEY_SIZE = len(LETTERS)
# the string to be encrypted/decrypted
message = 'This is my secret message.'

def getMessage():
    print('Enter your message:')
    return input()

# the encryption/decryption key
def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

# tells the program to encrypt or decrypt
mode = 'encrypt' # set to 'encrypt' or 'decrypt'



# stores the encrypted/decrypted form of the message
translated = ''

# capitalize the string in message
#message = message.upper()

def getTranslatedMessage(message, key):
    # run the encryption/decryption code on each symbol in the message string
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted (or decrypted) number for this symbol
            num = LETTERS.find(symbol) # get the number of the symbol
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key

            # handle the wrap-around if num is larger than the length of
            # LETTERS or less than 0
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            # add encrypted/decrypted number's symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol
    return translated

message = getMessage()
key = getKey()

print('Your translated text is:')
print(getTranslatedMessage(message, key))
