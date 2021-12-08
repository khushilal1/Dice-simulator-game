import random

x="yes"
while(x=="yes" or x=="y"):
    c=random.randint(1,6)
    if(c==1):
        print("   ")
        print(" * ")
        print("   ")


    if(c==2):
        print("*  ")
        print("   ")
        print("  *")


    if(c==3):
        print("*  ")
        print(" * ")
        print("  *")


    if(c==4):
        print("* *")
        print("   ")
        print("* *")


    if(c==5):
        print("*  *")
        print("  * ")
        print("*  *")


    if(c==6):
        print(" * * * ")
        print("       ")
        print(" * * * ")
    
    x=input("Do you want to play again? yes/y\n")
    if(x=="no" or x=="n"):
        print("Thanks for playing games")
        break