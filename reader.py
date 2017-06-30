#!/usr/bin/python3

import pyttsx3

text = input('Enter text to read: ')

engine = pyttsx3.init()

engine.say(text)

engine.runAndWait()