import cogs.utils.db as db
import json
from discord.ext import commands

init_ext = [
    'cogs.event',
    'cogs.task',
    'cogs.command'
]

bot = commands.Bot(command_prefix=['s/'], description='sausiber', pm_help=None, help_attrs=dict(hidden=True))


def load_files():
    with open('config.json') as f:
        return json.load(f)


def load_database():
    with open('postgresql.json') as f:
        db_file = json.load(f)
    db.load_db(db_file['user'], db_file['password'], db_file['hostname'], db_file['database'])


if __name__ == "__main__":
    config = load_files()
    load_database()

    for ext in init_ext:
        try:
            bot.load_extension(ext)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(ext, type(e).__name__, e))

    bot.run(config['token'])
