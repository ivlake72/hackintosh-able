import subprocess
import json 

final_data = {
    "AUDIO": [],
}

def getAudioChipsetInfo():
    cmd = 'powershell -Command "Get-CimInstance Win32_SoundDevice | Select-Object Name | ConvertTo-Json"'
    output = subprocess.check_output(cmd, shell=True, text=True)
    ac_info = json.loads(output)

    for audio in ac_info:
        final_data['AUDIO'].append(audio['Name'])


def getAudioInfo():
    getAudioChipsetInfo()
    return final_data["AUDIO"]