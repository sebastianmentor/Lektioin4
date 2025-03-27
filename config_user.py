import configparser
import shutil
import os

PROFILE_FILE = "userprofile.ini"
BACKUP_FILE = "userprofile.ini.bak"

def create_default_profile():
    """Create a default profile for user"""
    if not os.path.exists(PROFILE_FILE):

        print(f"Creating default {PROFILE_FILE}")
        
        config = configparser.ConfigParser()

        config["user"] = {
            'username': 'Jon Doe',
            'role': 'guest'
            }

        with open(PROFILE_FILE, "w") as f:
            config.write(f)

        print("Default user created!")


if __name__ == "__main__":
    create_default_profile()