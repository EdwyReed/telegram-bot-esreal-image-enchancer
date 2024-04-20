# Telegram `nightmareai/real-esrgan` Image Enhancement Bot

## Overview
This project is a Telegram bot designed to enhance images sent by users. Utilizing the Replicate API, the bot applies sophisticated image processing techniques to improve image quality. Built with Pyrogram, it supports asynchronous operations ensuring efficient handling of user requests.

## Features
- Image enhancement using Replicate API (https://replicate.com/nightmareai/real-esrgan).
- Support for multiple user images.
- Base64 encoding for secure image transfer.
- Environment-based configuration for sensitive data.
- Access control to restrict the bot usage to authorized users only.

## Prerequisites
- Python 3.10 or newer.
- A Telegram API key and a bot token from BotFather.
- An account with Replicate and access to their API.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/EdwyReed/telegram-bot-esreal-image-enchancer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd telegram-bot-esreal-image-enchancer
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
1. Create a `.env` file in the root directory with the following contents:
   ```
   API_ID=your_telegram_api_id
   API_HASH=your_telegram_api_hash
   BOT_TOKEN=your_bot_token
   ALLOWED_USER_IDS=comma_separated_list_of_user_ids
   ```
2. Replace `your_telegram_api_id`, `your_telegram_api_hash`, `your_bot_token`, and `comma_separated_list_of_user_ids` with your actual data.

## Usage
Run the bot using the following command:
```bash
python bot.py
```

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t telegram-bot .
   ```
2. Run the bot in a Docker container:
   ```bash
   docker run -d --name my-telegram-bot telegram-bot
   ```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
