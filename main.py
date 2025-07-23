import os
import getpass
import platform
from datetime import datetime

def get_system_info():
    info = {
        "Username": getpass.getuser(),
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Date & Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return info

def log_info(info, filename="system_log.txt"):
    with open(filename, "a") as file:
        file.write("---- System Info Logged ----\n")
        for key, value in info.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")

def main():
    system_info = get_system_info()
    log_info(system_info)
    print("System information logged successfully.")

if __name__ == "__main__":
    main()
