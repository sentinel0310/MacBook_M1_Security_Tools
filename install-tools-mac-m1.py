import subprocess

# List of 50 security tools to install - https://github.com/sentinel0310/MacBook_M1_Security_Tools
tools = [
    'nmap',
    'netcat',
    'tcpdump',
    'wireshark',
    'hashcat',
    'JohnTheRipper',
    'hydra',
    'sqlmap',
    'metasploit',
    'aircrack-ng',
    'bettercap',
    'burpsuite',
    'maltego',
    'radare2',
    'Ghidra',
    'IDA Pro',
    'volatility',
    'Autopsy',
    'Sleuth Kit',
    'WireGuard',
    'OpenVPN',
    'Tor',
    'dnsenum',
    'theHarvester',
    'Recon-ng',
    'Sublist3r',
    'sqlninja',
    'Dirbuster',
    'Wfuzz',
    'Nikto',
    'Skipfish',
    'Arachni',
    'Gobuster',
    'Aquatone',
    'masscan',
    'nmap',
    'CrackMapExec',
    'Empire',
    'Responder',
    'mimikatz',
    'Bloodhound',
    'PowerSploit',
    'PowerView',
    'Evil-WinRM',
    'Pwsh-Netcat',
    'mitmproxy',
    'TShark',
    'Snort',
    'Security Onion',
]

# Install Homebrew if not installed
if not subprocess.run(['which', 'brew'], stdout=subprocess.PIPE).stdout:
    subprocess.run(['/bin/bash', '-c', "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"])

# Check if the tools are already installed
installed_tools = subprocess.run(['brew', 'list'], stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines()
for tool in tools:
    if tool in installed_tools:
        print(f"{tool} is already installed.")
        continue

    # Install the tool if it's not installed
    try:
        subprocess.run(['brew', 'install', tool], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {tool}: {e}")
