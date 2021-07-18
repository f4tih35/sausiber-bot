# SAUSIBER Discord Bot

## Installation
- Clone this project with `$ git clone https://github.com/sausiber/discord-bot.git`
- You can use virtual environment if you want. [Checkout this link if you don't know what virtual environment is](https://docs.python.org/3/tutorial/venv.html)
- Install requirement packages with `$ pip install -r requirements.txt`

- Create and fill config.json for using your discord token.

```json
{
  "token": ""
}
```

- Create and fill postgresql.json for database operations.

```json
{
  "hostname": "",
  "user": "",
  "password": "",
  "database": ""
}
```

- Run setup.py for creating tables.

`$ python setup.py`

- Finally run bot.py and enjoy your discord bot.

`$ python bot.py`
