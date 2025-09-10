import cpuinfo

cpu_info = cpuinfo.get_cpu_info()

family = cpu_info.get("family")
model = cpu_info.get("model")
brand = cpu_info.get("brand_raw")

codename = "Unknown"

# Intel 예시 매핑 (간단 버전)
intel_codename_map = {
    (6, 158): "Coffee Lake",
    (6, 142): "Kaby Lake-R",
    (6, 94): "Skylake",
    (6, 60): "Haswell",
}

if (family, model) in intel_codename_map:
    codename = intel_codename_map[(family, model)]

print(f"CPU: {brand}")
print(f"Codename: {codename}")
