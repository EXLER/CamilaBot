#!/usr/bin/env python3

import os
import configparser
from datetime import datetime
from subprocess import check_output, CalledProcessError

import discord
from discord.ext import commands

import utils.log

config = configparser.ConfigParser()
config.read("config.ini")

cogs = []
for file in os.listdir("cogs"):
    if file.endswith(".py"):
        cogs.append(f"cogs.{file[:-3]}")


class Camila(commands.Bot):
    """
    Main Bot class derived from the discord.py Bot.
    """

    def __init__(self, command_prefix, description):
        super().__init__(command_prefix=command_prefix, description=description)

        self.startup = datetime.now()

        self.failed_cogs = []
        self.exitcode = 0

    def load_cogs(self):
        for extension in cogs:
            try:
                self.load_extension(extension)
            except BaseException as e:
                utils.log.warn(f"{extension} failed to load.")
                self.failed_cogs.append([extension, type(e).__name__, e])


def run_bot() -> int:
    # Attempt to get current git information
    try:
        commit = check_output(["git", "rev-parse", "HEAD"]).decode("ascii")[:-1]
    except CalledProcessError as e:
        print(f"Checking for git commit failed: {type(e).__name__}: {e}")
        commit = "<unknown>"

    try:
        branch = check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode()[
            :-1
        ]
    except CalledProcessError as e:
        print(f"Checking for git branch failed: {type(e).__name__}: {e}")
        branch = "<unknown>"

    bot = Camila(
        (".", "!"), description="Camila, a calendar and task managment Discord bot"
    )
    bot.help_command = commands.DefaultHelpCommand(dm_help=None)
    utils.log.info(f"Starting Camila on commit {commit} on branch {branch}")
    bot.load_cogs()
    bot.run(config["Discord"]["BotToken"])

    return bot.exitcode


if __name__ == "__main__":
    exit(run_bot())
