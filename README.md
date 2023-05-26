# Linux Package and Python Library List Script

This script allows you to list the installed Linux packages and Python libraries on a CentOS or Debian system. It provides information such as package versions and installation dates.

## Prerequisites

- Python 3.x
- `pip` package manager (for listing Python libraries)
- CentOS or Debian Linux distribution

## Usage

1. Make sure you have Python 3.x installed on your CentOS or Debian system.

2. Install the required packages by running the following command:


3. Save the script to a file, for example, `package_list.py`.

4. Open a terminal and navigate to the directory where the script is saved.

5. Run the script using the following command:
python3 name_of_the_script.py

6. The script will detect the Linux distribution and list the installed Linux packages and Python libraries accordingly.

## Limitations

- The script assumes that you have the necessary permissions to access the required system files and execute commands.
- The availability of package version and installation date information may vary depending on the Linux distribution and system configuration.
- The script relies on external commands (`rpm`, `dpkg-query`, `pip`) and may require administrative privileges to execute successfully.




