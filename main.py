print(
    "1. Deity Hub\n"
    "2. W-azure Hub\n"
    "3.Sea hub"
)
deityhubscript = input("your choice:")
if deityhubscript == "1":
    script = requests.get("https://pastebin.com/raw/D5vHuHXz").text
    print(script)
if deityhubscript == "2":
    script = requests.get("https://pastebin.com/raw/uyptWCd1").text
    print(script)
if deityhubscript == "3":
    script = requests.get("https://pastebin.com/raw/v62nzyfD3").text
    print(script)
 #deptrai
