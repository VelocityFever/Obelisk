from util import Events

class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("feedback",desc="Send feedback")]

    async def handle_command(self, message_object, command, args):
        if command == "feedback":
            text = args[1]
            await self.feedback(message_object, text)

    async def feedback(self, message_object, text):
        msg = "{0.author.mention}, send feedback at: https://goo.gl/forms/m64rDIB1aKAgcSDv2.".format(message_object)
        await self.pm.client.send_message(message_object.channel, msg)

