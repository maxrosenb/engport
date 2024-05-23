import json

# Load the JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

# Get the user ID for 'mangoingp' from the users dictionary
user_id_map = {user_id: user_data['name'] for user_id, user_data in data['meta']['users'].items()}
userindex = data['meta']['userindex']
mangoingp_id = '608685586630311946'

# Find the index of 'mangoingp' in userindex
mangoingp_index = userindex.index(mangoingp_id)

# Extract messages for 'mangoingp' by iterating through the 'data' section
user_messages = []

for channel_id, messages in data['data'].items():
    for message_id, message_details in messages.items():
        if message_details['u'] == mangoingp_index:
            if 'm' in message_details:
                user_messages.append(message_details['m'])

# Display the messages
for message in user_messages:
    print(message)

# Optional: Save the extracted messages to a new JSON file
with open('mangoingp_messages.json', 'w') as outfile:
    json.dump(user_messages, outfile, indent=4)