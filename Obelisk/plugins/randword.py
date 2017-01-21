from util import Events
import codecs
import random

class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("randword",desc="Chooses a random word")]

    async def handle_command(self, message_object, command, args):
        if command == "randword":
            word_file = "/home/kevin/Obelisk/words.txt"
            lines = codecs.open(word_file, "r", "utf-8", "ignore").readlines()
            rand_line = str(lines[random.randint(0, len(lines))-1]).strip()
            await self.randword(message_object, rand_line)

    async def randword(self, message_object, line):
        await self.pm.client.send_message(message_object.channel, line)
