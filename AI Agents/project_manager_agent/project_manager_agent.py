from slack_sdk import WebClient
from slack_sdk.socket_mode import SocketModeClient, SocketModeRequest
from notion_client import Client as NotionClient
import os
from dotenv import load_dotenv

load_dotenv()

slack_client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
notion = NotionClient(auth=os.getenv("NOTION_API_KEY"))

def get_notion_tasks():
    database_id = "your_database_id"  # Replace with actual ID
    try:
        results = notion.databases.query(database_id=database_id).get("results", [])
        tasks = [result["properties"]["Name"]["title"][0]["text"]["content"] for result in results]
        return tasks
    except Exception as e:
        print(f"Error retrieving tasks from Notion: {e}")
        return []

def handle_events(client: SocketModeClient, req: SocketModeRequest):
    if req.type == "events_api":
        event = req.payload.get("event", {})
        if event.get("type") == "message":
            text = event.get("text", "").lower()
            if "notion tasks" in text:
                tasks = get_notion_tasks()
                slack_client.chat_postMessage(channel=event["channel"], text=f"Tasks: {tasks}")

socket_mode_client = SocketModeClient(app_token=os.getenv("SLACK_APP_TOKEN"), web_client=slack_client)
socket_mode_client.socket_mode_request_listeners.append(handle_events)
socket_mode_client.connect()
