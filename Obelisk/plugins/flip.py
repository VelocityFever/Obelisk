from util import Events
import codecs
import random

class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("flip",desc="Flips a coin")]

    async def handle_command(self, message_object, command, args):
        if command == "flip":
            num_file = "/home/kevin/Obelisk/coin.txt"
            lines = codecs.open(num_file, "r", "utf-8", "ignore").readlines()
            rand_line = str(lines[random.randint(0, len(lines))-1]).strip()
            await self.flip(message_object, rand_line)

    async def flip(self, message_object, line):
        msg = "The coin landed on **_" + line + "_**!"
        await self.pm.client.send_message(message_object.channel, msg)
