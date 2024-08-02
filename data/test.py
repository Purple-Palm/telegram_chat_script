import yaml
import emoji
import time
import sys
import os

import yaml.scanner


# with open('data/config.yml', 'r', encoding='utf-8') as f:
#     config = yaml.safe_load(f)

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

github_repo_link = "https://github.com/Purple-Palm/telegram_chat_script"
config_is_loaded = False
try:
        with open('data/config.yml', 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
        config_is_loaded = True

        version = config['version']

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



def heart_animation():
    with open('data/animations/heart_animation.yml', 'r', encoding='utf-8') as f:
        heart_animation = yaml.safe_load(f)

    heart_settings = config['heart_animation']
    heart_speed = heart_settings['animation_speed']
    heart_size = heart_settings['size']
    heart_emoji = heart_animation['emoji']
    try:
        heart_pattern = "\n".join(heart_animation[f'{heart_size}'])
    except:
        print("Invalid size {}".format(heart_size))
        heart_pattern = "\n".join(heart_animation['normal']['animation'])


    frame_index = 0
    while (frame_index != len(heart_emoji)):
        switch_emoji1 = emoji.emojize(heart_emoji[frame_index]).split("-")[0]
        switch_emoji2 = emoji.emojize(heart_emoji[frame_index]).split("-")[1]
        print(heart_pattern.replace("1", switch_emoji1).replace("2", switch_emoji2))
        print("#####") 
        time.sleep(heart_speed) 
        frame_index += 1

def minecraft_animation():
    with open('data/animations/minecraft_animation.yml', 'r', encoding='utf-8') as f:
        minecraft_animation = yaml.safe_load(f)

    minecraft_settings = config['minecraft_animation']
    minecraft_speed = minecraft_settings['animation_speed']
    minecraft_pattern = minecraft_animation['minecraft_emoji']

    for frame in minecraft_pattern:
        print(frame)
        print("#####")
        time.sleep(minecraft_speed) 

def display_animation(command): 
    animation_name = find_animation(command)
    with open(f'data/animations/{animation_name}.yml', 'r', encoding='utf-8') as f:
       animation = yaml.safe_load(f)
    animation_settings = config[animation_name]
    animation_speed = animation_settings['animation_speed']

    if len(animation) == 1:
        for pattern in animation:
            animation_pattern = animation[pattern]
        for frame in animation_pattern:
            print(frame)
            print("#####")
            time.sleep(animation_speed) 
    else:
        print("not supported yet")
    
    
    pass


def find_animation(command):
    for option in config:
         file_option = config[option]
         if type(file_option) is dict:
               for parameter in file_option:
                   option_parameter = file_option[parameter]
                   if option_parameter == command:
                        print("Found", command, "in", option)
                        return option


def reveal_config():
    print(colored(orange,"############\nCONFIG"))
    for option in config:
         file_option = config[option]
         print(colored(red,"FILE-OPTION: "), option) 
         if type(file_option) is dict:
               for parameter in file_option:
                   option_parameter = file_option[parameter]
                   print(colored(blue, "-PARAMETER: "), parameter)
                   print(colored(green,"--SETTING: "), option_parameter)
         else:
              print(colored(green,"--SETTING: "), file_option)
    print(colored(orange),"############")


def is_command(command):
    for option in config:
         file_option = config[option]
         if type(file_option) is dict:
               for parameter in file_option:
                   option_parameter = file_option[parameter]
                   if option_parameter == command:
                        print("Found", command, "in", option)
                        return True
    return False
                    

               


exceute_command = input("Command: ")

# if display_animation == ".heart":
#     heart_animation()
# elif display_animation == ".minecraft":
#     minecraft_animation()
if exceute_command.startswith("."):
    command = exceute_command.split()[0]
    print(command)
    print(colored(red,"Is command:"), is_command(command))
    if is_command(command):
         display_animation(command)
         
    #  reveal_config()
