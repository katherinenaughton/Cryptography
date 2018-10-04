"""
cryptography.py
Author: Katie Naughton
Credit: I worked alone. 

Assignment:
Write and submit a program that encrypts and decrypts user data.
See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

func=input("Enter e to encrypt, d to decrypt, or q to quit: ")
while func !='q':
    print(c)
    if c=='q':
        print('Goodbye!')
    elif c== 'e' or c=='d':
        m=input("Message: ")
        k=input("Key: ")
        print(m)
        print(k)
        
    else: 
        print("Did not understand command, try again.")
