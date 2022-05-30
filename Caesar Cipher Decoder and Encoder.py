#################################
######Caesar Cipher #############
#################################



def main():
    message = input('Please enter a message to encrypt: ')
    encryption_key = int(input('Please enter a encrypt Key:'))

    def encrypt(char, encryption_key):
        return chr(ord('A') + (ord(char) - ord('A') + encryption_key) % 26)

    ##############################################################
    #######################     Encryption         ###############
    ##############################################################

    def encrypt_message(message, encryption_key):
        message = message.upper()
        cipher = " "
        for c in message:
            if c in "., ":
                cipher = cipher + c
            else:
                cipher = cipher + encrypt(c, encryption_key)
        print(f'Encoding:{cipher}')
        print('************************')

    encrypt_message(message, encryption_key)

    ##############################################################
    #######################     Decryption          ##############
    ##############################################################

    def decryption(char, key):
        return chr(ord('A') + (ord(char) - ord('A') + 26 - key) % 26)

    def decrypt_messsage(cipher, key):
        decrip_message = " "
        for c in cipher:
            if c in '.,':
                decrip_message = decrip_message + c
            else:
                decrip_message = decrip_message + decryption(c, key)
        print(f'Decoding: {message}')

    decrypt_messsage(message, encryption_key)

    try_again = input("Do you want to try again y/n: ").lower()
    if try_again == 'y':
        main()
    else:
        exit()


main()
