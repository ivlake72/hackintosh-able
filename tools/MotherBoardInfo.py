import subprocess
import json

import os, sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

final_data = {
    "MOTHERBOARD": {},
}

def getMotherboardInfo():
    cmd = 'powershell -Command "Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer, Product | ConvertTo-Json -Compress"'
    output = subprocess.check_output(cmd, shell=True, text=True)
    mb_info = json.loads(output)

    if isinstance(mb_info, list):
        mb_info = mb_info[0]
    mb = mb_info.get("Product", "").strip()

    final_data['MOTHERBOARD']['modelName'] = mb_info.get("Product", "").strip()

    return mb

def is_unsupported(model, unsupported_list):
    for keyword in unsupported_list:
        if keyword.lower() in model.lower():
            return True
    return False

def checkCompatible():
    with open(resource_path("compatible-dict.json"), "r", encoding="utf-8") as f:
        data = json.load(f)
        unsupported_list = data["unsupported_motherboard"]

        model = getMotherboardInfo()

        if is_unsupported(model, unsupported_list):
            final_data['MOTHERBOARD']['isSupported'] = False
        else:
            final_data['MOTHERBOARD']['isSupported'] = True


def getMotherBoardInfo():
    checkCompatible()
    return final_data["MOTHERBOARD"]