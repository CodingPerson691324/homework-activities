
import os
import platform
import sys
from time import sleep

def shutdown_system():
    system = platform.system().lower()

    print("Initiating shutdown sequence...")
    sleep(1)

    try:
        if system == 'windows':
            os.system('shutdown /s /t 1')
        elif system == 'linux' or system == 'darwin':  # Linux or Mac
            os.system('sudo shutdown -h now')
        else:
            print("Unsupported operating system")
            return False
        return True
    except Exception as e:
        print(f"Error during shutdown: {e}")
        return False

def main():
    while True:
        choice = input("Do you want to shutdown the system? (yes/no): ").lower()

        if choice == 'yes':
            print("System will shutdown in a moment...")
            shutdown_system()
            break
        elif choice == 'no':
            print("Shutdown cancelled")
            break
        else:
            print("Please enter 'yes' or 'no'")

if __name__ == "__main__":
    main()
