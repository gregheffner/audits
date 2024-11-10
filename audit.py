import os
import subprocess

# Replace with the target IP address or URL
target = "<IP address or URL>"

def run_nmap_scan(target):
    print("Running Nmap scan...")
    nmap_command = f"nmap -sS -sV -O -p- -oN nmap_scan_results.txt {target}"
    subprocess.run(nmap_command, shell=True)
    print("Nmap scan completed. Results saved to nmap_scan_results.txt")

def run_nikto_scan(target):
    print("Running Nikto scan...")
    nikto_command = f"nikto -h {target} -output nikto_scan_results.txt"
    subprocess.run(nikto_command, shell=True)
    print("Nikto scan completed. Results saved to nikto_scan_results.txt")

def start_nessus_service():
    print("Starting Nessus service...")
    subprocess.run("sudo systemctl start nessusd", shell=True)
    print("Nessus service started. Access it at https://localhost:8834")

def main():
    print("Website Security Audit Playbook")
    print("1. Preparation")
    print(f"Target: {target}")
    
    print("\n2. Reconnaissance with Nmap")
    run_nmap_scan(target)
    
    print("\n3. Web Server Scanning with Nikto")
    run_nikto_scan(target)
    
    print("\n4. Vulnerability Scanning with Nessus")
    start_nessus_service()
    print("Please configure and run the Nessus scan manually through the web interface.")
    
    print("\n5. Analysis and Reporting")
    print("Review the scan results from Nmap, Nikto, and Nessus.")
    
    print("\n6. Remediation")
    print("Apply necessary patches, updates, and configuration changes.")
    
    print("\n7. Documentation")
    print("Create a report and share it with relevant stakeholders.")

if __name__ == "__main__":
    main()