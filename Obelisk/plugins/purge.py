from util import Events
from util.Ranks import Ranks


class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("purge", Ranks.Mod, desc="Purge a number of messages. Mods and Admins only"),
                Events.Command("purgeall", desc="Purges all messages from a channel. Admins only")]

    async def handle_command(self, message_object, command, args):
        if command == "purge":
            await self.purge(message_object, args[1])
        if command == "purgeall":
            await self.purgeall(message_object)

    async def purge(self, message_object, num):
        await self.pm.client.purge_from(message_object.channel, limit=int(num))
    async def purgeall(self, message_object):
        limit = self.pm.client.messages.maxlen
        chnnl = message_object.channel
        await self.pm.client.purge_from(chnnl, limit=limit)
