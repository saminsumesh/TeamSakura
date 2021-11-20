import random


data = {
    "r": "Rᴏᴄᴋ🪨",
    "p": "Pᴀᴘᴇʀ📜",
    "s": "Sᴄɪssᴏʀ✂️"
}


def main():
    print("Gᴀᴍᴇ Sᴛᴀʀᴛᴇᴅ👑\n\n")
    while True:
        
        # keys
        keys = []
        for key in data:
            keys.append(key)
        
        # key of user 
        user_input = "Eɴᴛᴇʀ ʏᴏᴜʀ ᴋᴇʏ." + "\n" + "Kᴇʏs :-"
        for key in keys:
            user_input += f" '{key}' for {data[key]}"
        user_input += "\n:- "
        user = input(user_input)
        
        # key of computer/opponent
        computer = random.choice(keys)
        
        # text for print result
        text = "Yᴏᴜ: " + data[user] + "\n" + "Cᴏᴍᴘᴜᴛᴇʀ: " + data[computer]+"\n"
        
        # same keys
        if user == computer:
            print(text+"Sᴀᴍᴇ")
        
        # win keys
        elif (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
            print(text+"Yᴏᴜ Wᴏɴ😎")
        
        # lose keys
        else:
            print(text+"Yᴏᴜ ʟᴏsᴇ🥺")
        
        # next game or finished
        next = input("\nDᴏ ʏᴏᴜ ɴᴇᴇᴅ ᴛʜɪs ɢᴀᴍᴇ ᴀɢᴀɪɴ? 'y' ғᴏʀ ʏᴇs ᴀɴᴅ 'n' ғᴏʀ ɴᴏ.\n:- ")
        if next == "y" or next == "ʏᴇs":
            print("\n\nNᴇxᴛ Gᴀᴍᴇ")
        else:
            print("\nGᴀᴍᴇ Fɪɴɪsʜᴇᴅ")
            break

main()
