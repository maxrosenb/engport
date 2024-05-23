import json

# Load the JSON data from a file
with open('data.json', 'r') as file:
    data = json.load(file)

# Get the user ID for 'birdaum' from the users dictionary
user_id_map = {user_id: user_data['name'] for user_id, user_data in data['meta']['users'].items()}
userindex = data['meta']['userindex']
birdaum_id = None

# Find the user ID for 'birdaum'
for user_id, user_data in data['meta']['users'].items():
    if user_data['name'] == 'birdaum':
        birdaum_id = user_id
        break

if birdaum_id is None:
    print("User 'birdaum' not found.")
    exit()

# Find the index of 'birdaum' in userindex
birdaum_index = userindex.index(birdaum_id)

# Extract messages for 'birdaum' by iterating through the 'data' section
user_messages = []

for channel_id, messages in data['data'].items():
    for message_id, message_details in messages.items():
        if message_details['u'] == birdaum_index:
            if 'm' in message_details:
                user_messages.append(message_details['m'])

# Display the number of messages
print(f"Total number of messages sent by 'birdaum': {len(user_messages)}")



# Optional: Save the extracted messages to a new JSON file
with open('birdaum_messages.json', 'w') as outfile:
    json.dump(user_messages, outfile, indent=4)
