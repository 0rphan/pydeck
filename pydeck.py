import serial, time
import argparse
from profiles import *

def get_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Arduino arguments
    parser.add_argument("-c", "--com", help="The communication port of the arduino", default="COM3")
    parser.add_argument("-f", "--frequency", help="The frequency of the serial", default="9600")

    # obswebsocket arguments

    parser.add_argument("-i", "--ip", help="The ip of the obs websocket", default="localhost")
    parser.add_argument("-p", "--port", help="The port of the obs websocket", default="4444")
    parser.add_argument("-w", "--password", help="The password to the websocket", default="")

    return parser.parse_args()

def main():
    args = get_args()

    api.connect(args.ip, args.port, args.password)

    connected = False
    ser = serial.Serial(args.com, args.frequency)

    # List of profiles the deck will cycle trough
    profiles = [demo_record_mode()]

    current_profile = 0;

    # loop until the arduino tells us the serial connection is ready
    while not connected:
        print("Press any key to start!")
        serin = ser.read()
        connected = True
        print(f"Current profile: {profiles[current_profile].__class__.__name__}")
        # if serial available save value in var, print value and clear it afterwards for new input
        while True:
            var = ser.read_until().strip().decode()
            if var == '':
                continue

            # If current_profile pressed ('C' from arduino)
            if var == 'C':
                current_profile = (current_profile + 1) % len(profiles)
                print(f"Switched to {profiles[current_profile].__class__.__name__}")
            else:
                profiles[current_profile].process_command(var)

            del var

    # close the port and end the program
    ser.close()

    # disconnect for the api
    api.disconnect()

if __name__ == "__main__":
    main()