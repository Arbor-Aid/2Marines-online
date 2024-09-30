from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()

slack_client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

def generate_content():
    # Example: Notify about new content creation
    slack_client.chat_postMessage(channel="your_channel_id", text="New blog post generated: 'How 2Marines is Making a Difference'.")
    print("Content creation notification sent.")

generate_content()
