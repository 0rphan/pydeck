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

    def init_commands(self):
        self.commands = [None for _ in range(16)]

    def add_command(self, command, index=-1):
        if index != -1:
            self.commands[index] = command
        else:
            for i in range(len(self.commands)):
                if self.commands[i] is None:
                    self.commands[i] = command
                    break

            print(f"[{self.__class__.__name__}] Error: Commands list is full!")

    def start_stop_stream(self):
        ret = api.start_stop_stream()
        if ret != None:
            print(f"[{self.__class__.__name__}] {ret}")

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

    def next_scene(self):
        ret = api.next_scene()
        if ret != None:
            print(f"[{self.__class__.__name__}] {ret}")

# Demo: stream profile!
class demo_stream_mode(profile):
    def __init__(self):
        self.add_command(self.start_stop_stream)
        self.add_command(self.next_scene, index=3)

# Demo: recording profile!
class demo_record_mode(profile):
    def __init__(self):
        self.add_command(self.start_record)
        self.add_command(self.pause_resume_record)
        self.add_command(self.stop_record)