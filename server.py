import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from pdf_converter import convert_to_markdown, create_pdf_converter

mcp = FastMCP()


APP_HOME = Path(os.getenv("APP_HOME", Path(__file__).parent))
DATA_DIR = APP_HOME / "data"


doc_converter = create_pdf_converter()


@mcp.tool()
def get_document_text(filename: str) -> str:
    """
    Use this tool to get the content of a document given its filename.

    Args:
        filename (str): The filename of the document to get.

    Returns:
        str: The content of the document in Markdown format.
    """
    doc_path = DATA_DIR / filename
    return convert_to_markdown(doc_path, doc_converter)


@mcp.tool()
def get_document_list() -> list[str]:
    """
    Use this tool to get the list of documents.

    Returns:
        list[str]: The list of document filenames.
    """
    return sorted([str(path.name) for path in DATA_DIR.glob("*.pdf")])


if __name__ == "__main__":
    mcp.run(transport="stdio")
