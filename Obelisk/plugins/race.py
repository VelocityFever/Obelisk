from util import Events
import discord
import asyncio
import random


class Plugin(object):
    def __init__(self, pm):
        self.pm = pm
        self.race = self.Race()

    class Race(object):
        class Participant(object):
            # Field used to sort participants
            position = 0

            def __init__(self, name, emoji):
                self.name = name
                self.emoji = emoji
                self.progress = 0
                self.finished = False

        open = False
        running = False
        participants = list()
        finish_pos = 1

    @staticmethod
    def register_events():
        """
        Define events that this plugin will listen to
        :return: A list of util.Events
        """
        return [Events.Command("race"), Events.Command("joinrace", desc="Starts/joins a race")]
    async def handle_command(self, message_object, command, args):
        """
        Handle Events.Command events
        :param message_object: discord.Message object containing the message
        :param command: The name of the command (first word in the message, without prefix)
        :param args: List of words in the message
        """
        if command == "race":
            await self.start_race(message_object)
        if command == "joinrace":
            await self.join_race(message_object, args)

    async def start_race(self, message_object: discord.Message):
        """
        :param message_object: discord.Message object
        """
        self.race = None
        self.race = self.Race()
        self.race.participants = list()
        self.race.finish_pos = 1
        race_start = await self.pm.client.send_message(message_object.channel,
                                                       message_object.author.name + " has started a race! \n"
                                                                                    "Type `/joinrace [emoji]` to "
                                                                                    "join the race (10s)")
        # Give users time to join
        self.race.open = True
        await asyncio.sleep(10)
        await self.pm.client.delete_message(message_object)
        await self.pm.client.delete_message(race_start)
        self.race.open = False

        # If enough participants, start the race
        if len(self.race.participants) > 0:
            race_status = ":checkered_flag: :checkered_flag: :checkered_flag:\n"
            for p in self.race.participants:
                steps = round(p.progress / 5) - 1
                left = 20 - steps - 1
                race_status += "`" + p.name[:15] + self.repeat("_", 15 - len(p.name)) + "` | " + \
                               self.repeat("\_", steps) + p.emoji + self.repeat("\_", left) + \
                               " (" + str(p.progress) + ") \n"
            race_status += ":checkered_flag: :checkered_flag: :checkered_flag:"
            race_message = await self.pm.client.send_message(message_object.channel, race_status)

            # Run the race until every player has finished
            self.race.running = True
            while self.race.running:
                self.race.running = False
                player_finished = False

                # Update player states
                for p in self.race.participants:
                    p.progress = min(p.progress + random.randint(5, 20), 100)
                    if p.progress < 100:
                        self.race.running = True
                    elif not p.finished:
                        p.position = self.race.finish_pos
                        print("Player " + p.name + " " + p.emoji + "finished " + str(p.position))
                        p.finished = True
                        player_finished = True

                # Update progress message
                race_status = ":checkered_flag: :checkered_flag: :checkered_flag:\n"
                for p in self.race.participants:
                    steps = round(p.progress / 5) - 1
                    left = 20 - steps - 1

                    race_status += "`" + p.name[:15] + self.repeat("_", 15 - len(p.name)) + "` | " + \
                                   self.repeat("\_", steps) + p.emoji + self.repeat("\_", left) + \
                                   " (" + str(p.progress) + ") \n"

                race_status += ":checkered_flag: :checkered_flag: :checkered_flag:"
                race_message = await self.pm.client.edit_message(race_message, race_status)

                # Finishing state update
                if player_finished:
                    self.race.finish_pos += 1

                # Wait a bit before updating
                await asyncio.sleep(1)

            # Game ended. Display rankings
            finish_text = "Race ended! Ranking:\n"
            for pl in sorted(self.race.participants, key=lambda part: part.position):
                finish_text += pl.name + " (" + pl.emoji + "): " + str(pl.position) + "\n"

            await self.pm.client.send_message(message_object.channel, finish_text)

    async def join_race(self, message_object: discord.Message, args):
        if self.race.open:
            if args[1] != "":
                for e in self.pm.client.get_all_emojis():
                    print(e)
                await self.user_join_as_emoji(message_object, args[1])
            else:
                emojis = [":dog:", ":cat:", ":mouse:", ":hamster:", ":rabbit:", ":bear:", ":panda_face:", ":koala:",
                          ":snail:", ":bee:", ":elephant:", ":gorilla:", ":squid:"]
                await self.user_join_as_emoji(message_object, random.choice(emojis))
        else:
            not_running = await self.pm.client.send_message(message_object.channel,
                                                            "There is no active or open race at this moment! "
                                                            "Please start one with '!race'")
            await asyncio.sleep(3)
            await self.pm.client.delete_message(not_running)

    async def user_join_as_emoji(self, message_object, emoji):
        if message_object.author.nick is not None:
            self.race.participants.append(self.Race.Participant(message_object.author.nick, emoji))
        else:
            self.race.participants.append(self.Race.Participant(message_object.author.name, emoji))

        await self.pm.client.send_message(message_object.channel,
                                          message_object.author.name + " has joined the race as " +
                                          emoji)
        await asyncio.sleep(3)
        await self.pm.client.delete_message(message_object)

    @staticmethod
    def repeat(char, num):
        return ''.join([char for s in range(0, num)])

