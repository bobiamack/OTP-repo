from ast import arg
import random
import sys
import getopt

# generate one-time pad that uses random, always longer than messsage itself
def generatePad(message):
    # initalize pad list
    pad = []
    # create a list with a length of the message plus one (so that it will always be longer than the message)
    # that is made up of random numbers in the range 65 <= x <= 97 (uppercase letters) 
    pad_nums = random.sample(range(65,90), len(message) + 1)

    # change numbers to letters
    for num in pad_nums:
        num = chr(num)
        pad.append(num)

    return len(pad)
    #print("Here's your one-time pad:","".join(pad))

# encrypts message using one-time pad
def encrypt(pad,message):
    # get message and pad from user input
    #message = input("Please enter message you would like to encrypt: ")
    #pad = input("Please enter pad you would like to use: ")
    # initialize lists of numbers
    pad_nums = []
    message_nums = []
    encryption_nums = []
    encryption = []
    
    # change pad letters into numbers
    # append numbers to pad list
    for character in pad:
        pad_num = ord(character)
        pad_nums.append(pad_num)

    # change message letters into numbers
    # append numbers to message list
    for character in message:
        if character.isalnum():
            message_num = ord(character)
            message_nums.append(message_num)
        else:
            message_nums.append(character)

    # for loop to add pad nums to message nums (encrypting the message)
    # add each sum to encryption nums list
    counter = 0 # counter to parse through pad nums list
    for messNum in message_nums:
        if type(messNum) == int:
            if (messNum >= 97) and (messNum <= 122): # lowercase
                shift = (((messNum + pad_nums[counter]) - 162) % 26) + 97
                #print(shift)
                encryption_nums.append(shift)
            elif (messNum >= 65) and (messNum <= 90): # uppercase
                shift = (((messNum + pad_nums[counter]) - 130) % 26) + 65
                #print(shift)
                encryption_nums.append(shift)
            counter += 1
        else:
            encryption_nums.append(messNum)

    # change encryption nums to letters and appends to encryption list
    for character in encryption_nums:
        if type(character) == int:
            encryption_num = chr(character)
            encryption.append(encryption_num)
        else:
            encryption.append(character)

    #print("pad nums:", pad_nums)
    #print("message nums:", message_nums)
    #print("encryption nums:",encryption_nums)
    return "".join(encryption)
    #print("Encrypted message: ", "".join(encryption))
    

def decipher(pad,message):
    # get message and pad from user input
    #message = input("Please enter message you would like to decipher: ")
    #pad = input("Please enter pad: ")

    # initialize lists of numbers
    pad_nums = []
    message_nums = []
    decipher_nums = []
    decrypted = []
    
    # change pad letters into numbers
    # append numbers to pad list
    for character in pad:
        pad_num = ord(character)
        pad_nums.append(pad_num)

    # change message letters into numbers
    # append numbers to message list
    for character in message:
        if character.isalnum():
            message_num = ord(character)
            message_nums.append(message_num)
        else:
            message_nums.append(character)


    # for loop to subtract pad nums from message nums (decrypting the message)
    # add each difference to decipher nums list
    counter = 0 # counter to parse through pad nums list
    for messNum in message_nums:
        if type(messNum) == int:
            if (messNum >= 97) and (messNum <= 122): # lowercase
                shift = (((messNum - pad_nums[counter]) - 162) % 26) + 97
                #print(shift)
                decipher_nums.append(shift)
            elif (messNum >= 65) and (messNum <= 90): # uppercase
                shift = (((messNum - pad_nums[counter]) - 130) % 26) + 65
                #print(shift)
                decipher_nums.append(shift)
            counter += 1
        else:
            decipher_nums.append(messNum)

    # change decryption nums to letters and appends to decryption list
    for character in decipher_nums:
        if type(character) == int:
            encryption_num = chr(character)
            decrypted.append(encryption_num)
        else:
            decrypted.append(character)

    return "".join(decrypted)
    #print("Decrypted message: ", "".join(decrypted))

#decipher(pad_text, encrypted_text)
encrypt("QWERTYUIOP", "Rally Day!")
decipher("QWERTYUIOP", "Hwpcr Bug!")
#generatePad("hello!")

def main(argv):
    padinfile = ''
    unencryptedfile = ''
    encryptedfile = ''

    try:
        opts, args = getopt.getopt(argv,"mp:ed:w")
    except getopt.GetoptError:
        print('Please check the manual with m to see valid commands.')
        sys.exit(2)
    if not opts or len(opts) > 2:
        print('Too many arguments. Please check the manual with -m to see valid commands')
        sys.exit(2)
    for opt, args in opts:
        if opt == '-m':
            print('Manual for one-time pad cipher\n-p <padfile>: Generate a 10,000 character one-time pad and store it in <padfile>.\n-e <inputfile> -w <padfile>: Encrypt the <inputfile> using one-ti9me pad in <padfile>. \n-d <inputfile> -w <padfile>: Decrypt the <inputfile> using one-time pad in <padfile>.')
            sys.exit()
        elif opt == "-p":
            generatePad()
        elif opt == "-e":
            unencryptedfile = arg
        elif opt == "-d":
            encryptedfile = arg
        elif opt == "-w":
            padinfile = arg
    
    if unencryptedfile and padinfile:
        with open(unencryptedfile) as file:
            message = file.read()
        with open("encrypted-message.txt", "w") as file:
            file.write(encrypt(message,padinfile))
        print("The message in", unencryptedfile, "has been encryprted and saved to encrypted-message.txt")
    elif encryptedfile and padinfile:
        with open(encryptedfile) as file:
            message = file.read()
        with open("decrypted-message.txt", "w") as file:
            file.write(decipher(message,padinfile))
        print("The message in", encryptedfile, "has been decrypted and saved to decrypted-message.txt")
    else:
        print("Incorrect number of arguments. please check the manual with -m to see calid commands.")

if __name__ == "__main__":
    main(sys.argv[1:])
        



