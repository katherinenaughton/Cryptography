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
        
        #number associations for message
        m1=[]
        for i in m: 
            num=associations.find(i)
            m1.append(num)
        print(m1)
        
        #number associations for key
        k1=[]
        for j in k:
            num=associations.find(j)
            k1.append(num)
        print(k1)
        
        #lengths of message and key
        lenm=len(m)
        print(lenm)
        lenk=len(k)
        print(lenk)
        lena=len(associations)
        print(lena)
    
        #remainder
        rem=(lenm%lenk)
        print(rem)
        
        #divisor
        div=int(lenm/lenk)
        print(div)
        
        #when remainder is 0
        k2=k1*div
        print(k2)
        
        #when remainder isn't 0
        k3=[]
        for i in k1[0:(rem)]:
            k3.append(i)
        print(k3)
                
        k4=k2 + k3 
        
        #encrypt
        if f=='e':
            ezip=list(zip(m1, k4))
            print(ezip)
            eadd=[]
            for c in ezip:
                num2=(c[0]+c[1])
                if num2>84:
                    num3=num2-85
                    eadd.append(num3)
                else: 
                    eadd.append(num2)
            print(eadd)
                
            efinal=[]
            for b in eadd:
                eletter=associations[b]
                efinal.append(eletter)
            print(efinal)
            output=""
            for i in efinal:
                output += i+""
            print(output)
        
        #decrypt
        if f=='d':
            dzip=list(zip(m1, k4))
            print(dzip)
            dadd=[]
            for c in dzip:
                dnum2=(c[0]-c[1])
                if dnum2<0:
                    dnum3=dnum2+85
                    dadd.append(dnum3)
                
                else:
                    dadd.append(dnum2)
            print(dadd)
                
            dfinal=[]
            for b in dadd:
                dletter=associations[b]
                dfinal.append(dletter)
            print(dfinal)
            output=""
            for i in dfinal:
                output += i+""
            print(output)
    
    elif f!='e' and f!='d' and f!='q':
        print("Did not understand command, try again.")
print('Goodbye!')

