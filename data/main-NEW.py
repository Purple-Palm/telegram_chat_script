import sys
import asyncio
import time
import yaml 
import yaml.scanner
import re

from telethon import TelegramClient, errors
from telethon.sync import TelegramClient
from telethon import events


###########################
## Settings
###########################

## Console color print
red    = [206, 76,  54]
green  = [68,  250, 123]
blue   = [17, 168, 205]
yellow = [241, 250, 118]
orange = [255, 184, 107]
gray   = [128, 128, 128] 
slate  = [192, 194, 201] #type of gray color
black1 = [2,2,2]         #not completely black color
def colored(color, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(color[0], color[1], color[2], text)

## Config 
github_repo_link = "https://github.com/Purple-Palm/telegram_chat_script"
config_is_loaded = False
try:
        with open('config.yml', 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
        config_is_loaded = True

        version = config['version']
        share_command = config['share']['command']
        typing_command = config['typing']['command']
        heart_command = config['heart_animation']['command']
        zig_command = config['zig_animation']['command']
        minecraft_command = config['minecraft_animation']['command']
        sheep_command = config['sheep_animation']['command']
        

except yaml.scanner.ScannerError as error:
        print(colored(red,error))
        print(
              "[" + colored(red, "ERROR") + "]", 
              colored(blue, "Config file"),
              "might be", 
              colored(orange,"corrupted."), 
              "Try to fix it or downoad it again from", 
              colored(blue, github_repo_link)
              )
        input("Press Enter to continue...")  # Wait for user input
        sys.exit(11) # ERROR_BAD_FORMAT

except FileNotFoundError as error:
        print(colored(red,error))
        print(
              "[" + colored(red, "ERROR") + "]", 
              colored(blue, "Config file"), 
              colored(orange,"is not found."), 
              "Try to find it, change it's name to",
              colored(blue, "config.yml"),
              "or downoad it again from", 
              colored(blue, github_repo_link)
              )
        input("Press Enter to continue...")  # Wait for user input
        sys.exit(2) # ERROR_FILE_NOT_FOUND


## Translation
chosen_language = config['language']
language_is_loaded = False
try:                                                    
        with open(f'languages/{chosen_language}.yml', 'r', encoding='utf-8') as f: 
                translation = yaml.safe_load(f) 

        language_is_loaded = True

        errorMessage = translation['errors']
        commandsGuide = translation['commands']
        word_text = translation['word-text']
        word_seconds = translation['word-seconds']
        word_size = translation['word-size']

except FileNotFoundError as error:
        print(colored(red,error))
        print(
              "[" + colored(red, "ERROR") + "]", 
              colored(blue, "English Language translation file"), 
              colored(orange,"is not found."), 
              "Try to find it, change it's name to",
              colored(blue, "{}}.yml").format(chosen_language),
              "or downoad it again from", 
              colored(blue, github_repo_link)
              )
        input("Press Enter to continue...")  # Wait for user input
        sys.exit(2) # ERROR_FILE_NOT_FOUND
        
except yaml.scanner.ScannerError as error:
        print(colored(red,error))
        print(
              "[" + colored(red, "ERROR") + "]", 
              colored(blue, "Chosen Language ({}) translation file").format(chosen_language),
              "might be", 
              colored(orange,"corrupted."), 
              "Try to fix it or downoad it again from", 
              colored(blue, github_repo_link)
              )
        input("Press Enter to continue...")  # Wait for user input
        sys.exit(11) # ERROR_BAD_FORMAT

except:
        with open('languages/en_us.yml', 'r', encoding='utf-8') as f: # Load default language 
                translation = yaml.safe_load(f) 
        print("[" + colored(red, translation['errors']['error-title']) + "]" 
              + translation['errors']['wrong-language'])


## API info 
api_id   = int(sys.argv[1])
api_hash = str(sys.argv[2])

## Connect
client = TelegramClient('users/current_user', api_id, api_hash)
client.start()




####################
## Account info
####################
print(colored(gray, "Script by Cactus and VGSS_"))                          #Authors
entity = client.get_entity("me")                                            
MY_ID = entity.id                                                           #telegram account id 

# Connection / Acount information 
print(
        "["
        + colored(green, "PROFILE: ")                                           #prints profile label text in green color
        + str(entity.first_name)                                                #prints your account first name
        + " | " + colored(orange, "Id: ") + str(MY_ID)                          #prints id label text in orange color and your telegram account id  
        + " | " + colored(orange, "Username: ") + "@" + str(entity.username)    #prints your telegram account username
        + "]"
)
# Confirmation of script launch
print(
        colored(green, "✓ ")                                                #prints green checkmark
        + translation['script-successfully-launched']                        #prints succesful launch message
)                
# Version of the script
print(
        colored(green, translation['version'])                        #prints version label text in green color
        + str(version)                                                      #prints current version 
)
# Commands
print(
        "["
        + colored(blue, commandsGuide['commands-title'])
        + "] " + "\n"
        + colored(gray, commandsGuide['syntax-guide'].format(word_seconds, word_size, word_text)) + "\n"
        +f"{share_command} "  
        + colored(slate, commandsGuide['share-command']) + "\n"
        +f"{typing_command} [{colored(gray,word_text)}] "
        + colored(slate, commandsGuide['typing-command']) + "\n"
        + f"{heart_command} <speed=[{colored(gray,word_seconds)}]> <size=[{colored(gray,word_size)}]> <{colored(gray,word_text)}> "     
        + colored(slate, commandsGuide['heart-command']) + "\n"
        + f"{zig_command} <speed=[{colored(gray,word_seconds)}]> <size=[{colored(gray,word_size)}]> <{colored(gray,word_text)}> "
        + colored(slate, commandsGuide['zig-command']) + "\n"
        + f"{minecraft_command} <speed=[{colored(gray,word_seconds)}]> <{colored(gray,word_text)}> "
        + colored(slate, commandsGuide['minecraft-command']) + "\n"
        + f"{sheep_command} <speed=[{colored(gray,word_seconds)}]> <{colored(gray,word_text)}> "  
        + colored(slate, commandsGuide['sheep-command']) + "\n"
)




########################
## Check script work
## CMD: ping
########################
@client.on(events.NewMessage(outgoing=True, pattern='ping'))     #if user type 'ping' in chat, bot will send 'pong' 
async def handler(event):
    if event.message.from_id.user_id != MY_ID:
        return
    if event.text == 'ping':
        m = await event.respond('pong')                              #sends 'pong' in responce to 'ping'
        await asyncio.sleep(1)
        await client.delete_messages(event.chat_id, [event.id, m.id])



######################
## Heart Animation
## CMD: .heart
## ARG: text
######################
with open('animations/heart_animation.yml', 'r', encoding='utf-8') as f:
        heart_animation = yaml.safe_load(f)

heart_settings = config['heart_animation']
heart_speed = heart_settings['animation_speed']
heart_size = heart_settings['size']

@client.on(events.NewMessage(pattern=r"\{}(\s+speed=(\d+(\.\d+)?))?(\s+size=(\w+))?(\s+(.*))?".format(heart_command)))  # Using raw input it makes possible to determine specific arguments like 'speed='
async def handler(event):
    if event.message.from_id.user_id != MY_ID: # If message comes from someone but user it will not execute
        return
    try:

        # Get info about message that has been sent and chat where message is located in
        message   = event.message
        chat      = event.chat_id  
        input_text = event.text 
        print(commandsGuide['command-issued'], colored(blue, input_text)) # Print issued command by user in console

        temp_text = input_text
        temp_text = temp_text.replace(heart_command, "")

        # Extract animation size 
        size_match = re.search(r"size=(\w+)", temp_text.lower())
        size = size_match.group(1) if size_match else heart_size
        temp_text = temp_text.replace(size_match.group(0), "") if size_match else temp_text

        # Exctract animation speed argument
        speed_match = re.search(r"speed=(\d+(\.\d+))", temp_text.lower())
        speed = float(speed_match.group(1)) if speed_match else heart_speed 
        temp_text = temp_text.replace(speed_match.group(0), "") if speed_match else temp_text

        text = temp_text

        # Prepare to animate
        heart_emoji = heart_animation['emoji'] # Get all emojis for animation
        try:
                heart_template = "\n".join(heart_animation['animation'][f'{size}']) 
        except:
                print(errorMessage['invalid-size'].format(size))
                heart_template = "\n".join(heart_animation[f'{heart_size}']) 

        # Play animation
        try:
                frame_index = 0
                while(frame_index != len(heart_emoji)):
                        await client.edit_message(chat, message, heart_template.replace("1", heart_emoji[frame_index].split("-")[0])      #replaces 1's with first emojis from list that separated by '-'
                                                                        .replace("2", heart_emoji[frame_index].split("-")[1]))     #replaces 2's with second emojis from list that separated by '-'
                        await asyncio.sleep(speed)
                        
                        frame_index = frame_index + 1  

                if text == " " or text == "":
                        pass
                else:
                        await client.edit_message(chat, message, text)            #edits sended message
                print(colored(green,commandsGuide['command-done']), input_text)

        except errors.FloodWaitError as output:  # If telegram prevents user from editing the message creating the flood, this exception wont let script to crash
                        print( "[" + colored(orange, errorMessage['warning-title']) + "] " + errorMessage['flood-error'], f"\n{output}")     #notifies a user about the problem occurred with comand 
        
    except:
        print( "[" + colored(red, errorMessage['error-title']) + "] " + errorMessage['wrong-command'], colored(blue, heart_command))     #notifies a user about the problem occurred with comand 


####################################################################################################################################################################################
## TESTING AREA



# def is_command(command):
#         for parameter in config:
#                 parameter_value = config[parameter]
#                 if type(parameter_value) is dict:
#                         for option in parameter_value:
#                                 if command == parameter_value[option]:
#                                         return True
#         return False



    
# @client.on(events.NewMessage(pattern=r"\.(\s+speed=(\d+(\.\d+)?))?(\s+size=(\w+))?(\s+(.*))?"))  # Using raw input it makes possible to determine specific arguments like 'speed='
# async def handler(event):
#     if event.message.from_id.user_id != MY_ID: # If message comes from someone but user it will not execute
#         return
#     command_match = re.search(r"\.\w+", event.text.lower())
#     print(event.text.lower(), command_match.group(0), command_match)
#     command = command_match.group(0) if command_match else event.text.lower().split()[0]
#     if is_command(command) == False:
#         print(command, is_command(command))
#         return
#     else:
#         print(command, is_command(command))
#         command = command.replace(".", "")       
#     try:
#         with open('animations/{}_animation.yml'.format(command), 'r', encoding='utf-8') as f:
#                 animation = yaml.safe_load(f)
#         animation_settings = config['{}_animation'.format(command)]
#         animation_speed = animation_settings['animation_speed']
#         animation_size = animation_settings['size']

#         # Get info about message that has been sent and chat where message is located in
#         message   = event.message
#         chat      = event.chat_id  
#         input_text = event.text 
#         print(commandsGuide['command-issued'], colored(blue, input_text)) # Print issued command by user in console

#         temp_text = input_text
#         temp_text = temp_text.replace(heart_command, "")

#         # Extract animation size 
#         size_match = re.search(r"size=(\w+)", temp_text.lower())
#         size = size_match.group(1) if size_match else animation_size
#         temp_text = temp_text.replace(size_match.group(0), "") if size_match else temp_text

#         # Exctract animation speed argument
#         speed_match = re.search(r"speed=(\d+(\.\d+))", temp_text.lower())
#         speed = float(speed_match.group(1)) if speed_match else animation_speed 
#         temp_text = temp_text.replace(speed_match.group(0), "") if speed_match else temp_text

#         text = temp_text

#         # Prepare to animate
#         animation_emoji = animation['emoji'] # Get all emojis for animation
#         try:
#                 animation_template = "\n".join(animation['animation'][f'{size}']) 
#         except:
#                 print(errorMessage['invalid-size'].format(size))
#                 animation_template = "\n".join(animation['animation'][f'{animation_size}']) 

#         # Play animation
#         try:
#                 frame_index = 0
#                 while(frame_index != len(animation_emoji)):
#                         await client.edit_message(chat, message, animation_template.replace("1", animation_emoji[frame_index].split("-")[0])      #replaces 1's with first emojis from list that separated by '-'
#                                                                         .replace("2", animation_emoji[frame_index].split("-")[1]))     #replaces 2's with second emojis from list that separated by '-'
#                         await asyncio.sleep(speed)
                        
#                         frame_index = frame_index + 1  

#                 if text == " " or text == "":
#                         pass
#                 else:
#                         await client.edit_message(chat, message, text)            #edits sended message
#                 print(colored(green,commandsGuide['command-done']), input_text)

#         except errors.FloodWaitError as output:  # If telegram prevents user from editing the message creating the flood, this exception wont let script to crash
#                         print( "[" + colored(orange, errorMessage['warning-title']) + "] " + errorMessage['flood-error'], f"\n{output}")     #notifies a user about the problem occurred with comand 
        
#     except:
#         print( "[" + colored(red, errorMessage['error-title']) + "] " + errorMessage['wrong-command'], colored(blue, f".{command}"))     #notifies a user about the problem occurred with comand 
    

## RUN
client.run_until_disconnected()