from fastmcp import MCPClient


class JiraConfluenceMCPClient:
    def __init__(self, server_url: str):
        """
        server_url example: http://localhost:8000/mcp
        """
        self.client = MCPClient(server_url)

    def list_tools(self):
        """
        Discover available MCP tools.
        """
        return self.client.list_tools()

    def fetch_jira_ticket(self, issue_key: str):
        """
        Call MCP tool: fetch_jira_ticket
        """
        return self.client.call_tool(
            name="fetch_jira_ticket",
            arguments={"issue_key": issue_key},
        )

    def generate_confluence_page(self, issue_key: str):
        """
        Call MCP tool: generate_confluence_page_from_jira
        """
        return self.client.call_tool(
            name="generate_confluence_page_from_jira",
            arguments={"issue_key": issue_key},
        )
