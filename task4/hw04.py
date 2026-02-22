def parse_input(user_input):
    """Parse user input into a command and its arguments."""
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


def add_contact(args, contacts):
    """Add a new contact to the contacts dictionary."""
    if len(args) != 2:
        return "Error: give me name and phone please."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Update an existing contact's phone number."""
    if len(args) != 2:
        return "Error: give me name and phone please."
    name, phone = args
    if name not in contacts:
        return f"Error: contact '{name}' not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    """Show the phone number for a given contact name."""
    if len(args) != 1:
        return "Error: give me a name please."
    name = args[0]
    if name not in contacts:
        return f"Error: contact '{name}' not found."
    return contacts[name]


def show_all(contacts):
    """Return all contacts as a formatted string."""
    if not contacts:
        return "No contacts saved."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
