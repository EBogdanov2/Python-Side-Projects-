# This is a program that either changes a string of characters into a coded message consisting of numbers
# the other function of it is to receive a set of integers that is then converted into characters and thus
# decoding the original message

# This function takes the string and changes it into numbers
def wordarraytransform(newword):

    alphabet = {
        'a': 26,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25,
    }
    newword = list(newword.lower())
    wordinnumbers = []
    for i in range(0,len(newword)):
        wordinnumbers.append(alphabet.get(newword[i]))
    return (str(wordinnumbers)).strip('[]').replace(',','').replace('None','')

# This function changes the numbers as a string back into the original letters
def codetoword(secretmessage):

    numberalphabet = {
        '26': 'a',
        '1': 'b',
        '2': 'c',
        '3': 'd',
        '4': 'e',
        '5': 'f',
        '6': 'g',
        '7': 'h',
        '8': 'i',
        '9': 'j',
        '10': 'k',
        '11': 'l',
        '12': 'm',
        '13': 'n',
        '14': 'o',
        '15': 'p',
        '16': 'q',
        '17': 'r',
        '18': 's',
        '19': 't',
        '20': 'u',
        '21': 'v',
        '22': 'w',
        '23': 'x',
        '24': 'y',
        '25': 'z'
    }
    numberstoletters = []
    for i in range(0, len(secretmessage) -1):
        numberstoletters.append(numberalphabet.get(secretmessage[i]))
    return (str(numberstoletters)).strip('[]').replace(',','').replace('None','')

encodeordecode = input("Would you like to encode a message or decode one? ")
if encodeordecode.lower() == 'encode':
    newword = input('What is the message? ')
    if not newword: # makes sure that input is not empty
        print('please restart the process and enter a valid message')
    else:
        print('Your new message is: ' + wordarraytransform(newword))
elif encodeordecode.lower() == 'decode':
    secretmessage = input('Enter the message, with numbers seperated by whitespace(leave a space after final number): ')
    secretmessage = secretmessage.split(' ')
    if not secretmessage:
       print('please restart the process and enter a valid message')
    else:
       print('The message is: ' + codetoword(secretmessage))
else: # if there is no input or some input other than the two choices
    print("Please enter a valid option")

