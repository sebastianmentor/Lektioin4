import configparser
import shutil
import os
import argparse

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

def backup_profile():
    shutil.copy(PROFILE_FILE, BACKUP_FILE)
    print("Backup created!")

def update_user_role(new_role):
    config = configparser.ConfigParser()
    config.read(PROFILE_FILE)

    old_role = config['user']['role']
    config['user']['role'] = new_role

    with open(PROFILE_FILE, 'w') as f:
        config.write(f)

    print(f"Update user role from {old_role} to {new_role}!")

def update_user_name(new_name):
    config = configparser.ConfigParser()
    config.read(PROFILE_FILE)

    old_name = config['user']['username']
    config['user']['username'] = new_name

    with open(PROFILE_FILE, 'w') as f:
        config.write(f)

    print(f"Update user role from {old_name} to {new_name}!")

def restore_profile():
    if os.path.exists(BACKUP_FILE):
        shutil.copy(BACKUP_FILE, PROFILE_FILE)
        print("Profile restored from backup!")
    else:
        print("Alert! No backup found!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Handles user profile.")
    parser.add_argument(
        "--restore", 
        action="store_true", 
        help="Restore user profile from backup!")

    parser.add_argument(
        "--backup", 
        action="store_true", 
        help="Bacup current user profile!")
    
    parser.add_argument(
        "--role",
        type=str, 
        help="Declare new user role!"
    )

    parser.add_argument(
        "--username",
        type=str, 
        help="Declare new username!"
    )
    
    args = parser.parse_args()

    if args.restore:
        restore_profile()

    if args.backup:
        backup_profile()

    if args.role:
        update_user_role(args.role)
    
    if args.username:
        update_user_name(args.username)