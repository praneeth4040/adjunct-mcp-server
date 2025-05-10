import os
from mcp.server.fastmcp import FastMCP
from Servers.functions.file_operations import get_file, search_file, copy_file, delete_file

mcp = FastMCP()

@mcp.tool()
def get_file_mcp(file_path: str) -> str:
    """
    Gets a file from the file path and returns the file object.
    Args:
        file_path: The path of the file to get.
    Returns:
        The file object.
    """
    try:
        return  get_file(file_path)
    except Exception as e:
        return f"Error reading file: {str(e)}"

@mcp.tool()
def search_file_mcp(file_name: str , extension: str , search_dir: str) -> str:
    """Searches for a file by name and returns the file path if found.
    Args:
        file_name: The name of the file to search for.
        extension: The extension of the file to search for.
        search_dir: The directory to search for the file in.
    Returns:
        The file path if found, otherwise a message indicating the file was not found.
    """
    try:
        path = search_file(file_name, extension, search_dir)
        return path if path else "File not found."
    except Exception as e:
        return f"Error searching file: {str(e)}"

@mcp.tool()
def copy_file_mcp(source_path: str, destination_path: str) -> str:
    """Copies a file from the source path to the destination path.
    Args:
        source_path: The path of the file to copy.
        destination_path: The path to copy the file to.
    Returns:
        A message indicating the file was copied successfully.
    """
    try:
        return copy_file(source_path, destination_path)
    except Exception as e:
        return f"Error copying file: {str(e)}"

@mcp.tool()
def delete_file_mcp(file_path: str) -> str:
    """Deletes a file from the file path.
    Args:
        file_path: The path of the file to delete.
    Returns:
        A message indicating the file was deleted successfully.
    """
    try:
        return delete_file(file_path)
    except Exception as e:
        return f"Error deleting file: {str(e)}"
