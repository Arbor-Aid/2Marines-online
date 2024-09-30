from slack_sdk import WebClient
from github import Github
import os
from dotenv import load_dotenv

load_dotenv()

slack_client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
github_client = Github(os.getenv("GITHUB_TOKEN"))

def get_github_issues(repo_name):
    repo = github_client.get_repo(repo_name)
    issues = repo.get_issues(state="open")
    return [f"Issue #{issue.number}: {issue.title}" for issue in issues]

def handle_events(client: SocketModeClient, req: SocketModeRequest):
    if req.type == "events_api":
        event = req.payload.get("event", {})
        if event.get("type") == "message":
            text = event.get("text", "").lower()
            if "github issues" in text:
                issues = get_github_issues("your_github_repo")
                slack_client.chat_postMessage(channel=event["channel"], text=f"Issues: {issues}")

socket_mode_client = SocketModeClient(app_token=os.getenv("SLACK_APP_TOKEN"), web_client=slack_client)
socket_mode_client.socket_mode_request_listeners.append(handle_events)
socket_mode_client.connect()
