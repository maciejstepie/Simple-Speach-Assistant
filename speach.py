import speech_recognition as sr
import pyperclip
import pyautogui
import json
import subprocess
from translator import translate

# Load commands and their actions from file
def load_commands():
	with open('commands.json', 'r') as f:
		commands = json.load(f)
	print("Reloaded commands file.")
	return commands

def print_commands(commands):
	print("Here's a list of available commands:")
	for key, value in commands.items():
		print(f"{key}: {value}")

def execute_program(speech):
	if speech.split()[1].lower() in commands:
			program = commands[speech.split()[1].lower()]
			try:
				subprocess.Popen(program)
				print("Executing program: " + program)
			except OSError:
				print("Failed to execute program: " + program)
	else:
		print("Can't find program: " + speech.split()[1].lower())
		print_commands()

# declare global commands variable
global commands
commands = load_commands()

# create instance of recognizer class
r = sr.Recognizer()

def paste_text(text, speech):
	pyperclip.copy(text)
	pyautogui.hotkey("ctrl", "v")
	if speech.split()[-1].lower() == "enter":
		pyautogui.write(['enter'])
		print("Enter key pressed.")

def process_speech(speech):
	if speech.split()[0].lower() == "stop":
		print("Stopping...")
		return False

	if speech.split()[0].lower() == "enter":
		pyautogui.write(['enter'])
		print("Enter key pressed.")
		return True

	# check if first word is "wklej"
	if speech.split()[0].lower() == "wklej":
		if len(speech.split()) > 1 and speech.split()[1].lower() == "tłumacz":
			text_to_translate = " ".join(speech.split()[2:])					
			translated_text = translate(text_to_translate)					
			paste_text(translated_text, speech)					
			print("Translated text pasted from clipboard.")
		else:
			text_to_paste = " ".join(speech.split()[1:])
			paste_text(text_to_paste, speech)
			print("Text pasted from clipboard.")

	# Reload commands file
	if "przeładuj komendy" in speech:
		load_commands()

	# Execute program based on command
	if speech.split()[0].lower() == "uruchom":
		execute_program(speech)

	return True

# use default microphone as source
with sr.Microphone() as source:
	print("Listening...")
	r.pause_threshold = 0.5 # seconds of non-speaking audio before a phrase is considered complete
	r.adjust_for_ambient_noise(source) # remove background noise
	while True:
		# listen for audio from the user
		audio = r.listen(source)

		# recognize speech using Google Speech Recognition
		try:
			speech = r.recognize_google(audio, language='pl-PL')
			#speech = r.recognize_sphinx(audio, language="pl-PL")
			print("You said: " + speech)
			if not process_speech(speech):
				break

		except sr.UnknownValueError:
			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))

print("Program stopped.")