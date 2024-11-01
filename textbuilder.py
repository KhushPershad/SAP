import sys

logPath = sys.argv[1]
with open(logPath, "r") as file:
    log = file.read()

dict = {"enter":"\n", "tab":"\t", "space":" ", "shift": "", "ctrl_l": "", "ctrl_r":"", "esc": ""}
text = ""
for key in log.split(" "):
    if "Key" not in key:
        text += key
        continue
    key = key.removeprefix("Key.")
    if key == "backspace" and len(text) == 0:
        pass
    elif key == "backspace" and len(text) > 0:
        text = text[:-1]
    else:
        text += dict[key]
            

print(text)
