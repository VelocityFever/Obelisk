from util import Events
import codecs
import random

class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("eightball",desc="Ask the 8ball something")]

    async def handle_command(self, message_object, command, args):
        if command == "eightball":
            num_file = "/home/kevin/Obelisk/8ball.txt"
            lines = codecs.open(num_file, "r", "utf-8", "ignore").readlines()
            rand_line = str(lines[random.randint(0, len(lines))-1]).strip()
            await self.eightball(message_object, rand_line)

    async def eightball(self, message_object, line):
        msg = line
        await self.pm.client.send_message(message_object.channel, msg)
