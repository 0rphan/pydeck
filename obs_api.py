import sys
import time

import logging
logging.basicConfig(level=logging.INFO)

sys.path.append('../')
from obswebsocket import obsws, requests

class OBSAPI():
    def __init__(self):
        self.state = ""

    def start_record(self):
        started = self.ws.call(requests.StartRecording()).status
        if not started:
            return "Already recording!"

        self.state = "recording"
        return "Recording started!"

    def pause_resume_record(self):
        if self.state == "recording":
            paused = self.ws.call(requests.PauseRecording())
            if not paused:
                return "Already paused!"

            self.state = "paused"
            return "Recording paused!"
        elif self.state == "paused":
            resumed = self.ws.call(requests.ResumeRecording())
            if not resumed:
                return "Recording not paused"

            self.state = "recording"
            return "Recording resumed!"

        return "No ongoing recording!"

    def stop_record(self):
        stopped = self.ws.call(requests.StopRecording()).status
        if not stopped:
            return "No ongoing recording!"

        self.state = ""
        return "Recording stopped!"

    def connect(self, host="localhost", port="4444", password=""):
        self.host = host
        self.port = port
        self.password = password

        self.ws = obsws(self.host, self.port, self.password)
        self.ws.connect()

    def disconnect(self):
        self.ws.disconnect()