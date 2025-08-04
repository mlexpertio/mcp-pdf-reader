# MCP PDF Reader

A Model Context Protocol (MCP) server that provides tools for reading and processing PDF documents. Built with Docling for document conversion and text extraction.

## Features

- **MCP Server** with tools for PDF document processing
- **Document Text Extraction**: Convert PDF content to clean Markdown format
- **Document Discovery**: List and access available PDF files

## Tools

The server provides two main tools:

- **`get_document_list`**: Returns a list of all available PDF files in the data directory
- **`get_document_text`**: Extracts and returns the full text content of a specified PDF file in Markdown format

## Install

Make sure you have [`uv` installed](https://docs.astral.sh/uv/getting-started/installation/).

Clone the repository:

```bash
git clone git@github.com:mlexpertio/mcp-pdf-reader.git
cd mcp-pdf-reader
```

Install Python:

```bash
uv python install 3.12.10
```

Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate
```

Install dependencies:

```bash
uv sync
```

## Usage

### Add PDF Documents

Place your PDF files in the `data/` directory. The server will automatically detect and make them available through the tools.

### Run MCP Server

Start the MCP server:

```bash
python server.py
```

The server runs using stdio transport and can be integrated with any MCP-compatible client.

### Development and Testing

Use the MCP inspector to test the server:

```bash
mcp dev server.py
```

This will open a web interface where you can test the available tools and inspect their responses.

## Use in VSCode/Cursor

You can use the MCP integration in your editor. `Tools & Integrations` -> `New MCP Server` and edit the `mcp.json` file to include the following:

```json
{
  "mcpServers": {
    "pdf-reader": {
      "command": "/opt/homebrew/bin/uv", // path to your uv binary
      "args": ["run", "--directory", "PATH_TO_YOUR_PROJECT", "server.py"]
    }
  }
}
```

## License

See LICENSE file for details.
