# Jarvis-AI-2.0
A modified AI Assistant like Iron-man

# Jarvis Virtual Assistant

Jarvis is a virtual artificial intelligence designed to assist users with various tasks using voice commands. It utilizes several APIs and libraries to provide functionality such as answering questions, retrieving information from Wikipedia, accessing cryptocurrency balances, and performing web searches.

## Features

- **Voice Interaction:** Users can interact with Jarvis using voice commands, enabling hands-free operation.
- **OpenAI Integration:** Jarvis can answer a wide range of questions using the OpenAI GPT-3.5 model, providing informative responses.
- **Wikipedia Search:** Users can ask Jarvis to search Wikipedia for information on specific topics.
- **Cryptocurrency Balance:** Jarvis can retrieve cryptocurrency balances from the Gemini exchange API.
- **Date and Time:** Users can ask Jarvis for the current date and time.
- **Web Browsing:** Jarvis can open web browsers to specific websites upon user request.
- **Speech Recognition:** Jarvis utilizes the SpeechRecognition library to understand and process user speech.
- **Text-to-Speech:** Jarvis utilizes the pyttsx3 library to convert text responses into speech for user interaction.

## Setup

1. **API Keys:** Obtain API keys for OpenAI, Gemini, and GROQ (optional).
2. **Dependencies:** Install the required Python libraries using pip:
    ```
    pip install openai requests wikipedia SpeechRecognition pyttsx3
    ```
3. **Configuration:** Update the API keys in the script with your own keys.
4. **Run:** Execute the script `main.py` to start the virtual assistant.

## Usage

- **Voice Commands:** Speak to Jarvis using voice commands to perform various tasks.
- **Interaction:** Jarvis will respond verbally to user queries and commands, providing relevant information or performing actions.
- **Termination:** To exit the program, say "exit," "bye," "quit," or "close."

## Limitations

- **Internet Connection:** Jarvis requires an active internet connection to access external APIs and perform web searches.
- **API Rate Limits:** Usage of external APIs may be subject to rate limits and restrictions.
- **Accuracy:** Responses provided by Jarvis may not always be accurate or complete, as they rely on external sources and models.

## Contributing

Contributions to Jarvis are welcome! Feel free to submit pull requests for bug fixes, enhancements, or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
