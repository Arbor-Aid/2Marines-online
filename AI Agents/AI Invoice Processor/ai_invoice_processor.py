from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()

slack_client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

def process_invoices():
    # Example: Notify about invoice processing
    slack_client.chat_postMessage(channel="your_channel_id", text="Invoice Processing: 10 invoices processed today.")
    print("Invoice processing notification sent.")

process_invoices()
