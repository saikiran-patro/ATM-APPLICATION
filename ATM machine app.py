userpin = {"user1":1234, "user2":2345, "user3": 3456, "user4": 4567, "user5": 5678}
userbal = {"user1":50000, "user2":20000, "user3": 5000, "user4": 10000, "user5": 8000}

# Cash deposition of ATM
print("----------Cashier cash deposition----------\n")
amt2000 = int(input("Enter number of 2000 rupee notes to be filled: "))
amt500 = int(input("Enter number of 500 rupee notes to be filled: "))
amt100 = int(input("Enter number of 100 rupee notes to be filled: "))
amttotal = amt2000*2000 + amt500*500 + amt100*100
print("Total amount in ATM is Rs. {0}\n".format(amttotal))

# Start ATM code here
print("----------WELCOME TO BANK OF Eduvance----------\n")
def compute(u1,up,amt2000,amt500,amt100):
        print("1.WITHDRAW")
        print("2.PIN CHANGE")
        print("3.BALANCE CHECK")
        c=0
        O1=int(input("choose any one"))
        if O1==1:
            while(c==0):
                u2000=int(input("enter the number of note for 2000"))
                u500=int(input("enter the number of note for 500"))
                u100=int(input("enter the number of note for 100"))
                ut=u2000*2000+u500*500+u100*100
                if ut<=amttotal:
                    
                    if ut<userbal[u1]:
                        c=1
                    else:
                        print("insufficient balance,Re-enter")
                else:
                    print("insufficient ATM balance,Re-enter")
            userbal[u1]=userbal[u1]-ut
            
            amt2000=amt2000-u2000
            amt500=amt500-u500
            amt100=amt100-u100
        if O1==2:
            up=int(input("enter the new pin"))
            up=int(input("Re-enter the new pin"))
            userpin[u1]=up
        if O1==3:
            print("{0}:{1}".format(u1,userbal[u1]))
print("----user id available---------")
print("1. user1")
print("2. user2")
print("3. user3")
print("4. user4")
print("5. user5")

while True:
        
     
    u1=input("enter a name")
    if u1 in userpin:
        up=int(input("enter 4 digit PIN"))
        if userpin[u1]==up:
            compute(u1,up,amt2000,amt500,amt100)
        else:
            for i in range(2):
                up=int(input("Re-enter correct 4 digit PIN"))
                if userpin[u1]==up:
                    compute(u1,up)
                    break
    else:
        u1=input("Re-enter correct  name")
        if u1 in userpin:
            up=int(input("enter 4 digit PIN"))
            if userpin[u1]==up:
                compute(u1,up,amt2000,amt500,amt100)
            else:
                for i in range(2):
                    up=int(input("Re-enter correct 4 digit PIN"))
                    if userpin[u1]==up:
                        compute(u1,up)
                        break
else:
    for i,j in usebal.items():
        print(i,j)
