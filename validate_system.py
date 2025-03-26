import subprocess
import json
import platform

def get_system_specs():
    specs = {
        "nvidia_smi": subprocess.getoutput("nvidia-smi"),
        "nvcc_version": subprocess.getoutput("nvcc --version"),
        "storage": subprocess.getoutput("df -h"),
        "os": subprocess.getoutput("lsb_release -a"),
        "kernel": subprocess.getoutput("uname -r"),
        "python": platform.python_version()
    }
    return specs

if __name__ == "__main__":
    specs = get_system_specs()
    print(json.dumps(specs, indent=2))
