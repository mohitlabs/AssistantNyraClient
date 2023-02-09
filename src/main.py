# MIT License

# Copyright (c) 2023 MohitLabs

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from gtts import gTTS
import speech_recognition as sr
import requests
import urllib
import os
import sys
import subprocess
#import signal
import datetime
import webbrowser
import random

class AssistantNyraClient:
	def __init__(self):
		self.BASEURL = "http://127.0.0.1:8090/"
		self.FILEPATH = "audio/"
		self.FILENAME = "Voice.mp3"
	
	def listen(self):
		rec = sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening...\n")
			rec.pause_threshold = 1
			audio = rec.listen(source)
		try:
			print("Recognizing...\n")
			query = rec.recognize_google(audio, language="en-in").lower()
			print(f"You said: {query}\n")
			self.search_query(query)
		except Exception as e:
			print(e)
			self.say("Sorry, I can't get it. Please, can you say that again?")
			print("Say that again please...\n")
			return "None"
	
	def search_query(self, query):
		final_URL = self.BASEURL + urllib.parse.quote(query)
		response = requests.get(final_URL)
		print(f"HTTP Response: {response.text}\n")
		print(f"Status Code: {response.status_code}\n")
		self.say(response.text)
	
	def say(self, text):
		try:
			tts = gTTS(text=text, lang="en")
			tts.save(self.FILEPATH + self.FILENAME)
			os.system(f"mpg321 {self.FILEPATH + self.FILENAME}")
		except Exception as e:
			print(e)
			os.system(f"mpg321 {self.FILEPATH}NetworkError.mp3")

if __name__ == "__main__":
	while True:
		AssistantNyraClient().listen()

# URL = "https://something.com"
# DATA = {
#     "parameter1": 4,
#     "parameter2": 8
# }

# r2 = requests.post(url=URL, data=DATA)
# print(r2.text)
# print(r1.status_code)
