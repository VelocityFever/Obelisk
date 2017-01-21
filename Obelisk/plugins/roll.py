from util import Events
import codecs
import random

class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("roll",desc="Rolls a dice")]

    async def handle_command(self, message_object, command, args):
        if command == "roll":
            num_file = "/home/kevin/Obelisk/numbers.txt"
            lines = codecs.open(num_file, "r", "utf-8", "ignore").readlines()
            rand_line = str(lines[random.randint(0, len(lines))-1]).strip()
            await self.roll(message_object, rand_line)

    async def roll(self, message_object, line):
        msg = "And you rolled a..." + line + "!"
        await self.pm.client.send_message(message_object.channel, msg)
