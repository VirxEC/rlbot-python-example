# RLBotPythonExample

Example of a Python bot using the RLBot framework

## Quick Start

1. Install Python 3.10 or later
1. Create a Python virtual environment
   - `python3 -m venv venv`
1. Activate the virtual environment
   - Windows: `.\venv\Scripts\activate`
   - Linux: `source venv/bin/activate`
1. Install the required packages
   - `pip install -r requirements.txt`
1. Download `RLBotServer.exe` and place it in the root directory
   - <https://github.com/RLBot/core>
1. Modify `rlbot.toml` to your liking
   - Note: `dev.toml` also exists with a few changed settings that might be useful for development
1. Start a match with `python run.py`

## Changing the bot

- Bot behavior is controlled by `src/bot.py`
- Bot appearance is controlled by `src/loadout.toml`
