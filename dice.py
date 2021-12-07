import random


def ludo(x):
    c=random.randrange(1,6)
    while(x=="Y"):
        if(c==1):
            print("   ")
            print(" . ")
            print("   ")
            break

        elif(c==2):
            print(".    ")
            print("     ")
            print("    .")
            break

        elif(c==3):
            print(".   ")
            print(" .  ")
            print("   .")
            break

        elif(c==4):
            print(".   .")
            print("     ")
            print(".   .")
            break

        elif(c==5):
            print(".   .")
            print("  .  ")
            print(".   .")
            break

        elif(c==6):
            print(" ... ")
            print("     ")
            print(" ... ")
            
            break
        else:
            continue


x=input("Press Y to start game\n")
ludo(x)