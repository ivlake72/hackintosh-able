import subprocess
import json 

import os, sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

final_data = {
    "AUDIO": [],
}

def getAudioChipsetInfo():
    cmd = 'powershell -Command "Get-CimInstance Win32_SoundDevice | Select-Object Name | ConvertTo-Json"'
    output = subprocess.check_output(cmd, shell=True, text=True)
    ac_info = json.loads(output)

    with open(resource_path("compatible-dict.json"), "r") as f:
        unsuppored_audio_list = json.loads(f.read())['unsupported_sounds']
        
        for audio in ac_info:
            if audio['Name'] in unsuppored_audio_list:
                final_data['AUDIO'].append({'modelName': audio['Name'], 'isSupported': False, 'message': 'Need VoodooHDA.kext'})
            else: 
                final_data['AUDIO'].append({'modelName': audio['Name'], 'isSupported': True, 'message': ''})


def getAudioInfo():
    getAudioChipsetInfo()
    return final_data["AUDIO"]
