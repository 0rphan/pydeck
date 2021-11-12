# Stream deck using Arduino and Python

This is a little project I started due to the fact that I wanted to stream and didn't want to spend lots on a simple stream deck.
So I programmed one using an Arduino nano, custom numpad and Python.

## Requirments:
* [OBS websocket](https://github.com/Palakis/obs-websocket) library for python
* pySerial - `pip install pyserial`
* Arduino (nano would be enough)
* Numpad for the arduino

## Setup
There isn't much to do:
1. Connect the numpad to the arduino (As explained below)
1. Connect the arduino to the PC
1. Run `python3 pydeck.py`
1. Upload the arduino code
1. Enjoy!

## How to use
After you ran `python3 pydeck.py` you can start using the strean deck.
But what if you want to check layout?

To do so go to profiles.py and follow this steps:
1. Create a new class that inherits from class profile
	```python
	class my_profile(profile):
		def __init__(self):
			pass
	```
2. Add your wanted commands to the list of commands
	```python
	class my_profile(profile):
		def __init__(self):
			self.commands = [self.start_stream, self.start_record]
	```
* Note: More than 16 commands wont be usable due to a 4x4 numpad

## For developers
* IDE (sublime is my recommendation)
* [Arduino IDE](https://www.arduino.cc/en/software)
* [Python](https://www.python.org/) 3.X +