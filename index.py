from tools.CPUInfo import getCPUInfo
from tools.GPUInfo import getGPUInfo
from tools.MotherBoardInfo import getMotherBoardInfo
from tools.AudioChipsetInfo import getAudioInfo
import os, webbrowser

os.system('cls')

running = True
isAlreadyGot = False
final_data = {}

def status_color(status, label="- Is Supported?:"):
    color = "\033[32m" if status else "\033[31m"
    print(f"\033[90m{label}\033[0m {color}{status}\033[0m")

while running:
    print("== Hackintosh-Able by Lumex57 ==")

    if not isAlreadyGot:
        print('[+] Getting CPU Info..')
        final_data['CPU'] = getCPUInfo()

        print('[+] Getting GPU Info..')
        final_data['GPU'] = getGPUInfo()

        print('[+] Getting Motherboard info..')
        final_data['MB'] = getMotherBoardInfo()

        print('[+] Getting Audio info..')
        final_data['AC'] = getAudioInfo()

        isAlreadyGot = True

    os.system('cls')

    print("== Hackintosh-Able by Lumex57 ==")
    print('\n')

    print('\033[36m[+] CPU\033[0m')
    print(f'\033[90m- Model Name:\033[0m {final_data["CPU"]['modelName']}')
    print(f'\033[90m- Code Name:\033[0m {final_data["CPU"]['codename']}')
    status_color(final_data["CPU"]['isSupported'])

    print('\n')
    print('\033[36m[+] GPU\033[0m')
    print(f'\033[90m- Model Name:\033[0m {final_data["GPU"]['modelName']}')
    status_color(final_data["GPU"]['isSupported'])

    print('\n')
    print('\033[36m[+] Motherboard\033[0m')
    print(f'\033[90m- Model Name:\033[0m {final_data["MB"]['modelName']}')
    status_color(final_data["MB"]['isSupported'])

    print('\n')
    print('\033[36m[+] Audio\033[0m')

    for i in range(len(final_data["AC"])):

        print(f'\033[90m===========\n')
        print(f'\033[90m- Model Name:\033[0m {final_data["AC"][i]['modelName']}')
        status_color(final_data["AC"][i]['isSupported'])
        print('\n')

    print('\033[90m- Options\033[0m')
    print('\033[90m[1] Exit\033[0m')
    print('\033[90m[2] Go To Repository\033[0m')
    inn = input("> ")

    if inn == "1":
        running = False
    if inn == "2":
        webbrowser.open("https://github.com/lumex57/hackintosh-able")

