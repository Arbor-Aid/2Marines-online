from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()

slack_client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

def test_apis():
    # Testing Slack
    try:
        slack_client.api_test()
        print("Slack API is working.")
    except Exception as e:
        print(f"Error with Slack API: {e}")

    # Testing Notion
    try:
        notion_client = Client(auth=os.getenv("NOTION_API_KEY"))
        notion_client.search(query="test")
        print("Notion API is working.")
    except Exception as e:
        print(f"Error with Notion API: {e}")

    # Testing GitHub
    try:
        github_client = Github(os.getenv("GITHUB_TOKEN"))
        github_client.get_user().login
        print("GitHub API is working.")
    except Exception as e:
        print(f"Error with GitHub API: {e}")

test_apis()
