import subprocess
import re
import json

cmd = (
    'powershell -Command "Get-PnpDevice -Class Display | '
    'Select-Object -Property InstanceId, FriendlyName | ConvertTo-Json"'
)

output = subprocess.check_output(cmd, shell=True, text=True)
gpu_info = json.loads(output)

match = re.search(r'DEV_([0-9A-F]{4})', gpu_info['InstanceId'], re.I)
if match:
    device_id = match.group(1).upper()
    print(gpu_info['FriendlyName'])
    print(device_id)
