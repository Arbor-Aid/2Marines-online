from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()

slack_client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

def test_bot_responses():
    try:
        # Test Slack response
        response = slack_client.chat_postMessage(channel="your_channel_id", text="QA Test: Bot is active.")
        print(f"Slack response: {response}")
    except Exception as e:
        print(f"Error testing Slack bot: {e}")

test_bot_responses()
