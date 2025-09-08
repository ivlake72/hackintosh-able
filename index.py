from tools.CPUInfo import getCPUInfo
from tools.GPUInfo import getGPUInfo

cpu_data = getCPUInfo()
gpu_data = getGPUInfo()

final_data = {
    "CPU": cpu_data,
    "GPU": gpu_data
}

print(final_data)
