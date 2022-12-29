command = "help"
prev = "NULL"

while True:
    command = input(">")
    if command.upper() == "START":
        if prev == command:
            print("Car already started")
        else:
            print("Car started... Ready to go!")
        prev = command
    elif command.upper() == "STOP":
        if prev == command:
            print("Car already stopped")
        else:
            print("Car stopped.")
        prev = command
    elif command.upper() == "HELP":
        print("Start - to start the car")
        print("Stop - to stop the car")
        print("Quit - to exit")
    elif command.upper() == "QUIT":
        break
    else:
        print("I don't understand that... use help to display commands")
