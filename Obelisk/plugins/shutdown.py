import sys
from util import Events
from util.Ranks import Ranks

class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("shutdown", Ranks.Admin, desc="Shutdown. Admin only")]

    async def handle_command(self, message_object, command, args):
        if command == "shutdown":
            await self.shutdown(message_object)

    async def shutdown(self, message_object):
        await self.pm.client.send_message(message_object.channel, "Shutting down...")
        await self.pm.client.logout()
        sys.exit(0)
