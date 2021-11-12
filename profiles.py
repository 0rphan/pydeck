from obs_api import OBSAPI

api = OBSAPI()

# Class 'profile' is the main class that holds all the functions the deck can be assinged to do.
# To expand the deck's functionality inherit from this class 
class profile():
    def process_command(self, comm):
        index = int(comm, 16)
        if index > len(self.commands) - 1:
            print(f"[{self.__class__.__name__}] Error: no commands assigned!")
            return
        self.commands[index]()

    def start_record(self):
        ret = api.start_record()
        if ret != None:
            print(f"[{self.__class__.__name__}] {ret}")

    def pause_resume_record(self):
        ret = api.pause_resume_record()
        if ret != None:
            print(f"[{self.__class__.__name__}] {ret}")

    def stop_record(self):
        ret = api.stop_record()
        if ret != None:
            print(f"[{self.__class__.__name__}] {ret}")

# Demo: recording profile!
class demo_record_mode(profile):
    def __init__(self):
        self.commands = [self.start_record, self.pause_resume_record, self.stop_record]