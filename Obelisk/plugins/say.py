from util import Events

class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("say",desc="Says something")]

    async def handle_command(self, message_object, command, args):
        if command == "say":
            text = args[1]
            await self.say(message_object, text)

    async def say(self, message_object, text):
        msg = text
        await self.pm.client.delete_message(message_object)
        await self.pm.client.send_message(message_object.channel, msg)
