  main()
import os
import shutil
import time

# Define colors
class Colors:
    HEADER = '\033[95m'   # Magenta
    OKBLUE = '\033[94m'   # Blue
    OKGREEN = '\033[92m'  # Green
    WARNING = '\033[93m'  # Yellow
    FAIL = '\033[91m'     # Red
    ENDC = '\033[0m'      # Reset to default
    BOLD = '\033[1m'      # Bold text
    UNDERLINE = '\033[4m' # Underlined text

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the program header with enhanced graphics."""
    width = shutil.get_terminal_size().columns
    title = " Git Pull Utility "
    version = " Version 2.0 "
    
    # Calculate padding for centering the title and version
    title_padding = (width - len(title) - 2) // 2
    version_padding = (width - len(version) - 2) // 2

    # Terminal prompt style header
    print(f"{Colors.HEADER}┌─[Update@termux]─[~]{Colors.ENDC}")
    
    # Create a structured header with proper alignment
    print(f"{Colors.HEADER}╔{'═' * (width - 2)}╗{Colors.ENDC}")
    
    # Title with a border
    print(f"{Colors.OKGREEN}║{' ' * title_padding}{title}{' ' * title_padding}║{Colors.ENDC}")
    
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
