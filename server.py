"""MCP server to read image files and return as base64."""

import base64
import mimetypes
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("boecht/read-image")


@mcp.tool()
def read_image(file_path: str) -> dict:
    """Read an image file and return its contents as base64.

    Args:
        file_path: Absolute path to the image file.

    Returns:
        Dictionary with base64 data, file size, and mime type.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Not a file: {file_path}")

    data = path.read_bytes()
    mime_type, _ = mimetypes.guess_type(file_path)

    return {
        "data": base64.b64encode(data).decode("ascii"),
        "size_bytes": len(data),
        "mime_type": mime_type or "application/octet-stream",
    }


if __name__ == "__main__":
    mcp.run()
