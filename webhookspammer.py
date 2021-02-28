import requests, os, platform, time
from colorama import Fore, Back, Style
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("Webhook Spammer")

cmd = 'mode 36,25'
os.system(cmd)

class color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;36m'
   GREEN = '\033[32m'
   YELLOW = '\033[  1;33;48m'
   RED = '\033[31m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'
   WHITE = '\033[37m'

print(color.RED+" ──────────────────────────────────")
print(color.RED+" ╔═╗╔═╗╔═╗╔╦╗╔╦╗╔═╗╦═╗")
print(color.RED+" ╚═╗╠═╝╠═╣║║║║║║║╣ ╠╦╝")
print(color.RED+" ╚═╝╩  ╩ ╩╩ ╩╩ ╩╚═╝╩╚═")
print(color.RED+" ──────────────────────────────────")
print("")

webhook = input(color.WHITE +"Webhook Link: ")
text = input(color.WHITE +"Message Content: ")

if platform.system() == "Windows":
    clearcmd = "cls"
else:
    clearcmd = "clear"

os.system(clearcmd)

data = {
    "content": text
}
def send(i):
    res = requests.post(webhook, data=data)
    try:
        print(color.RED + 'Getting ratelimited, waiting ' + str(res.json()["retry_after"]) + 'ms.')
        time.sleep(res.json()["retry_after"]/1000)
        res = 'Waited ' + Fore.RED + str(res.json()["retry_after"]) + 'ms.'
    except:
        i += 1
        res = "Sent message."
    print(color.GREEN + res + color.GREEN + ' Total: ' + color.WHITE + str(i))
    return i
i = 0
while True:
   i = send(i)