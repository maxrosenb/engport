import json
import argparse
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

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
        return []

    # Find the index of the user in userindex
    user_index = userindex.index(user_id)

    # Extract messages for the user by iterating through the 'data' section
    user_messages = []

    for channel_id, messages in data['data'].items():
        for message_id, message_details in messages.items():
            if message_details['u'] == user_index:
                if 'm' in message_details:
                    user_messages.append(message_details['m'])

    # Save the extracted messages to a new JSON file named after the username
    output_file = f"{username}_messages.json"
    with open(output_file, 'w') as outfile:
        json.dump(user_messages, outfile, indent=4)
    
    return user_messages

def detect_language_distribution(messages):
    english_count = 0
    portuguese_count = 0

    for message in messages:
        try:
            lang = detect(message)
            if lang == 'en':
                english_count += 1
            elif lang == 'pt':
                portuguese_count += 1
        except LangDetectException:
            # Ignore messages where language detection fails
            pass

    # Calculate the percentages excluding other languages
    total_valid_messages = english_count + portuguese_count
    if total_valid_messages > 0:
        english_percent = (english_count / total_valid_messages) * 100
        portuguese_percent = (portuguese_count / total_valid_messages) * 100
    else:
        english_percent = portuguese_percent = 0

    return english_percent, portuguese_percent

def main():
    parser = argparse.ArgumentParser(description='Extract messages for a specific user from a JSON file and analyze language distribution.')
    parser.add_argument('username', type=str, help='Username to extract messages for')

    args = parser.parse_args()
    user_messages = extract_messages(args.username)

    if user_messages:
        english_percent, portuguese_percent = detect_language_distribution(user_messages)
        print(f"Percentage of {args.username}'s messages in English vs. Portuguese:")
        print(f"English: {english_percent:.2f}%")
        print(f"Portuguese: {portuguese_percent:.2f}%")

if __name__ == '__main__':
    main()
