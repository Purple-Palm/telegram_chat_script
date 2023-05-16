#developers are not native english speakers so please don't be mad
    
####################
## Import libs
import sys
import asyncio
import time
import yaml

from telethon.sync import TelegramClient
from telethon import TelegramClient
from telethon import events

# from telethon                       import functions, types
# from telethon.tl.types              import ChatBannedRights
# from telethon.tl.functions.users    import GetFullUserRequest
# from telethon.tl.functions.channels import EditBannedRequest



version = "1.1.0 Beta"   #version variable that changes in version text line

###########################
## Console color print
red    = [206, 76,  54]
green  = [68,  250, 123]
blue   = [253, 127, 233]
yellow = [241, 250, 118]
orange = [255, 184, 107]
gray   = [128, 128, 128] 
slate  = [192, 194, 201] #type of gray color
black1 = [2,2,2]         #not completely black color
def colored(color, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(color[0], color[1], color[2], text)


###########################
## Settings
api_id   = int(sys.argv[1])
api_hash = str(sys.argv[2])

## Connect
client = TelegramClient('users/current_user', api_id, api_hash)
client.start()

## Translation
with open('languages/choose-language.yml', 'r', encoding='utf-8') as f:
    chosenlang = yaml.safe_load(f)

with open('languages/translations.yml', 'r', encoding='utf-8') as f:
    translations = yaml.safe_load(f)

lang = chosenlang['language'][0] + chosenlang['language'][1]

  

####################
## Account info
####################
print(colored(gray, "Script by Cactus and VGSS_"))                          #Authors
entity = client.get_entity("me")                                            
MY_ID = entity.id                                                           #telegram account id variable
print(
        "["
        + colored(green, "PROFILE: ")                                       #prints 'PROFILE' text in green color
        + str(entity.first_name)                                            #prints your account first name
        + " | " + colored(orange, "Id: ") + str(MY_ID)                      #prints 'Id' text in orange color and your telegram account id  
        + " | " + colored(orange, "Uname: ") + "@" + str(entity.username)   #prints your telegram account username
        + "]"
        + colored(black1, "        ur gay)")                                #easter egg) don't be mad
)
print(             
        colored(green, "✓ ")                                                #prints green checkmark
        + translations[lang]['script-successfully-launched']                #prints 'Script successfully lauched' text
)
print(
        colored(green, translations[lang]['version'])                        #prints 'Version' text in green color
        + str(version)                                                      #prints version variable
)
print(                                                                      #prints list of commands
        "["
        + colored(blue, translations[lang]['command-list'])
        + "] "
        + colored(gray, translations[lang]['command-guide'])
        +".share "  
        + colored(slate, translations[lang]['share-command'])
        +".t [{}] ".format(translations[lang]['text-word'])  
        + colored(slate, translations[lang]['typing-command'])
        + ".heart <{}> ".format(translations[lang]['text-word'])  
        + colored(slate, translations[lang]['heart-command'])
        + ".zig <{}> ".format(translations[lang]['text-word'])  
        + colored(slate, translations[lang]['zig-command'])
        + ".minecraft <{}> ".format(translations[lang]['text-word'])  
        + colored(slate, translations[lang]['minecraft-command'])
        + ".sheep <{}> ".format(translations[lang]['text-word'])  
        + colored(slate, translations[lang]['sheep-command'])
)

########################
## Check script work
## CMD: ping
########################
@client.on(events.NewMessage(outgoing=True, pattern='ping'))     #if user type 'ping' in chat, bot will send 'pong' 
async def handler(event):
    if event.message.from_id.user_id != MY_ID:
        return

    m = await event.respond('pong')                              #sends 'pong' in responce to 'ping'
    await asyncio.sleep(1)
    await client.delete_messages(event.chat_id, [event.id, m.id])



#################
## Typing
## CMD: .t
## ARG: text
#################
@client.on(events.NewMessage(pattern=".t+"))                    #.t+ means that after the command you can put the text that will be displayed  
async def handler(event):
    if event.message.from_id.user_id != MY_ID:                  
        return

    try:
        if event.message.message.replace(".t ", "") == ".t":
            return

        text      = event.message.message.split(".t ", maxsplit=1)[1]            #splits text by one symbol
        orig_text = text                                                          
        message   = event.message                                                #gets data about message that sended
        chat      = event.chat_id                                                #gets chat id that which message sended in

        tbp = "" # to be printed
        typing_symbol = "/"
     
        while(tbp != orig_text):
            typing_symbol = "_"                                                  #puts '_' symbol while it types
            await client.edit_message(chat, message, tbp + typing_symbol)        #edits message
            await asyncio.sleep(0.1)

            tbp = tbp + text[0]
            text = text[1:]

            typing_symbol = "-"
            await client.edit_message(chat, message, tbp)                        #edits sended message
            await asyncio.sleep(0.1)
    except:
        print( "[" + colored(red, translations[lang]['error-title']) + "] " + translations[lang]['error-message1'] + " [.t] " + translations[lang]['error-message2'] )  #print Error in case something not right



######################
## Heart Animation
## CMD: .heart
## ARG: text
######################
heart_emoji = [       #List of emoji that used in animation  '1 - 2'
    "✨-💎",
    "✨-🌺",
    "☁️-😘",
    "✨-🌸",
    "🌾-🐸",
    "🔫-💥",
    "☁️-💟",
    "🍀-💖",
    "🌴-🐼",
    "🟥-⬛"
]
# Pattern of animation
edit_heart = '''      
1 2 2 1 2 2 1
2 2 2 2 2 2 2
2 2 2 2 2 2 2
1 2 2 2 2 2 1
1 1 2 2 2 1 1
1 1 1 2 1 1 1
'''

@client.on(events.NewMessage(pattern=".heart+"))            #.heart+ means that after the command you can put the text that will be displayed        
async def handler(event):
    if event.message.from_id.user_id != MY_ID:
        return

    try:
        text = event.message.message.replace(".heart ", "")
        if text == ".heart":
            text = "Love this animations? ||Me too bro, this is V1.1.0||"                                      #text that will be displayed at the end of animation instead of user's

        message   = event.message
        chat      = event.chat_id

        # play anim
        frame_index = 0
        while(frame_index != len(heart_emoji)):
            await client.edit_message(chat, message, edit_heart.replace("1", heart_emoji[frame_index].split("-")[0])      #replaces 1's with first emojis from list that separated by '-'
                                                               .replace("2", heart_emoji[frame_index].split("-")[1]))     #replaces 2's with second emojis from list that separated by '-'
            await asyncio.sleep(1)
            frame_index = frame_index + 1

        await client.edit_message(chat, message, text)            #edits sended message
    except:
        print( "[" + colored(red, translations[lang]['error-title']) + "] " + translations[lang]['error-message1'] + " [.heart] " + translations[lang]['error-message2'] )     #print Error in case something not right

######################
## Svastica Animation
## CMD: .zig
## ARG: text
######################
zig_emoji = [                   #List of emoji that used in animation  '1 - 2'
    "🌕-🌑",
    "🙋‍♂️-💀",
    "♥️-♠️",
    "♦️-♣️",
    "🔴-⚫️",
    "❤️-🖤",
    "🟥-⬛",
    "🔥-🔯"
]
# Pattern of animation
edit_zig = '''                  
2 1 2 2 2
2 1 2 1 1
2 2 2 2 2
1 1 2 1 2
2 2 2 1 2
'''

@client.on(events.NewMessage(pattern=".zig+"))                  #.zig+ means that after the command you can put the text that will be displayed 
async def handler(event):
    if event.message.from_id.user_id != MY_ID:
        return

    try:
        text = event.message.message.replace(".zig ", "")
        if text == ".zig":
            text = " "                                          #text that will be displayed at the end of animation instead of user's         

        message   = event.message
        chat      = event.chat_id

        # play anim
        frame_index = 0
        while(frame_index != len(zig_emoji)):
            await client.edit_message(chat, message, edit_zig.replace("1", zig_emoji[frame_index].split("-")[0])         #replaces 1's with first emojis from list that separated by '-'
                                                             .replace("2", zig_emoji[frame_index].split("-")[1]))         #replaces 2's with second emojis from list that separated by '-'
            await asyncio.sleep(1)
            frame_index = frame_index + 1

        await client.edit_message(chat, message, text)          #edits sended message
    except:
        print( "[" + colored(red, translations[lang]['error-title']) + "] " + translations[lang]['error-message1'] + " [.zig] " + translations[lang]['error-message2'] )               #print Error in case something not right

########################
## Minecraft Animation
## CMD: .minecraft
## ARG: text
########################
minecraft_emoji = [                 #pattern of animation
    "🟩 🟩 🟩 🟩 🟩",
    "🟩 🟩 🟩 🟩 🟩\n🟫 🟫 🟫 🟫 🟫",
    "🟩 🟩 🟩 🟩 🟩\n🟫 🟫 🟫 🟫 🟫\n🟫 🟫 🟫 🟫 🟫",
    "🟩 🟩 🟩 🟩 🟩\n🟫 🟫 🟫 🟫 🟫\n🟫 🟫 🟫 🟫 🟫\n🟫 🟫 🟫 🟫 🟫",
    "🟩 🟩 🟩 🟩 🟩\n🟫 🟫 🟫 🟫 🟫\n🟫 🟫 🟫 🟫 🟫\n🟫 🟫 🟫 🟫 🟫\n🟫 🟫 🟫 🟫 🟫",
    "💚💚💚💚💚\n🤎🤎🤎🤎🤎\n🤎🤎🤎🤎🤎\n🤎🤎🤎🤎🤎\n🤎🤎🤎🤎🤎",
    "🟢🟢🟢🟢🟢\n🟤🟤🟤🟤🟤\n🟤🟤🟤🟤🟤\n🟤🟤🟤🟤🟤\n🟤🟤🟤🟤🟤",
    "🍏🍏🍏🍏🍏\n🥥🥥🥥🥥🥥\n🥥🥥🥥🥥🥥\n🥥🥥🥥🥥🥥\n🥥🥥🥥🥥🥥",
    "🫑🫑🫑🫑🫑\n🥔🥔🥔🥔🥔\n🥔🥔🥔🥔🥔\n🥔🥔🥔🥔🥔\n🥔🥔🥔🥔🥔",
    "🌳🌳🌳🌳🌳\n🪵🪵🪵🪵🪵\n🪵🪵🪵🪵🪵\n🪵🪵🪵🪵🪵\n🪵🪵🪵🪵🪵",
    "🟩 🟩 🟩 🟩 🟩\n🟫 🟫 🟫 🟫 🟫\n🟫 🟫 🟫 🟫 🟫\n🟫 🟫 🟫 🟫 🟫\n🟫 🟫 🟫 🟫 🟫",
    "🟩 🟩 🟩 🟩 🟩\n🟫 🟫 🟫 🟫 🟫\n🟫 🟫 🟫 🟫 🟫\n🟫 🟫 🟫 🟫 🟫",
    "🟩 🟩 🟩 🟩 🟩\n🟫 🟫 🟫 🟫 🟫\n🟫 🟫 🟫 🟫 🟫",
    "🟩 🟩 🟩 🟩 🟩\n🟫 🟫 🟫 🟫 🟫",
    "🟩 🟩 🟩 🟩 🟩",
    "⠀"
]

@client.on(events.NewMessage(pattern=".minecraft+"))                #.minecraft+ means that after the command you can put the text that will be displayed 
async def handler(event):
    if event.message.from_id.user_id != MY_ID:
        return

    try:
        text = event.message.message.replace(".minecraft ", "")
        if text == ".minecraft":
            text = ""                                               #text that will be displayed at the end of animation instead of user's

        message = event.message
        chat    = event.chat_id

        for emoji in minecraft_emoji:                               #cycle that runs animation

            await client.edit_message(chat, message, emoji)         #edits sended message
            await asyncio.sleep(0.5)                                #speed of animation

        await client.edit_message(chat, message, text)
    except:
        print("[" + colored(red, translations[lang]['error-title']) + "] " + translations[lang]['error-message1'] + " [.minecraft] " + translations[lang]['error-message2'])        #print Error in case something not right
        
########################
## Sheep Animation
## CMD: .sheep
## ARG: text
########################
sheep_emoji = [                 #pattern of animation
    "⠀⬜️⬜️⬜️⬜️⬜️",
    "⠀⬜️⬜️⬜️⬜️⬜️\n⠀⬛️⬜️⬜️⬜️⬜️",
    "⠀⬜️⬜️⬜️⬜️⬜️\n⠀⬛️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️",
    "⠀⬜️⬜️⬜️⬜️⬜️\n⠀⬛️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️",
    "⠀⬜️⬜️⬜️⬜️⬜️\n⠀⬛️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️",
    "⠀⬜️⬜️⬜️⬜️⬜️\n⠀⬛️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️",
    "⠀⬜️⬜️⬜️⬜️⬜️\n⠀⬛️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️",
    "⠀⬜️⬜️⬜️⬜️⬜️\n⠀⬛️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️",
    "⠀⬜️⬜️⬜️⬜️⬜️\n⠀⬛️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️",
    "⠀⬜️⬜️⬜️⬜️⬜️\n⠀⬛️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️",
    "⠀⬜️⬜️⬜️⬜️⬜️\n⠀⬛️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟫🟫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟫🟫",
    "⠀⬜️⬜️⬜️⬜️⬜️\n⠀⬛️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟫🟫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟫🟫\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟫🟫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟫🟫",
    "⠀⬜️⬜️⬜️⬜️⬜️\n⠀⬛️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️⠀⠀⠀⠀⠀⠀⠀⬜️⬜️⬜️\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟫🟫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟫🟫\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟫🟫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀🟫🟫\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬛️⬛️⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⬛️⬛️",  
]

@client.on(events.NewMessage(pattern=".sheep+"))                #.minecraftsheep+ means that after the command you can put the text that will be displayed 
async def handler(event):
    if event.message.from_id.user_id != MY_ID:
        return

    try:
        text = event.message.message.replace(".sheep ", "")
        if text == ".sheep":
            text = ""                                               #text that will be displayed at the end of animation instead of user's

        message = event.message
        chat = event.chat_id

        for emoji in sheep_emoji:                               #cycle that runs animation

            await client.edit_message(chat, message, emoji)         #edits sended message
            await asyncio.sleep(0.3)                                #speed of animation

        await client.edit_message(chat, message, text)
    except:
        print("[" + colored(red, translations[lang]['error-title']) + "] " + translations[lang]['error-message1'] + " [.sheep] " + translations[lang]['error-message2'])        #print Error in case something not right
        


## RUN
client.run_until_disconnected()
