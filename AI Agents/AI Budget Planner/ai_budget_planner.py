from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()

slack_client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

def plan_budget():
    # Example: Notify about budget planning
    slack_client.chat_postMessage(channel="your_channel_id", text="Budget Planning: Q4 budget plan is ready for review.")
    print("Budget planning notification sent.")

plan_budget()
