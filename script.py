import subprocess

def get_installed_packages():
    package_list = []
    distro = get_linux_distro()

    if distro == "centos":
        command = ["rpm", "-qa", "--queryformat", "%{NAME} %{VERSION} %{INSTALLTIME}\n"]
    elif distro == "debian":
        command = ["dpkg-query", "-W", "-f='${Package} ${Version} ${Install-Date}\n'"]
    else:
        print("Unsupported Linux distribution.")
        return package_list

    try:
        output = subprocess.check_output(command).decode("utf-8")
        lines = output.split("\n")

        if distro == "centos":
            for line in lines:
                package_info = line.split()
                if len(package_info) >= 3:
                    package_name = package_info[0]
                    package_version = package_info[1]
                    package_install_date = package_info[2]
                    package_list.append((package_name, package_version, package_install_date))
        elif distro == "debian":
            for line in lines:
                package_info = line.split()
                if len(package_info) >= 3:
                    package_name = package_info[0]
                    package_version = package_info[1]
                    package_install_date = package_info[2]
                    package_list.append((package_name, package_version, package_install_date))
        
        return package_list

    except subprocess.CalledProcessError:
        print("Error occurred while fetching the package list.")
        return package_list


def get_installed_libraries():
    library_list = []

    try:
        output = subprocess.check_output(["pip", "list"]).decode("utf-8")
        lines = output.split("\n")[2:-1]

        for line in lines:
            package_info = line.split()
            if len(package_info) >= 2:
                package_name = package_info[0]
                package_version = package_info[1]
                library_list.append((package_name, package_version))
        
        return library_list

    except subprocess.CalledProcessError:
        print("Error occurred while fetching the library list.")
        return library_list


def get_linux_distro():
    try:
        output = subprocess.check_output(["lsb_release", "-si"]).decode("utf-8").strip()
        return output.lower()

    except subprocess.CalledProcessError:
        print("Error occurred while determining Linux distribution.")
        return None


if __name__ == "__main__":
    packages = get_installed_packages()
    libraries = get_installed_libraries()

    print("Installed Packages:")
    for package in packages:
        print(f"{package[0]} ({package[1]}) - Installed on {package[2]}")

    print("\nInstalled Python Libraries:")
    for library in libraries:
        print(f"{library[0]} ({library[1]})")
