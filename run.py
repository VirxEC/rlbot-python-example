from pathlib import Path

from rlbot.managers import MatchManager

MATCH_CONFIG_FILE = "rlbot.toml"

if __name__ == "__main__":
    root_dir = Path(__file__).parent

    match_manager = MatchManager(root_dir)
    match_manager.start_match(root_dir / MATCH_CONFIG_FILE, False)
    match_manager.disconnect()
