import json

# Load the JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

# Get the user ID for 'itsfael' from the users dictionary
user_id_map = {user_id: user_data['name'] for user_id, user_data in data['meta']['users'].items()}
userindex = data['meta']['userindex']
itsfael_id = None

# Find the user ID for 'itsfael'
for user_id, user_data in data['meta']['users'].items():
    if user_data['name'] == 'itsfael':
        itsfael_id = user_id
        break

if itsfael_id is None:
    print("User 'itsfael' not found.")
    exit()

# Find the index of 'itsfael' in userindex
itsfael_index = userindex.index(itsfael_id)

# Extract messages for 'itsfael' by iterating through the 'data' section
user_messages = []

for channel_id, messages in data['data'].items():
    for message_id, message_details in messages.items():
        if message_details['u'] == itsfael_index:
            if 'm' in message_details:
                user_messages.append(message_details['m'])

# Display the messages
for message in user_messages:
    print(message)

# Optional: Save the extracted messages to a new JSON file
with open('itsfael_messages.json', 'w') as outfile:
    json.dump(user_messages, outfile, indent=4)
