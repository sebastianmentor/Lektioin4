PROFILE_FILE = "userprofile.ini"
BACKUP_FILE = "userprofile.ini.bak"

print(f"Vi är i varables nu och {__name__=}")

if __name__ == "__main__":
    print("Jag körs endast om jag är en huvudfil!")
    while True:
        name = input("Enter name or q for quit: ")
        if name == "q": break

        print(name)