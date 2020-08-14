command = ""
started = False
while True:
    command = input("> ")
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("Start - to start the car \nStop - to stop the car\nQuit - to exit")
    elif command == "quit":
        print("Thank you for playing car game")
        break
    else:
        print("Sorry, I don't understand that")