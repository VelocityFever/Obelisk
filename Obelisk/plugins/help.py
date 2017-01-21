
from util import Events


class Plugin(object):
    def __init__(self, pm):
        self.pm = pm

    @staticmethod
    def register_events():
        return [Events.Command("help", desc="Shows help text for a plugin"),
                Events.Command("obelisk", desc="Alias of ^^"),
                Events.Command("hello", desc="Hello!"),
                Events.Command("commands", desc="Shows a list of commands"),
                Events.Command("info", desc="Check info"),
                Events.Command("support", desc="Support us on Patreon"),
                Events.Command("invite", desc="Get an invite link for Obelisk")]
    async def handle_command(self, message_object, command, args):
        if command == "help":
            if args[1] is not "":
                await self.show_help(message_object, args[1].lower())
            else:
                await self.show_help_assigned(message_object)
        if command == "info":
            await self.info(message_object)
        if command == "hello":
            await self.hello(message_object)
        if command == "commands":
            await self.commands(message_object)
        if command == "invite":
            await self.invite(message_object)
        if command == "support":
            await self.support(message_object)
        if command == "obelisk":
            await self.needhelp(message_object)
    async def commands(self, message_object):
        hstr = "**Complete Command List**\n"
        for name, commands in self.pm.comlist.items():
            if len(commands) > 0:
                hstr += "\n**{0}**\n".format(name[:-3])
                for c, d in commands:
                    if d is not "":
                        hstr += "`" + self.pm.botPreferences.commandPrefix + c + "`: \n_" + d + "_\n"
                    else:
                        hstr += "`" + self.pm.botPreferences.commandPrefix + c + "`\n"
        await self.pm.client.send_message(message_object.author, hstr)
        commandlist = '{0.author.mention}, I sent a list of commands to your direct messages. :thumbsup: '.format(message_object)
        await self.pm.client.send_message(message_object.channel, commandlist)

    async def info(self, message_object):
        await self.pm.client.send_message(message_object.channel, 'I am Obelisk, a fully modular Discord bot. Invite me to your server at: http://bit.ly/ObeliskBot')

    async def hello(self, message_object):
        msg = 'Hello {0.author.mention}!'.format(message_object)
        await self.pm.client.send_message(message_object.channel, msg)

    async def show_help(self, message_object, args):
        try:
            hstr = "**{0}**:\n".format(args)
            for c, d in self.pm.comlist[args + ".py"]:
                hstr = hstr + "`" + self.pm.botPreferences.commandPrefix + c + "`: " + d + "\n"
            await self.pm.client.send_message(message_object.channel, hstr)
        except KeyError:
            await self.pm.client.send_message(message_object.channel,
                                              ":exclamation: That\'s not a valid plugin name")

    async def show_help_assigned(self, message_object):
        x = "Help:\n"

        x += "`" + self.pm.botPreferences.commandPrefix + "help [help_topic]` to evoke a help topic.\n" + \
             "`" + self.pm.botPreferences.commandPrefix + "commands` for all commands."
        "Find help on my server at: https://discord.gg/2S9DPD2 "
        await self.pm.client.send_message(message_object.channel, x)
    async def invite(self, message_object):
        await self.pm.client.send_message(message_object.channel, "http://bit.ly/ObeliskBot")
    async def support(self, message_object):
        await self.pm.client.send_message(message_object.channel, "http://bit.ly/SupportObelisk to support me on my Patreon. To get support, go to http://bit.ly/ObeliskServer")
    async def needhelp(self, message_object):
        msg = "{0.author.mention}, need help perhaps? Do /commands for a list of commands. :wink:".format(message_object) 
        await self.pm.client.send_message(message_object.channel, msg)
