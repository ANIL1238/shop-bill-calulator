#import random
#random.randrange(10,20)
"""sum=0
input(print("NEME::"))
while(True):
    userinput=input(print("ENTER THE ITEM NAME"))
    if (userinput !='p'):
        print(f" THE TOTAL  SO FAR {sum}")
    else:
        sum=sum+int(userinput)
        print(f"the total bill is{sum} || TQ FOR COMING ")"""

import datetime
print("--------------------------------------------")
print(" ....🛒AKS SUPER 🛍️MARKET....")
x=datetime.datetime.now()
print(x.month,"/",x.day,"/", x.year )

#items={"kola": 20,
      # "apple": 40,
      # "orange": 30,
      # "cherry":120}
total=0
a=input(" name:")
int(input(" ph number:"))
#for i in items:


while True:
        order = input("enter the item name")
        print("----------------------------")
        amount=int(input("amount:"))
        print("----------------------------")
        if order == "end":
            if amount==0:

             print(f"the total is {order}", total)

             print(f"hey {a}  :) vist again")
             print("----------------------")
            break
        else:
            quy = int(input("enter the quenty:"))
            total = total + amount * quy
            #print(f"the total is{total}")
            #print(f"the total is {order}", total)

