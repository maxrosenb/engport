import json

# Load the JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

# Get the user ID for 'westside' from the users dictionary
user_id_map = {user_id: user_data['name'] for user_id, user_data in data['meta']['users'].items()}
userindex = data['meta']['userindex']
westside_id = None

# Find the user ID for 'westside'
for user_id, user_data in data['meta']['users'].items():
    if user_data['name'] == 'westside':
        westside_id = user_id
        break

if westside_id is None:
    print("User 'westside' not found.")
    exit()

# Find the index of 'westside' in userindex
westside_index = userindex.index(westside_id)

# Extract messages for 'westside' by iterating through the 'data' section
user_messages = []

for channel_id, messages in data['data'].items():
    for message_id, message_details in messages.items():
        if message_details['u'] == westside_index:
            if 'm' in message_details:
                user_messages.append(message_details['m'])

# Display the messages
for message in user_messages:
    print(message)

# Optional: Save the extracted messages to a new JSON file
with open('westside_messages.json', 'w') as outfile:
    json.dump(user_messages, outfile, indent=4)
