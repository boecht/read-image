# boecht/read-image

MCP server to read image files.

As of February 2026, GitHub Copilot does not have built-in support for reading
image files directly. This MCP server provides a workaround by reading image
files and returning their contents in a format that can be processed by Copilot.

## Example `.vscode/mcp.json` configuration

```json
{
  "servers": {
    "boecht/read-image": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "${workspaceFolder}/.mcp/read-image", // adjust path as needed
        "python",
        "server.py"
      ]
    }
  }
}
```
