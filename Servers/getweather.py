from mcp.server.fastmcp import FastMCP

from Servers.functions.weather_operations import get_weather



mcp = FastMCP()



@mcp.tool()

def get_weather_mcp(location: str) -> str:

    """

    Fetches the weather information for the given location.

    

    Args:

        location: The name of the city or location to get the weather for.

    

    Returns:

        A string containing the weather details or an error message.

    """

    try:

        return get_weather(location)

    except Exception as e:

        return f"Error fetching weather: {str(e)}"