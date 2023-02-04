import asyncio
import os

async def create_dotenv():
    print("Seems like you don't have a .env file. Let's create one now!")
    token = input("Please enter your discord token (this won't be shared with anyone): ")
    if input("do you want to enable the twitter liked image module? (y/n) ") == "y":
        bearer = input("Please enter your twitter bearer token: ")
        twitter_id = input("Please enter your twitter user id: ")
        with open(".env", "w") as f:
            f.write(f'TOKEN="{token}"\n')
            f.write(f'BEARER_TOKEN="{bearer}"\n')
            f.write(f'USER_ID="{twitter_id}"\n')
    else:
        with open(".env", "w") as f:
            f.write(f'TOKEN="{token}"')


def main():
    print("Thanks for using my bot! Let's get you setup!")
    if not os.path.exists(".env"):
        asyncio.run(create_dotenv())
    if input("Do you want to setup the bot in a virtual environment? (y/n) ") == "y":
        os.system("python3 -m venv venv")
        os.system("source venv/bin/activate")
        os.system("pip3 install -r requirements.txt")
        print("Installed as a virtual environment! Remember to run 'source venv/bin/activate' whenever you'd like to use the bot!")
    else:
        os.system("pip3 install -r requirements.txt")
        print("Installed requirements!")

main()