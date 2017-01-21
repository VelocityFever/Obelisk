from util import Events
from util.Ranks import Ranks


class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        """
        Define events that this plugin will listen to
        :return: A list of util.Events
        """
        return [Events.Command("reload", Ranks.Admin, desc="Reloads all modules. Admin only")]

    async def handle_command(self, message_object, command, args):
        """
        Handle Events.Command events
        :param message_object: discord.Message object containing the message
        :param command: The name of the command (first word in the message, without prefix)
        :param args: List of words in the message
        """
        if command == "reload":
            await self.reload(message_object)

    async def reload(self, message_object):
        self.pm.client.send_message(message_object.channel, "Reloading plugins...")
        self.pm.load_plugins()
        self.pm.register_events()

