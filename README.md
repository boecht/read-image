# boecht/read-image

MCP server to read image files and return as base64.

As of February 2026, GitHub Copilot does not have built-in support for reading
image files directly. This MCP server provides a workaround by reading image
files and returning their contents as base64-encoded strings, which can then
be processed by Copilot.

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

## Example `.github/workflows/copilot-setup-steps.yml`

```yaml
---
name: "Copilot Setup Steps for GitHub Codespaces"

on: workflow_dispatch

jobs:
  copilot-setup-steps:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout

      - name: Set up Python
        uses: actions/setup-python

      - name: Install uv
        uses: astral-sh/setup-uv

      - name: Verify uv works
        run: uv --version

      - name: Install MCP server dependencies
        run: uv sync --directory .mcp/read-image # Adjust path as needed
```
