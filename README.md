# Speech Recognition and Translation

This is a Python script that listens to your voice commands and executes programs based on the commands. It also has the ability to copy and paste text from the clipboard and translate Polish words to English.

## Requirements

To run this script, you need to have the following Python libraries installed:

-   pyttsx3==2.90
-   SpeechRecognition==3.8.1
-   pyperclip==1.8.2
-   pyautogui==0.9.52
-   googletrans==4.0.0-rc1

You can install these libraries using the following command:
`pip install -r requirements.txt`

## Usage

To use this script, you need to run the `speech_recognition.py` file. Before running the script, make sure that your microphone is connected and working properly.

When the script is running, you can give voice commands to execute programs or paste text from the clipboard. If you say the word "tłumacz" followed by a Polish word, the script will translate the word to English and read out the translation.

To stop the script, say the word "stop".

## License

This script is licensed under the MIT License. Feel free to use and modify it for your own purposes.
