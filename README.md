# Minimal MCP Server Boilerplate

A minimal Python MCP (Model Context Protocol) server example with a simple `add` function.

## Features

- Simple `add(a: int, b: int) -> int` function that adds two integers
- Uses `uv` for dependency management
- Runs via stdio (use with `uvx`)

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Test the server locally:
   ```bash
   uv run mcp-server-coverage-report
   ```

## Using with Cursor

To configure Cursor to use this MCP server, add the following to your Cursor MCP settings.

### Option 1: Using uvx (Recommended)

Add to your Cursor MCP configuration (usually in Cursor settings or `.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "mcp-server-coverage-report": {
      "command": "uvx",
      "args": [
        "--from",
        "/mnt/c/Github/mcp-server-coverage-report",
        "mcp-server-coverage-report"
      ]
    }
  }
}
```

**Note:** Update the path `/mnt/c/Github/mcp-server-coverage-report` to match your actual project directory.

### Option 2: Using uv run

Alternatively, you can use `uv run`:

```json
{
  "mcpServers": {
    "mcp-server-coverage-report": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/mnt/c/Github/mcp-server-coverage-report",
        "mcp-server-coverage-report"
      ]
    }
  }
}
```

After adding the configuration, restart Cursor for the changes to take effect.

## Development

- Install new dependencies: `uv add <package-name>`
- Run the server: `uv run mcp-server-coverage-report`
- The server exposes one tool: `add` which takes two integers and returns their sum
