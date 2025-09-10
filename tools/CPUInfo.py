import cpuinfo
import json

import os, sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

final_data = {
    "CPU": {},
}

codename_map = {
    "intel": {
        (6,60): "Haswell",
        (6,69): "Haswell",
        (6,70): "Haswell",
        (6,71): "Haswell",
        (6,94): "Skylake",
        (6,78): "Broadwell",
        (6,61): "Broadwell",
        (6,85): "Broadwell",
        (6,142): "Kaby Lake",
        (6,158): "Coffee Lake",
        (6,165): "Coffee Lake Refresh",
        (6,166): "Whiskey Lake",
        (6,167): "Amber Lake",
        (6,168): "Comet Lake",
        (6,141): "Kaby Lake",
        (6,140): "Skylake",
        (6,37): "Nehalem",
        (6,44): "Westmere",
        (6,26): "Nehalem-EP",
        (6,46): "Westmere-EX",
        (6,63): "Haswell-E",
        (6,79): "Broadwell-E",
        (6,85): "Broadwell-E",
        (6,106): "Cascade Lake",
        (6,55): "Sandy Bridge-E",
        (6,62): "Ivy Bridge-E",
        (6,45): "Sandy Bridge",
        (6,58): "Ivy Bridge",
        (6,23): "Penryn",
        (6,15): "Core (Yonah)",
        (15,4): "NetBurst (Prescott)",
        (15,6): "NetBurst (Cedar Mill)",
        (15,2): "NetBurst (Northwood)"
    },
    "amd": {
        (23,1): "Zen",
        (23,8): "Zen+",
        (23,17): "Zen+",
        (23,24): "Zen+",
        (23,49): "Zen 2",
        (23,113): "Zen 2",
        (23,96): "Zen 3",
        (25,1): "Zen 3",
        (25,33): "Zen 3",
        (25,97): "Zen 4",
        (25,112): "Zen 4",
        (21,1): "Bulldozer",
        (21,2): "Piledriver",
        (21,48): "Steamroller",
        (21,96): "Excavator",
        (20,1): "Llano (K10.5)",
        (18,1): "Phenom II (K10)",
        (15,72): "Athlon 64 (K8)",
        (15,44): "Opteron (K8)",
        (6,8): "K7 (Athlon XP)"
    }
}

def getCPUandCheckCompatible():
    cpu = cpuinfo.get_cpu_info()
    brand = cpu['brand_raw']
    final_data["CPU"]["modelName"] = brand
    final_data["CPU"]["isSupported"] = True

    cpu_info = cpuinfo.get_cpu_info()
    family = cpu_info.get("family")
    model = cpu_info.get("model")
    brand = cpu_info.get("brand_raw", "Unknown")

    vendor = "intel" if "intel" in brand.lower() else "amd" if "amd" in brand.lower() else None

    if vendor and (family, model) in codename_map[vendor]:
        final_data["CPU"]["codename"] = codename_map[vendor][(family, model)]
        
    with open(resource_path("compatible-dict.json"), "r") as f:
        unsupported_cpu = json.load(f)['unsupported_cpu']

    for uc in unsupported_cpu:
        if uc.lower() in brand.lower():
            final_data["CPU"]["isSupported"] = False
            break

def getCPUInfo():
    getCPUandCheckCompatible()
    return final_data["CPU"]
