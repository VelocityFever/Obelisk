from util import Events
from util.Ranks import Ranks

class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("eval", Ranks.Admin, desc="Evaluates something")]

    async def handle_command(self, message_object, command, args):
        if command == "eval":
            text = args[1]
            await self.eval(message_object, text)

    async def eval(self, message_object, text):
        evaled = eval(text)
        msg = "```Markdown\n#Evaluated: \n" + text + "\n#Returned: \n"  + str(evaled) + "```"
        await self.pm.client.send_message(message_object.channel, msg)
