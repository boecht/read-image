"""MCP server to read image files."""

import mimetypes
from pathlib import Path

from mcp.server.fastmcp import FastMCP, Image

mcp = FastMCP("boecht/read-image")


@mcp.tool()
def read_image(file_path: str) -> Image:
    """Read an image file from the filesystem and return its contents.

    Args:
        file_path: Absolute path to the image file.

    Returns:
        Image content that can be displayed by the AI agent.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Not a file: {file_path}")

    data = path.read_bytes()
    mime_type, _ = mimetypes.guess_type(file_path)

    return Image(data=data, format=mime_type or "image/png")


if __name__ == "__main__":
    mcp.run()
