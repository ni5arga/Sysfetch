import platform
import psutil
from colorama import init, Fore

init(autoreset=True)

def get_system_information():
    system_info = {
        'System': platform.system(),
        'Node Name': platform.node(),
        'Release': platform.release(),
        'Version': platform.version(),
        'Machine': platform.machine(),
        'Processor': platform.processor(),
        'CPU Cores': psutil.cpu_count(logical=False),
        'Logical CPUs': psutil.cpu_count(logical=True),
        'RAM (Total)': round(psutil.virtual_memory().total / (1024 ** 3), 2),
        'RAM (Used)': round(psutil.virtual_memory().used / (1024 ** 3), 2),
        'RAM (Free)': round(psutil.virtual_memory().free / (1024 ** 3), 2),
    }

    try:
        disk_info = psutil.disk_usage('/')
        system_info['Disk Space (Total)'] = round(disk_info.total / (1024 ** 3), 2)
        system_info['Disk Space (Used)'] = round(disk_info.used / (1024 ** 3), 2)
        system_info['Disk Space (Free)'] = round(disk_info.free / (1024 ** 3), 2)
    except Exception as e:
        print(f"Error fetching disk information: {e}")

    return system_info

def get_network_information():
    network_info = {}
    try:
        net_io = psutil.net_io_counters()
        network_info['Bytes Sent'] = net_io.bytes_sent
        network_info['Bytes Received'] = net_io.bytes_recv
    except Exception as e:
        print(f"Error fetching network information: {e}")

    return network_info

def get_battery_information():
    battery_info = {}
    try:
        battery = psutil.sensors_battery()
        battery_info['Percentage'] = battery.percent
        battery_info['Plugged'] = "Yes" if battery.power_plugged else "No"
    except Exception as e:
        print(f"Error fetching battery information: {e}")

    return battery_info

def get_process_information():
    process_info = {}
    try:
        processes = psutil.process_iter()
        process_count = sum(1 for _ in processes)
        process_info['Current Processes'] = process_count
    except Exception as e:
        print(f"Error fetching process information: {e}")

    return process_info

def display_information(category_name, info_dict):
    print(Fore.CYAN + f"{category_name} Information:")
    for key, value in info_dict.items():
        print(f"{Fore.BLUE}{key}:{Fore.RESET} {value}")

if __name__ == "__main__":
    system_info = get_system_information()
    network_info = get_network_information()
    battery_info = get_battery_information()
    process_info = get_process_information()

    display_information("System", system_info)
    display_information("Network", network_info)
    display_information("Battery", battery_info)
    display_information("Process", process_info)
