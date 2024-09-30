from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()

slack_client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

def suggest_donation():
    # Example: Notify about personalized donation suggestions
    slack_client.chat_postMessage(channel="your_channel_id", text="Suggested donation: $50 based on your previous contributions.")
    print("Personalized donation suggestion sent.")

suggest_donation()
