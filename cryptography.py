"""
cryptography.py
Author: Katie Naughton
Credit: I worked alone. 

Assignment:
Write and submit a program that encrypts and decrypts user data.
See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

f=''
while f!='q':
    f=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if f== 'e' or f=='d':
        m=input("Message: ")
        k=input("Key: ")
        print(m)
        print(k)
        m1=[]
        for i in m: 
            num=associations.find(i)
            m1.append(num)
        print(m1)
        k1=[]
        for j in k:
            num=associations.find(j)
            k1.append(num)
        print(k1)
    elif f!='e' and f!='d' and f!='q':
        print("Did not understand command, try again.")
print('Goodbye!')
