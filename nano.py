import requests
import os

class Colors:
    HEADER = '\033[95m'  # رنگ بنفش برای هدر
    OKBLUE = '\033[94m'  # رنگ آبی برای اطلاعات
    OKGREEN = '\033[92m' # رنگ سبز برای موفقیت
    WARNING = '\033[93m' # رنگ زرد برای هشدار
    FAIL = '\033[91m'    # رنگ قرمز برای خطا
    ENDC = '\033[0m'     # بازگشت به حالت عادی

def print_header():
    header_length = 63
    title = " WELCOME TO THE FILE MANAGER "
    padding_length = (header_length - len(title)) // 2
    
    print(f"{Colors.HEADER}{'=' * header_length}{Colors.ENDC}")
    print(f"{Colors.OKGREEN}{' ' * padding_length}{title}{' ' * padding_length}{Colors.ENDC}")
    print(f"{Colors.HEADER}{'=' * header_length}{Colors.ENDC}")

def print_status(message):
    print(f"{Colors.OKBLUE}[INFO] {message}{Colors.ENDC}")

def load_data():
    """Load saved links from data.txt"""
    if os.path.exists('data.txt'):
        with open('data.txt', 'r', encoding='utf-8') as file:
            return {line.strip(): line.strip().split('/')[-1] for line in file.readlines()}
    return {}

def save_data(link):
    """Save new link to data.txt"""
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(link + '\n')

def update_file(link, file_name):
    """Fetch and save the content of the file"""
    try:
        response = requests.get(link)

        if response.status_code == 200:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(response.text)  # Directly write the content
            print(f"{Colors.OKGREEN}File '{file_name}' has been successfully created/updated.{Colors.ENDC}")
            return True
        elif response.status_code == 404:
            print(f"{Colors.FAIL}File not found on the server (404). Deleting local file '{file_name}' if it exists.{Colors.ENDC}")
            if os.path.exists(file_name):
                os.remove(file_name)  # Remove the local file if it exists
            return False
        else:
            print(f"{Colors.FAIL}Error retrieving file '{file_name}'. Status code: {response.status_code}.{Colors.ENDC}")
            return False
    
    except requests.exceptions.RequestException as e:
        print(f"{Colors.FAIL}Error sending request: {e}.{Colors.ENDC}")
        return False

def main():
    os.system("clear")
    print_header()
    
    links = load_data()
    
    link = input(f"{Colors.WARNING}Enter the file link (must start with https://appcoders.ir/Browser/DM/): {Colors.ENDC}")
    
    # Validate the link
    if not link.startswith("https://appcoders.ir/Browser/DM/"):
        print(f"{Colors.FAIL}Invalid link!{Colors.ENDC}")
        return
    
    # Extract the file name
    file_name = link.split('/')[-1]

    # Check if the link is already saved
    if link in links:
        existing_file_name = links[link]
        
        # Check if the local file exists
        if os.path.exists(existing_file_name):
            print_status(f"File '{existing_file_name}' already exists in the system.")
            
            # Check for updates
            print_status("Checking for updates...")
            response = requests.get(link)
            if response.status_code == 200:
                new_content = response.text.strip()  # Strip any leading/trailing whitespace
                with open(existing_file_name, 'r', encoding='utf-8') as file:
                    old_content = file.read().strip()
                
                if new_content != old_content:
                    print_status(f"File '{existing_file_name}' has been updated.")
                    update_file(link, existing_file_name)
                else:
                    print_status("No updates found for the existing file.")
            elif response.status_code == 404:
                print(f"{Colors.FAIL}The remote file '{link}' was deleted. Removing local file '{existing_file_name}'.{Colors.ENDC}")
                os.remove(existing_file_name)  # Remove the local file
                del links[link]  # Remove from records
                with open('data.txt', 'w', encoding='utf-8') as file:
                    for saved_link in links.keys():
                        file.write(saved_link + '\n')
            else:
                print_status(f"Error checking for updates. Status code: {response.status_code}")
        
        else:
            print(f"{Colors.WARNING}The local file '{existing_file_name}' was deleted from the system. Removing from records.{Colors.ENDC}")
            del links[link]  # Remove from records if the local file is missing
            with open('data.txt', 'w', encoding='utf-8') as file:
                for saved_link in links.keys():
                    file.write(saved_link + '\n')
    
    else:
        # If it's a new link, load it and create the file.
        save_data(link)
        if update_file(link, file_name):
            print_status(f"New file '{file_name}' has been created.")

if __name__ == "__main__":
    main()
