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
    
        #remainder
        rem=(lenm%lenk)
        print(rem)
        
        #divisor
        div=int(lenm/lenk)
        print(div)
        
        #difference
        diff=lenk-rem
        print(diff)
        
        #when remainder is 0
        if rem==0:
            k2=k1*div
        print(k2)
        
        #when remainder isn't 0
         if rem!=0:
            k2=k3
            k3=[]
            for i in range(rem):
                for j in [m1:-1]:
                    k3.append(m1)
    
            print(k3)
                
        
            k2=k1*div +  
        
        
        
        #encrypt
        ezip=list(zip(m1, k2))
        print(ezip)
        eadd=[]
        for c in ezip:
            num2=(c[0]+c[1])
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
        
        
            
            
            
    elif f!='e' and f!='d' and f!='q':
        print("Did not understand command, try again.")
print('Goodbye!')
