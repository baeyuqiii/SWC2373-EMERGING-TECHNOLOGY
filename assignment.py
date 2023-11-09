from webexteamssdk import WebexTeamsAPI

# Input Webex token
teams_token = input("\nEnter Your access token : ")
api = WebexTeamsAPI(access_token=teams_token)

# To test connection
def test_connection():
    print("Connecting...")
    webex = api.people.me()
    if webex:
        print("Successful")

# To display user information
def information():
    webex = api.people.me()
    print(f"Display Name: {webex.displayName}")
    print(f"Nickname: {webex.nickName}")
    print(f"Emails: {', '.join(webex.emails)}")

# To list rooms and return them as a list
def listRooms():
    print("\nList of Rooms:")
    rooms = api.rooms.list(max=5)  # List 5 rooms
    roomList = []

    for room in rooms:
        roomList.append(room)
        print(f"{len(roomList)}: {room.title}")

    return roomList

# To display rooms
def displayRoom():
    print("\nList of Rooms:")
    rooms = list(api.rooms.list(max=5))  # List 5 rooms
    roomCount = 0

    for i, room in enumerate(rooms, start=1):
        print(f"Room ID : {room.id}")
        print(f"Room Title : {room.title}")
        print(f"Data Created  : {room.created}")
        print(f"Last Activity : {room.lastActivity}\n")

        roomCount += 1
        if roomCount >= 5:
            break

    return rooms

# To create a room
def createRoom():
    titleRoom = input("\nEnter the title of the new room: ")
    try:
        newRoom = api.rooms.create(title=titleRoom)
        print(f"-{newRoom.title}- (Room ID: {newRoom.id}) has been created successfully.")
    except Exception as e:
        print(f"Failed to create the room. Error: {e}")


# To send a message
def sendMessage():
    rooms = listRooms()
    if rooms:
        roomNumber = input("\nEnter the number of the room to send a message: ")

        try:
            roomNumber = int(roomNumber)
            if 1 <= roomNumber <= len(rooms):
                room = rooms[roomNumber - 1]
                message = input("\nEnter the message that you would like to send : ")
                api.messages.create(room.id, text=message)
                print("\nMessage sent successfully!")
            else:
                print("Invalid room number. Please select a valid room.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("No rooms available. You can create one using option 3.")

# List of options
while True:
    print("\nOptions:")
    print("0: Test Connection")
    print("1: Display Information")
    print("2: Display Rooms")
    print("3: Create Room")
    print("4: Send Message")
    print("5: Exit")

    option = input("Select an option: ")

    if option == "0":
        test_connection()
    elif option == "1":
        information()
    elif option == "2":
        displayRoom()
    elif option == "3":
        createRoom()
    elif option == "4":
        sendMessage()
    elif option == "5":
        print("Exit")
        break
    else:
        print("Invalid option. Please select a valid option.")
