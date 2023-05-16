# Telegram Chat Script

## :arrow_down: How to install
**1. Install python and pip**
> 1) Install [python](https://www.python.org/downloads/)
> 
> 2) Install [pip](https://bootstrap.pypa.io/get-pip.py)
>     - Right click -> Save -> Open downloads folder -> in PATH-bar just write `cmd` and press Enter -> in console write `python get-pip.py`



**2. Install Chocolatey**
> In powershell opened as administrator run this command
```
{Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
**3. Create telegram app**

This step is to get your <api_id> and <api_hash>. 

> Go to https://my.telegram.org/ -> enter your phone number -> click `API Development Tools` -> in `App title` write `Github` -> in `Short name` write `Githubb` -> in `Platform` choose `Desktop` -> click `Create application`
After that you will see two labels: `App api_id:` and `App api_hash:`. 

<sub>Keep this site open</sub>

### Preparing for the first launch
1. [Clone](How_to_clone_repo.md) the repository/download and extract .zip into the root folder of the Telegram.

3. Create a shortcut to the `Telegram.bat` file and send it to the desktop.

4. Open `INSTALL-FIRST.bat` as administrator and in console accept everything. <sub>Type `Y` and then `enter`.</sub>

5. Edit `Telegram.bat` file -> copy `App api_id:` and `App api_hash:` from [API development tools](https://my.telegram.org/apps), and replace `<api_id>` and `<api_hash>` with your number (API's).

6. Open `Telegram.bat`.


## :electric_plug: How to use

1. Launch the script and wait until it completely launched.

2. Open Telegram on your PC/Lalptop/Phone or device where you logged in with your account.

3. Type in messagebar `.` command (for example `.heart`).

4. Press enter and watch the process.

## :globe_with_meridians: How to change language

You can change language of translation. You can see translated text in console tab after code launch.

Go to your Telegram root folder -> data -> languages -> edit choose-language.yml and change `'en'` in ```yml language: 'en' ```to the one of listed letters below.
