def encrypt_pliantext(plian_text,shift):
    cipher_text=''.join([chr(ord(char)+shift) for char in plian_text])
    return cipher_text
def decrypt_ciphertext(cipher_text,shift):
    plianText=''.join([chr(ord(char) +shift) for char in cipher_text])
    return cipher_text


print("Well Come To Ceaser cipher!!")

option = 'YES'
while option != "NO":
    print("""
    Enter your choice!

    encryption ----> to encrypt Message
    decryption ----> To decrypt Message
    """)
    script_type = input("Type here!")
    if script_type != "encryption" and script_type != "decryption":
        print(" Please type your correctly!!")


    elif script_type == "encryption":
        text = input("Type the message here:").lower()
        key = int(input("Enter the shift number:"))
        encrypted_text = encrypt_pliantext( text,key)
        print(f"The encrypted form of your messeage is:\n {encrypted_text}")
        option = input("Type 'Yes' continue! or 'NO' to logout!").upper()
        if option == 'no':
            print("Good Bye!!")
    else:
        text = input("Type the message here:").lower()
        key = int(input("Enter the shift number:"))
        decrypted_text = decrypt_ciphertext(text,key)
        print(f"The decrypted form of your message is:\n {decrypted_text}")
        option = input("Type 'YES' to Continue! or 'NO' to Logout!").upper()
        if option == 'no':
            print("Good Bye!!")