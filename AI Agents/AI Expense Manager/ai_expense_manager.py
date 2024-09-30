from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()

slack_client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

def manage_expenses():
    # Example: Notify about expense management
    slack_client.chat_postMessage(channel="your_channel_id", text="Expense Management: Reduced operational costs by 5% this month.")
    print("Expense management notification sent.")

manage_expenses()
