import datetime

class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.messages = [] # Stores messages in a list

    def send_message(self, receiver, content):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = {
            "from": self.username,
            "to": receiver.username,
            "content": content,
            "timestamp": timestamp
        }
        receiver.messages.append(message)

    def view_message(self):
        if not self.messages:
            print("No messages.")
        else:
            print(f"\n{self.username}'s Inbox:")
        for message in self.messages:
            print()


# Authentication System to handle registration and login
class AuthSystem:

    def __init__(self):
        self.users = {}


    def signup(self, username, password):
        if username in self.users:
            print("User name already exists")
        else:
            new_user = User(username, password)
            self.users[username] = new_user
            print(f"User {username} registered successfully!")

    # Method login to a user

    def login(self, username, password):
        if username not in self.users:
            print("User not found! Please register first.")
            return None
        user = self.users[username]
        if user.password == password:
            print(f"User {username} logged in successfully!")
            return user
        else:
            print("Incorrect password!")
            return None

# ChatApplication class to handle user interaction
class ChatApplication:

    def __init__(self):
        self.auth_system = AuthSystem()

    # Method run
    def run(self):
        while True:
            print("\n--- Chat Application---")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Select an option: 9")

            if choice == '1':
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                self.auth_system.signup(username, password)

            elif choice == '2':
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                user = self.auth_system.login(username, password)


            elif choice == '3':
                print("Exiting chat application.")

            else:
                print("Invalid choice. Please try again.")

    def chat_session(self, user):
        while True:
            print(f"\n--- {user.username}'s Chat Session ---")
            print("1. Send a Message")
            print("2. View Inbox")
            print("3. Logout")
            choice = input("Select an option: ")

            if choice == '1':
                receiver_username = input("Enter the receiver's username: ")
                if receiver_username in self.auth_system.users:
                    receiver = self.auth_system.users[receiver_username]
                    message_content = input("Enter your message: ")
                    user.send_message(receiver, message_content)
                else:
                    print("Receiver not found!")
            elif choice == '2':
                user.view_box()
            elif choice == '3':
                print(f"{user.name} logged out")
                break
            else:
                print("Invalid choice. Please try again.")

#  Main block to run the chat application
if __name__ == "__main__":
    chat = ChatApplication()
    chat.run()
