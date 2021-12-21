def machine():
    # creating key strings 
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    # generating values of string
    values = keys[-1] + keys[0:-1]
    # value is created by taking last key to first key
    
    # creating two dictionaries
    encryptDict = dict(zip(keys, values))
    decryptDict = dict(zip(values, keys))
    
    # user input 
    message = input("Enter your secret message: ")
    mode = input("Crypto Mode : Encode(E) OR Decode(D)")
    
    # encode and decode conditional statements
    if mode.upper() == 'E':
        newMessage = ''.join([encryptDict[letter]
                              for letter in message.lower()])
    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter]
                              for letter in message.lower()])
    else:
        print("Please try again, wrong choice entered")

    return newMessage.capitalize()

print(machine()) 