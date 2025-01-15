# OpenAI-Powered Applications

This repository showcases three distinct applications that utilize OpenAI's powerful APIs to deliver advanced AI functionalities. Each application is built with a specific use case in mind, leveraging Flask, AIogram, and OpenAI services such as ChatGPT, Whisper, and DALL-E.

---

## Table of Contents

- [Application 1: Multilingual Audio Translator](#application-1-multilingual-audio-translator)
- [Application 2: Image Generation Bot](#application-2-image-generation-bot)
- [Application 3: Telegram Bots](#application-3-telegram-bots)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Application 1: Multilingual Audio Translator

### Overview
This Flask application accepts audio files, transcribes the content using OpenAI's Whisper API, and translates the transcription into a specified language using ChatGPT.

### Features
- Upload audio files directly from the web interface.
- Real-time transcription and translation.
- Supports multiple languages for translation.

### Usage Example
1. Upload an audio file (e.g., `Recording.mp3`).
2. Specify the target language for translation.
3. Get the translated output via ChatGPT.

---

## Application 2: Image Generation Bot

### Overview
This Flask application allows users to generate AI-crafted images based on a text prompt using OpenAI's DALL-E API.

### Features
- Interactive web interface for inputting prompts.
- Generates 5 unique images per prompt in 256x256 resolution.
- View and download generated images.

### Usage Example
- Input a text prompt like `a futuristic cityscape at sunset`.
- The app returns 5 AI-generated images.

---

## Application 3: Telegram Bots

### Overview
Two Telegram bots built using the AIogram library, each with unique functionality.

1. **ChatGPT-Powered Assistant**
   - Provides intelligent responses to user inputs.
   - Supports command-based features such as `/start`, `/clear`, and `/help`.
   - Maintains conversation history for context-aware replies.

2. **Echo Bot**
   - A simple bot that echoes user messages.
   - Lightweight and efficient.

### Features
- Context-aware responses for better engagement (ChatGPT Bot).
- Clear and reset conversation history.
- Easy-to-use commands for better interaction.

### Usage Example
- **ChatGPT Bot**:
  - Start the bot with `/start`.
  - Clear the context with `/clear`.
  - Chat with the bot and receive intelligent, context-aware replies.
- **Echo Bot**:
  - Start the bot and send any message to receive an echo.

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/openai-powered-apps.git
   cd openai-powered-apps
   ```
1. **Clone the repository:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Install dependencies:**
   ```bash
   git clone https://github.com/yourusername/openai-powered-apps.git
   cd openai-powered-apps
   ```
3. **Set environment variables: Create a .env file with the following:**
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   ```
4. **Run the applications:**
- For Flask apps:
   ```bash
   python app1.py  # Multilingual Audio Translator
   python app2.py  # Image Generation Bot
   ```
- For Telegram bots:
   ```bash
   python telegram_bot1.py  # ChatGPT Bot
   python telegram_bot2.py  # Echo Bot
   ```

## Usage
### Flask Applications
- Access the web interface at http://localhost:8080.
- Use the provided forms to interact with the applications.
### Telegram Bots
- Deploy the bots and interact with them on Telegram using their respective commands.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- OpenAI for providing cutting-edge APIs.
- Flask for web application development.
- AIogram for Telegram bot integration.

## Created with ❤️ by Tanvir Ahmed.
   ```bash
   This `README.md` provides a comprehensive overview of your project, including the purpose of each application, installation instructions, and usage examples. Replace placeholders like repository URLs and API keys with actual values to complete the setup.
   ```

