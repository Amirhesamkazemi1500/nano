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
        print(f"{Colors.OKGREEN} {' ' * (padding_length + 1)}{Colors.ENDC}")
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
    main()}║{' ' * title_padding}{title}{' ' * title_padding}║{Colors.ENDC}")
    
    # Version with a border
    print(f"{Colors.OKGREEN}║{' ' * version_padding}{version}{' ' * version_padding}║{Colors.ENDC}")

    print(f"{Colors.HEADER}╚{'═' * (width - 2)}╝{Colors.ENDC}")
    
def print_status(message):
    """Print status messages."""
    print(f"{Colors.OKBLUE}[INFO] {message}{Colors.ENDC}")

def print_report(report):
    """Print the report in a formatted way."""
    print(f"\n{Colors.BOLD}{Colors.UNDERLINE}Changes Detected:{Colors.ENDC}")
    for line in report:
        print(f"  • {line}")

def check_git_changes():
    """Check for changes in the git repository."""
    changes = os.popen("git status --porcelain").readlines()
    
    report = []
    
    for change in changes:
        if change.startswith('A '):  # Added file
            filename = change[3:].strip()
            report.append(f"{Colors.OKGREEN}A new file named: {filename}{Colors.ENDC}")
        elif change.startswith('D '):  # Deleted file
            filename = change[3:].strip()
            report.append(f"{Colors.FAIL}The file with the name was deleted: {filename}{Colors.ENDC}")
        elif change.startswith('M '):  # Modified file
            filename = change[3:].strip()
            report.append(f"{Colors.OKBLUE}The file was modified: {filename}{Colors.ENDC}")

    return report

def main():
    clear_screen()
    
    print_header()
    
    print_status("Executing 'git pull origin main'...")
    
    # Execute the command and capture the output
    result = os.popen("git pull origin main").read()
    
    time.sleep(1)  # Slight delay for better user experience
    print_status("Command executed successfully.")
    
    # Display the report of changes detected in the repository
    changes_report = check_git_changes()
    
    if changes_report:
        print_report(changes_report)
        print(f"\n{Colors.BOLD}{Colors.WARNING}Please review the changes above!{Colors.ENDC}")
        
        user_input = input(f"{Colors.OKBLUE}Would you like to see detailed git status? (y/n): {Colors.ENDC}")
        if user_input.lower() == 'y':
            detailed_status = os.popen("git status").read()
            print(f"\n{Colors.BOLD}{detailed_status}{Colors.ENDC}")
            
        else:
            print(f"{Colors.OKBLUE}Exiting... Have a great day!{Colors.ENDC}")
            
    else:
        print(f"{Colors.OKBLUE}No changes detected.{Colors.ENDC}")

if __name__ == "__main__":
    main()
