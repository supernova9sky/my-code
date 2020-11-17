# importing
import time
from colorama import *
import random
#colorama init
init()
a = 1
finding = 0
# Checking if number is correct
finding = int(input("Number:"))
if finding == 0:
    finding = random.randint(0,99999999999999999)
    print("Setting to value:",finding )
'''
while True:
    finding = int(input("Number:"))
    if finding % 2 == 0:
        break
    print(Back.LIGHTYELLOW_EX,Fore.RED + "Not correct!",Back.RESET,Fore.RESET)
'''
#Inputing valiues
upperborder = int(input("Upper border:"))
upperborder = upperborder + 1
upperborderminus = upperborder - 1
if finding > upperborder:
    print(Fore.RED + "You woud not get your number because your border is lower that the number",Fore.RESET)
timetosleep = float(input("Time to sleep(Recomended 0.1)"))
# Math
for i in range(2, upperborder):
    time.sleep(timetosleep)
    a += 1
    print("Turn no:", i, "Value:", a)
    found = 0
    if a==finding:
        found = 1
        print(Back.GREEN,Fore.RED + "Number found on turn:",i,Back.RESET,Fore.RESET)
        time.sleep(86400)
    if i==upperborderminus and found==0:
        print(Back.LIGHTYELLOW_EX,Fore.RED + "Number not found",Back.RESET,Fore.RESET)
        break
