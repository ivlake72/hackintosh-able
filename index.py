import subprocess
import re
import json
import cpuinfo

gpuCheckCmd = (
    'powershell -Command "Get-PnpDevice -Class Display | '
    'Select-Object -Property InstanceId, FriendlyName | ConvertTo-Json"'
)

final_data = {
    "GPU": {"modelName": "", "isSupported": False},
    "CPU": {"modelName": "", "isSupported": True},
}

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

    with open("compatible-dict.json", "r") as f:
        compatible_data = json.loads(f.read())

        match = re.search(r'DEV_([0-9A-F]{4})', gpu_info['InstanceId'], re.I)
        if match:
            device_id = match.group(1).upper()
            final_data['GPU']['modelName'] = gpu_info['FriendlyName']
            final_data['GPU']['isSupported'] = device_id in compatible_data['gpu'][vendor_filter(gpu_info['FriendlyName'])]

def getCPUandCheckCompatible():
    cpu = cpuinfo.get_cpu_info()
    brand = cpu['brand_raw']
    final_data["CPU"]["modelName"] = brand
    final_data["CPU"]["isSupported"] = True 

    with open("compatible-dict.json", "r") as f: 
        unsupported_cpu = json.loads(f.read())['unsupported_cpu']
    
        for uc in unsupported_cpu:
            if uc.lower() in brand.lower():
                final_data["CPU"]["isSupported"] = False
                break

def getInfo():
    getGPUandCheckCompatible() # GPU
    getCPUandCheckCompatible() # CPU

getInfo()
print(final_data)