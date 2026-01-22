# MCP Server Coverage Report

An MCP server to manage and display code coverage reports with [coveragepy](github.com/coveragepy/coveragepy). This server provides tools to view coverage statistics and identify lines missing test coverage in your codebase. This can be used in conjunction with prompts like:

> Increase the coverage of the functions in the plot module of my project



The following tools are provided:

- **`show_global_coverage`**: Generates a coverage report displaying all files and their coverage percentages, including information about missing lines.
- **`show_missing_lines`**: Shows the actual code content for lines that are missing test coverage from a specific file, grouped into ranges for consecutive missing lines.



This package also assumes that there is a `.coverage` file that has been generated in your project as an artifact from executing [pytest-cov](https://github.com/pytest-dev/pytest-cov), read their guide on how to configure it if it's the first time you look into code coverage



You can add it to your Cursor MCP configuration (usually in Cursor settings or `.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "mcp-server-coverage-report": {
      "command": "uvx",
      "args": [
        "mcp-server-coverage-report"
      ]
    }
  }
}
```

`uvx` is a tool from the `uv` package manager that allows you to run Python packages without installing them globally. In case you don't have `uv`, just run `pip install uv`



