from tools.CPUInfo import getCPUInfo
from tools.GPUInfo import getGPUInfo
from tools.MotherBoardInfo import getMotherBoardInfo

cpu_data = getCPUInfo()
gpu_data = getGPUInfo()
mb_data = getMotherBoardInfo()

final_data = {
    "CPU": cpu_data,
    "GPU": gpu_data,
    "MOTHERBOARD": mb_data
}

print(final_data)
