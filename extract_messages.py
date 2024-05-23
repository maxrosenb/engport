import json
import argparse

def extract_messages(username, input_file='data.json'):
    # Load the JSON data from a file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Get the user ID for the given username from the users dictionary
    user_id_map = {user_id: user_data['name'] for user_id, user_data in data['meta']['users'].items()}
    userindex = data['meta']['userindex']
    user_id = None

    # Find the user ID for the given username
    for user_id_key, user_data in data['meta']['users'].items():
        if user_data['name'] == username:
            user_id = user_id_key
            break

    if user_id is None:
        print(f"User '{username}' not found.")
        return

    # Find the index of the user in userindex
    user_index = userindex.index(user_id)

    # Extract messages for the user by iterating through the 'data' section
    user_messages = []

    for channel_id, messages in data['data'].items():
        for message_id, message_details in messages.items():
            if message_details['u'] == user_index:
                if 'm' in message_details:
                    user_messages.append(message_details['m'])

    # Display the messages
    for message in user_messages:
        print(message)

    # Save the extracted messages to a new JSON file named after the username
    output_file = f"{username}_messages.json"
    with open(output_file, 'w') as outfile:
        json.dump(user_messages, outfile, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Extract messages for a specific user from a JSON file.')
    parser.add_argument('username', type=str, help='Username to extract messages for')

    args = parser.parse_args()
    extract_messages(args.username)

if __name__ == '__main__':
    main()
