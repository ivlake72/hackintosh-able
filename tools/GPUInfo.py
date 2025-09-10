import subprocess
import json
import re

import os, sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

final_data = {
    "GPU": {},
}

gpuCheckCmd = (
    'powershell -Command "Get-PnpDevice -Class Display | '
    'Select-Object -Property InstanceId, FriendlyName | ConvertTo-Json"'
)

def vendor_filter(friendlyName):
    name_lower = friendlyName.lower()
    if "radeon" in name_lower or "rx" in name_lower:
        return "amd"
    elif "intel" in name_lower:
        return "intel"
    elif "nvidia" in name_lower:
        return "nvidia"
    return "unknown"

def getGPUandCheckCompatible():
    output = subprocess.check_output(gpuCheckCmd, shell=True, text=True)
    gpu_info = json.loads(output)

    with open(resource_path("compatible-dict.json"), "r") as f:
        compatible_data = json.load(f)

    match = re.search(r'DEV_([0-9A-F]{4})', gpu_info['InstanceId'], re.I)
    if match:
        device_id = match.group(1).upper()
        final_data['GPU']['modelName'] = gpu_info['FriendlyName']
        final_data['GPU']['isSupported'] = device_id in compatible_data['gpu'][vendor_filter(gpu_info['FriendlyName'])]

def getGPUInfo():
    getGPUandCheckCompatible()
    return final_data["GPU"]
