# Discord Message Extractor and Language Analyzer

This project provides a script to extract messages from a Discord chat log in JSON format for a specific user and analyze the language distribution of those messages (English vs. Portuguese).

## Features

- Extract messages for a specified username from a JSON file.
- Save the extracted messages to a JSON file named after the username.
- Analyze the language distribution of the messages.
- Print the percentage of messages in English and Portuguese.

## Requirements

- Python 3.x
- `langdetect` library

## Installation

1. Clone the repository or download the script file.

2. Install the required Python package:
    ```sh
    pip install langdetect
    ```

## Usage

To run the script, use the following command:

```sh
python extract_and_analyze.py <username>
