from util import Events


class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("servcount",desc="Counts servers bot is in")]

    async def handle_command(self, message_object, command, args):
        if command == "servcount":
            await self.servcount(message_object)

    async def servcount(self, message_object):
        count = len(self.pm.client.servers)
        await self.pm.client.send_message(message_object.channel, count)
