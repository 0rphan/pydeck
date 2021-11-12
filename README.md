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
1. Run `python3 macro_pad.py`
1. Upload the arduino code
1. Enjoy!

## For developers
* IDE (sublime is my recommendation)
* [Arduino IDE](https://www.arduino.cc/en/software)
* [Python](https://www.python.org/) 3.X +