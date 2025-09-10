from tools.CPUInfo import getCPUInfo
from tools.GPUInfo import getGPUInfo
from tools.MotherBoardInfo import getMotherBoardInfo
from tools.AudioChipsetInfo import getAudioInfo

cpu_data = getCPUInfo()
gpu_data = getGPUInfo()
mb_data = getMotherBoardInfo()
ac_data = getAudioInfo()

final_data = {
    "CPU": cpu_data,
    "GPU": gpu_data,
    "MOTHERBOARD": mb_data,
    "AUDIO": ac_data
}

print(final_data)
