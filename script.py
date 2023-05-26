import os
from datetime import datetime

# Function to list installed Linux packages with their versions and installation dates
def list_linux_centos_packages():
    os.system('rpm -qa --queryformat ')

def list_linux_debian_packages():
    os.system('dpkg-query -l | head ')


# Function to list installed Python libraries with their versions
def list_python_libraries():
    os.system('pip freeze')

# Get formatted date from UNIX timestamp
def get_formatted_date(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Check Linux distribution and list installed packages
def check_linux_distribution():
    with open('/etc/os-release', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('ID=centos'):
                print("List of Linux packages installed on CentOS:")
                list_linux_centos_packages()
                break
            elif line.startswith('ID=ubuntu'):
                print("List of Linux packages installed on Debian:")
                list_linux_debian_packages()
                break
        else:
            print("Unsupported Linux distribution.")

# Call the function to check Linux distribution and list installed packages
check_linux_distribution()

# List installed Python libraries with their versions
print("List of installed Python libraries:")
list_python_libraries()
