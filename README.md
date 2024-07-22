# RLBotPythonExample

Example of a Python bot using the RLBot framework

## Quick Start

- Install Python 3.10 or later
- Create a Python virtual environment
  - `python -m venv venv`
- Install the required packages
  - `pip install -r requirements.txt`
- Download `RLBotServer.exe` and place it in the root directory
  - <https://github.com/RLBot/core>
- Modify `rlbot.toml` to your liking
  - Note: `dev.toml` also exists with a few changed settings that might be useful for development
- Start a match with `python run.py`

## Changing the bot

- Bot behavior is controlled by `src/bot.py`
- Bot appearance is controlled by `src/looks.toml`
