import cpuinfo
import json

final_data = {
    "CPU": {"modelName": "", "isSupported": True},
}

def getCPUandCheckCompatible():
    cpu = cpuinfo.get_cpu_info()
    brand = cpu['brand_raw']
    final_data["CPU"]["modelName"] = brand
    final_data["CPU"]["isSupported"] = True

    with open("compatible-dict.json", "r") as f:
        unsupported_cpu = json.load(f)['unsupported_cpu']

    for uc in unsupported_cpu:
        if uc.lower() in brand.lower():
            final_data["CPU"]["isSupported"] = False
            break

def getCPUInfo():
    getCPUandCheckCompatible()
    return final_data["CPU"]
