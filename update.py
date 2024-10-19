import os
import time

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def print_header():
    header_length = 63
    title = " WELCOME TO THE TERMINAL SIMULATOR "
    padding_length = (header_length - len(title)) // 2
    
    print(f"{Colors.HEADER}{'=' * header_length}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}{' ' * padding_length}{title}{' ' * padding_length}{Colors.ENDC}")
    print(f"{Colors.HEADER}{'=' * header_length}{Colors.ENDC}")

def print_status(message):
    print(f"{Colors.OKBLUE}[INFO] {message}{Colors.ENDC}")

def check_git_status():
    print_status("Checking Git status...")
    os.system("git status")

def git_pull():
    check_git_status()
    
    print_status("Executing 'git pull origin main'...")
    os.system("git pull origin main")
    
    # Report changes
    report_changes()

def report_changes():
    print_status("Generating report of changes...")
    
    # Get the list of changed files
    changed_files = os.popen("git diff --name-status HEAD@{1} HEAD").read().strip().split("\n")
    
    if not changed_files or changed_files == ['']:
        print(f"{Colors.OKGREEN}No changes detected.{Colors.ENDC}")
        return

    for change in changed_files:
        status, file_name = change.split("\t")
        if status == "A":
            print(f"{Colors.OKGREEN}[ADDED] {file_name}{Colors.ENDC}")
        elif status == "D":
            print(f"{Colors.FAIL}[DELETED] {file_name}{Colors.ENDC}")
        elif status == "M":
            print(f"{Colors.WARNING}[MODIFIED] {file_name}{Colors.ENDC}")

def show_help():
    help_text = """
Available Commands:
- u : Execute 'git pull origin main'
- h : Show this help message
- q : Clear the terminal and exit after a few seconds
"""
    print(help_text)

def clear_and_exit():
    print_status("Clearing the terminal...")
    os.system("clear")
    time.sleep(3)
    print_status("Exiting the terminal simulator.")
    exit()

def main():
    os.system("clear")
    print_header()
    
    while True:
        command = input(f"{Colors.WARNING}Enter command (u for update, h for help, q to clear and exit): {Colors.ENDC}").strip().lower()
        
        if command == 'u':
            git_pull()
        
        elif command == 'h':
            show_help()
        
        elif command == 'q':
            clear_and_exit()
        
        else:
            print(f"{Colors.FAIL}[ERROR] Invalid command! Type 'h' for help.{Colors.ENDC}")

if __name__ == "__main__":
    main()
