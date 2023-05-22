import pyautogui

# Function to create a new macro

def create_macro():
    macro_name = input("Enter macro name: ")
    macro_steps = []

    print("Enter macro steps (press 'q' to finish):")
    while True:
        step = input("> ")
        if step.lower() == 'q':
            break
        macro_steps.append(step)

    print("Creating macro...")
    pyautogui.PAUSE = 1
    pyautogui.hotkey('ctrl', 'alt', 'shift', 'r')  

    for step in macro_steps:
        pyautogui.typewrite(step) 
        pyautogui.press('enter')  

    pyautogui.hotkey('ctrl', 'alt', 'shift', 'r')

    print(f"Macro '{macro_name}' created successfully.")

# Menu

while True:
    print("Macro Creation Script")
    print("1. Create Macro")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        create_macro()
    elif choice == '2':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

    print()