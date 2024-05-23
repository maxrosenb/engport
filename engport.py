import json
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

# Load the messages from the previously saved JSON file
with open('birdaum_messages.json', 'r') as file:
    user_messages = json.load(file)

# Initialize counters for English and Portuguese messages
english_count = 0
portuguese_count = 0

# Detect the language of each message
for message in user_messages:
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

# Print the results
print("Percentage of birdaum's messages in English vs. Portuguese:")
print(f"English: {english_percent:.2f}%")
print(f"Portuguese: {portuguese_percent:.2f}%")