"""Minimal MCP server boilerplate with coverage report tool."""

import io
from pathlib import Path

import coverage
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-server-coverage-report")


@mcp.tool()
def show_global_coverage() -> str:
    """Shows the files and the coverage they have.

    Generates a coverage report displaying all files and their coverage percentages,
    including information about missing lines.

    Returns:
        A formatted coverage report showing files and their coverage statistics
    """

    cov = coverage.Coverage()
    cov.load()
    buffer = io.StringIO()
    cov.report(file=buffer, show_missing=True)
    return buffer.getvalue()


@mcp.tool()
def show_missing_lines(file: str | Path) -> str:
    """Shows lines missing coverage from a file.

    Displays the actual code content for lines that are missing test coverage,
    grouped into ranges for consecutive missing lines.

    Args:
        file: The file path to show the missing lines from.

    Returns:
        A formatted report showing the missing lines with their code content.
    """

    file = Path(file)
    assert file.exists(), f"File {file} does not exist"

    # Load coverage data
    cov = coverage.Coverage()
    cov.load()

    # Get the absolute path for the file
    file_abs = file.resolve()

    # Get analysis for this file
    try:
        analysis = cov.analysis(str(file_abs))
    except coverage.CoverageException:
        # File might not be in coverage data
        return f"No coverage data found for {file}"

    # analysis returns: (statements, excluded, missing, missing_formatted)
    statements, excluded, missing, missing_formatted = analysis

    if not missing:
        return f"No missing lines found for {file}"

    # Read the file content
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Group consecutive missing lines into ranges
    result_parts = []
    missing_sorted = sorted(missing)

    i = 0
    while i < len(missing_sorted):
        start = missing_sorted[i]
        end = start

        # Find consecutive lines
        while i + 1 < len(missing_sorted) and missing_sorted[i + 1] == end + 1:
            end = missing_sorted[i + 1]
            i += 1

        # Format the range or single line
        if start == end:
            line_num = start
            result_parts.append(f"{line_num}")
        else:
            result_parts.append(f"{start}-{end}")

        # Add the actual code lines
        for line_num in range(start, end + 1):
            if 1 <= line_num <= len(lines):
                line_content = lines[line_num - 1].rstrip("\n\r")
                result_parts.append(line_content)

        # Add blank line between ranges
        result_parts.append("")
        i += 1

    return "\n".join(result_parts).rstrip()


def main() -> None:
    """Main entry point for the MCP server."""

    mcp.run()


if __name__ == "__main__":
    main()
