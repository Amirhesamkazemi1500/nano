import os

# تعریف رنگ‌ها
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
    print(f"{Colors.HEADER}==================================={Colors.ENDC}")
    print(f"{Colors.OKGREEN}          Git Pull Utility         {Colors.ENDC}")
    print(f"{Colors.HEADER}==================================={Colors.ENDC}")

def print_status(message):
    print(f"{Colors.OKBLUE}[INFO] {message}{Colors.ENDC}")

def main():
    print_header()
    print_status("Executing 'git pull origin main'...")

    # اجرای دستور
    os.system("git pull origin main")

    print_status("Command executed successfully.")

if __name__ == "__main__":
    main()
