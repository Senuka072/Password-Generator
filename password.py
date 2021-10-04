import random
import time
import webbrowser                                                              
import colorama
import os
from colorama import Fore
colorama.init(autoreset= True)

os.system("clear")

symbols = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

logo = """
    d8888b.  .d8b.  .d8888. .d8888. db   d8b   db  .d88b.  d8888b. d8888b.
    88  `8D d8' `8b 88'  YP 88'  YP 88   I8I   88 .8P  Y8. 88  `8D 88  `8D
    88oodD' 88ooo88 `8bo.   `8bo.   88   I8I   88 88    88 88oobY' 88   88
    88~~~   88~~~88   `Y8b.   `Y8b. Y8   I8I   88 88    88 88`8b   88   88
    88      88   88 db   8D db   8D `8b d8'8b d8' `8b  d8' 88 `88. 88  .8D
    88      YP   YP `8888Y' `8888Y'  `8b8' `8d8'   `Y88P'  88   YD Y8888D'

"""

logo2= """

   d888b  d88888b d8b   db d88888b d8888b.  .d8b.  d888888b  .d88b.  d8888b.
  88' Y8b 88'     888o  88 88'     88  `8D d8' `8b `~~88~~' .8P  Y8. 88  `8D
  88      88ooooo 88V8o 88 88ooooo 88oobY' 88ooo88    88    88    88 88oobY'
  88  ooo 88~~~~~ 88 V8o88 88~~~~~ 88`8b   88~~~88    88    88    88 88`8b
  88. ~8~ 88.     88  V888 88.     88 `88. 88   88    88    `8b  d8' 88 `88.
   Y888P  Y88888P VP   V8P Y88888P 88   YD YP   YP    YP     `Y88P'  88   YD


"""


time.sleep(1)
print(Fore.MAGENTA + logo)
time.sleep(1)
print(Fore.GREEN + logo2)
time.sleep(1)

print()
print()

time.sleep(1)
print(Fore.RED + "             [~]" + Fore.BLUE + "This Tool Can Be Generate A PowerFull Password")
time.sleep(1)
print(Fore.RED + "\t               [~]" + Fore.BLUE + " Made By Senuka Thisath")

print()
print()

time.sleep(1)
print(Fore.RED + "\t                [1]" + Fore.BLUE + " Get A Password")
time.sleep(1)
print(Fore.RED + "\t                [2]" + Fore.BLUE + " Update Tool (This Will Enable In Next Version)")
time.sleep(1)
print(Fore.RED + "\t                [3]" + Fore.BLUE + " Exit")
time.sleep(1)

print()
print()

def passwordGen():
    time.sleep(1)                                                                   
    print(Fore.RED + "Please Answer The Questions Below. This Will helpful To Generate A PowerFull Password")
    time.sleep(1)
    print()
    name = str(input(Fore.BLUE + "[-] What is your name? :: " + Fore.RED))
    print()
    age = str(input(Fore.BLUE + "[-] How old are you? :: " + Fore.RED))
    print()
    school = str(input(Fore.BLUE + "[-] Which school do you go? :: " + Fore.RED))
    print()
    favourite = str(input(Fore.BLUE + "[-] What is your favourite subject? :: " + Fore.RED))
    print()
    passlegnth = int(input(Fore.BLUE + "[-] How lenght of password do you need (Ex :: 5, 10, 20): " + Fore.RED))
    all = name.upper() + name.lower() + age + school.lower() + school.upper() + favourite.lower() + favourite.upper() + symbols
    password = "".join(random.sample(all, passlegnth))
    time.sleep(1)
    print()
    print(Fore.RED + "Password Generated")
    time.sleep(1)
    print()
    print(Fore.MAGENTA + "Your Password Is :: " + Fore.RED + password)
    
    next = input(Fore.RED + "Do You Need To Generate A Password Again? (Yes/No) :: ")
    if next == "yes" or "Yes":
        os.system("python password.py")
    if next == "no" or "No":
        exit()

def updatetool():
    print(Fore.MAGENTA + """db    db d8888b. d8888b.  .d8b.  d888888b d888888b d8b   db d888b8 
88    88 88  `8D 88  `8D d8' `8b `~~88~~'   `88'   888o  88 88' Y8b
88    88 88oodD' 88   88 88ooo88    88       88    88V8o 88 88
88    88 88~~~   88   88 88~~~88    88       88    88 V8o88 88  ooo
88b  d88 88      88  .8D 88   88    88      .88.   88  V888 88. ~8~
~Y8888P' 88      Y8888D' YP   YP    YP    Y888888P VP   V8P  Y888P

                                                                     """)
    os.system("git clone https://github.com/Senuka072/Password-Generator.git")
    print(Fore.BLUE + "Tool Updated" + Fore.RED +  "!")

cho = int(input(Fore.GREEN + "[+]" + Fore.BLUE + "\t Choice :: "))

print()

if cho == 1:
    passwordGen()
elif cho == 2:
    updatetool()
elif cho == 3:
    exit()
