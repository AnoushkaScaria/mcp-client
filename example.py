from client import JiraConfluenceMCPClient

MCP_SERVER_URL = "http://localhost:8000/mcp"


def main():
    client = JiraConfluenceMCPClient(MCP_SERVER_URL)

    print("🔍 Discovering tools...")
    tools = client.list_tools()
    for tool in tools:
        print(f"- {tool['name']}: {tool['description']}")

    issue_key = "PROJ-123"  # example Jira ticket

    print("\n📄 Fetching Jira ticket...")
    ticket = client.fetch_jira_ticket(issue_key)
    print(ticket)

    print("\n📝 Creating Confluence page...")
    page = client.generate_confluence_page(issue_key)
    print(f"Created page with ID: {page.get('id')}")


if __name__ == "__main__":
    main()
