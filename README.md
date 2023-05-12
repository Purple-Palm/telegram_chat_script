# Telegram Chat Script

## Installing python stuff
Install python https://www.python.org/downloads/

Install pip https://bootstrap.pypa.io/get-pip.py
   - Right click -> Save -> Open downloads folder -> in PATH-bar just write `cmd` and press Enter -> in console write `python get-pip.py`


Install Chocolatey
In powershell opened as administrator run this command
```
{Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
## Creating telegram app
Next you need to know your <api_id> and <api_hash>. 

Go to https://my.telegram.org/ -> enter your phone number -> click `API Development Tools` -> in `App title` write `Github` -> in `Short name` wriet `Githubb` -> in `Platform` choose `Desktop` -> click `Create application`
After that you will see two labels: `App api_id:` and `App api_hash:`. 
<sub>Keep this site open</sub>

## Preparing to run
1. Then download .zip file from repository.

2. Extract folder and open.

3. Press `Ctrl + A` to select all files and `Ctrl + C` to copy them. 

4. Paste everything to the Telegram folder:
   - On desktop right button on `Telegram` shortcut -> Open file lication -> `Ctrl + V`.
   
   - Go to disk where your Telegram located -> Users -> <your user name> -> AppData -> Roaming -> Telegram Desktop -> `Ctrl + V`.

5. Create a shortcut of `Telegram.bat` and put it on desktop.

6. Open `INSTALL-FIRST.bat` and in console type `Y`.

7. Edit `Telegram.bat` -> copy `App api_id:` and `App api_hash:`, and replace `<api_id>` and `<api_hash>` with these numbers.

8. Open `Telegram.bat` from desktop.
