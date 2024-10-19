import os
import shutil
import time

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

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the program header."""
    width = shutil.get_terminal_size().columns
    print(f"{Colors.HEADER}{'=' * width}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}{' ' * ((width - 30) // 2)}Git Pull Utility - Version 1.0{' ' * ((width - 30) // 2)}{Colors.ENDC}")
    print(f"{Colors.HEADER}{'=' * width}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}{' ' * ((width - 30) // 2)}-------------------------------{' ' * ((width - 30) // 2)}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}{' ' * ((width - 30) // 2)}       Your Git Assistant        {' ' * ((width - 30) // 2)}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}{' ' * ((width - 30) // 2)}-------------------------------{' ' * ((width - 30) // 2)}{Colors.ENDC}")
    print(f"{Colors.HEADER}{'=' * width}{Colors.ENDC}")

def print_status(message):
    """Print status messages."""
    print(f"{Colors.OKBLUE}[INFO] {message}{Colors.ENDC}")

def print_report(report):
    """Print the report in a formatted way."""
    print(f"\n{Colors.BOLD}{Colors.UNDERLINE}Report:{Colors.ENDC}")
    print(f"{Colors.OKGREEN}{report}{Colors.ENDC}")

def main():
    clear_screen()
    print_header()
    
    print_status("Executing 'git pull origin main'...")
    
    # Execute the command and capture the output
    result = os.popen("git pull origin main").read()
    
    time.sleep(1)  # Slight delay for better user experience
    print_status("Command executed successfully.")
    
    # Display the report
    print_report(result)

if __name__ == "__main__":
    main()
