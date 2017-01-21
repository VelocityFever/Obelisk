from util import Events

class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("reverse",desc="Flip text")]

    async def handle_command(self, message_object, command, args):
        if command == "reverse":
            v = args[1]
            text = v [::-1]
            await self.reverse(message_object, text)

    async def reverse(self, message_object, text):
        msg = text
        await self.pm.client.send_message(message_object.channel, msg)

