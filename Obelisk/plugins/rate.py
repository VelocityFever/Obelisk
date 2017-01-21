from util import Events
import random

class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("rate",desc="Rate someone or something between 0 and 100")]

    async def handle_command(self, message_object, command, args):
        if command == "rate":
            await self.rate(message_object, args[1])

    async def rate(self, message_object, user):

        def isDevMentioned():
            for u in message_object.mentions:
                if u.name == "Red Panda" or u.name == "Obelisk":
                    return True
            return False
        if user == "obelisk" or user == "Obelisk" or user == "Red Panda" or user == "RedPanda" or isDevMentioned():
            await self.pm.client.send_message(message_object.channel, "I would rate **" + user + "** 100.00/100")
        else:
            number = round(random.uniform(1, 100), 2)
            print(message_object.mentions)
            await self.pm.client.send_message(message_object.channel,
                                          "I would rate " + "**" + user + "** " + str(number) + "/100")
