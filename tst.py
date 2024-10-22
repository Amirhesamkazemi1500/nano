import os

def print_header():
    header = """
\033[1;36m========================================
           LINUX TERMINAL CONNECTOR
========================================\033[0m
"""
    print(header)

def main():
    print_header()
    print("\033[1;32mType 'exit' to quit.\033[0m")

    while True:
        command = input("\033[1;34m>>> \033[0m")  # Prompt with blue color
        if command.lower() == 'exit':
            print("\033[1;31mExiting the terminal...\033[0m")
            break
        else:
            try:
                output = os.popen(command).read()
                if output:
                    print(output)
                else:
                    print("\033[1;33mNo output.\033[0m")  # Yellow color for no output
            except Exception as e:
                print(f"\033[1;31mError: {e}\033[0m")  # Red color for errors

if __name__ == "__main__":
    main()
