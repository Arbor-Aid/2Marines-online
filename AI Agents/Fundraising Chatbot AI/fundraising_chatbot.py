from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()

slack_client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

def engage_donors():
    # Example: Send a message to potential donors
    slack_client.chat_postMessage(channel="your_channel_id", text="Support our cause: Donate to 2Marines today!")
    print("Donation engagement message sent.")

engage_donors()
