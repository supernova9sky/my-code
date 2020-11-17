import time
import pyautogui
from colorama import *
init()
#Message
wiadomosc = input(Fore.BLUE + "Wiadomosc:")
#Resetting
Fore.RESET
#Amount
ilosc = int(input(Fore.LIGHTMAGENTA_EX + "Ile razy:"))
#Resetting
Fore.RESET
#Delay
czekaj = int(input(Fore.CYAN + "Liczba sekund przed startem:"))
#Resetting
Fore.RESET
#Printing Delay
print(Fore.RED + "Masz",czekaj," sec przed spamem",Fore.RESET)
#Making a delay
time.sleep(czekaj)
#Sending messages
for i in range(0,int(ilosc)):
    pyautogui.typewrite(wiadomosc + "\n")
    print(Back.LIGHTBLUE_EX, Fore.RED + "SPAM NR",i,"WYSLANY",Back.RESET,Fore.RESET)
    if i == ilosc:
        exit(0)
