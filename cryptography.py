"""
cryptography.py
Author: Katie Naughton
Credit: I worked alone. 

Assignment:
Write and submit a program that encrypts and decrypts user data.
See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

f=input("Enter e to encrypt, d to decrypt, or q to quit: ")
while f !='q':
    if c== 'e' or c=='d':
        m=input("Message: ")
        k=input("Key: ")
        print(m)
        print(k)
    else: print("Did not understand command, try again.")
if f=='q':
    print('Goodbye!')
