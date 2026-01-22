"""Minimal MCP server boilerplate with add function."""

from mcp.server.fastmcp import FastMCP

# Create the server instance
mcp = FastMCP("mcp-server-coverage-report")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two integers together.

    Args:
        a: First integer
        b: Second integer

    Returns:
        The sum of a and b
    """
    return a + b


def main() -> None:
    """Main entry point for the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
