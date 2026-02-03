"""MCP server to read image files and return them as viewable content."""

import json
import mimetypes
from pathlib import Path
from typing import Annotated

from mcp.server.fastmcp import FastMCP, Image

mcp = FastMCP("boecht/read-image")


@mcp.tool(annotations={"readOnlyHint": True})
def read_image(
    file_path: Annotated[str, "Absolute path to the image file"],
) -> list:
    """Read an image file from the filesystem and return its contents.

    Args:
        file_path: Absolute path to the image file.

    Returns:
        Multipart content containing JSON metadata and image content.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Not a file: {file_path}")

    # Get file metadata
    file_size = path.stat().st_size
    mime_type, _ = mimetypes.guess_type(file_path)

    metadata = {
        "fileName": path.name,
        "filePath": str(path),
        "mimeType": mime_type or "application/octet-stream",
        "sizeBytes": file_size,
    }

    # Return multipart content: metadata JSON + image
    return [json.dumps(metadata), Image(path=path)]


if __name__ == "__main__":
    mcp.run()
