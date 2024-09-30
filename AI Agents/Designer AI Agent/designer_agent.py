from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()

slack_client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

def create_design_task():
    # Example: Notify about a new design task
    slack_client.chat_postMessage(channel="your_channel_id", text="New design task: Create a landing page mockup.")
    print("Design task notification sent.")

create_design_task()
