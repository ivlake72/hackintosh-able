import subprocess
import json

supported_motherboards = ["Z370-A", "B450M PRO4", "Z490-E"]

def get_motherboard_model():
    cmd = 'powershell -Command "Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer, Product | ConvertTo-Json"'
    output = subprocess.check_output(cmd, shell=True, text=True)
    mb_info = json.loads(output)
    product = mb_info.get("Product", "")
    return f"{product}"


print(get_motherboard_model())