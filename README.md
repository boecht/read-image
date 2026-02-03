# boecht/read-image

MCP server to read image files.

As of February 2026, GitHub Copilot does not have built-in support for reading
image files directly. This MCP server provides a workaround by reading image
files and returning their contents in a format that can be processed by Copilot.

## Tool

### `read_image`

Read an image file from the filesystem and return its contents.

**Arguments:**

- `file_path` (required): Absolute path to the image file

**Returns:**

Multipart content containing:

1. JSON metadata with file information:

   ```json
   {
     "fileName": "image.png",
     "filePath": "/path/to/image.png",
     "mimeType": "image/png",
     "sizeBytes": 12345
   }
   ```

2. The image content (viewable by the AI agent)

## Setup

Clone or copy this repository into your project:

```bash
git clone https://github.com/boecht/read-image .mcp/read-image
```

Then add the server to your `.vscode/mcp.json`:

```json
{
  "servers": {
    "read-image": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "${workspaceFolder}/.mcp/read-image",
        "python",
        "server.py"
      ]
    }
  }
}
```

Adjust the `--directory` path to match where you've placed this server.

## License

[Unlicense](LICENSE) - Public Domain
