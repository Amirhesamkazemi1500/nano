import os

# Define colors
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header():
    header_length = 63  # Length of the header
    title = "GIT PULL UTILITY"
    padding_length = (header_length - len(title)) // 2  # Calculate padding for center alignment
    
    print(f"{Colors.HEADER}{'=' * header_length}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}{' ' * padding_length}{title}{' ' * padding_length}{Colors.ENDC}")
    
    # If the title length is odd, add an extra space to the right
    if len(title) % 2 != 0:
        print(f"{Colors.OKGREEN}{' ' * (padding_length + 1)}{Colors.ENDC}")
    
    print(f"{Colors.HEADER}{'=' * header_length}{Colors.ENDC}")

def print_status(message):
    print(f"{Colors.OKBLUE}[INFO] {message}{Colors.ENDC}")

def print_report(report_message):
    print(f"{Colors.WARNING}┌─[update@termux]─[~/nano]{Colors.ENDC}")
    print(f"{Colors.WARNING}└──╼ ❯❯❯ {report_message}{Colors.ENDC}")

def main():
    print_header()
    print_status("Executing 'git pull origin main'...")

    # Execute command
    os.system("git pull origin main")

    print_status("Command executed successfully.")
    print_report("Report: Operation completed successfully.")

if __name__ == "__main__":
    main()
