
shift = 5


# simple ceasar cypher encryption implementation

def encrypt(message):
    result = ''
    for i in message:
        result += str(chr( ord(i) + shift)) # shifts the message by the specified amount
    return result




def decrypt(message):
    result = ''
    for i in message:
        result += str(chr( ord(i) - shift))
    return result



def main():
    message = input('enter a message to encrypt: ')

    encrpytedmsg = encrypt(message)
    decryptedmsg = decrypt(encrpytedmsg)
    print("encrypted message: ", encrpytedmsg, '\ndecrypted message: ', decryptedmsg, '\n')



main()