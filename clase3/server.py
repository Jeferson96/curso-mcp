"""Demo MCP server for basic arithmetic tools and greeting resources.

This module defines a minimal MCP server using ``FastMCP`` with:

- arithmetic tools (`add`, `subtract`)
- a simple text utility tool (`repeat_message`)
- dynamic resources for greetings and farewells (`greeting://{name}`, `farewell://{name}`)

The goal is to provide small, clear examples that can be used to learn how
to build and document MCP servers following good practices.
"""

from mcp.server.fastmcp import FastMCP

# Create an MCP server instance with a human‑readable name.
mcp = FastMCP("Demo MCP Server")


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two integer numbers.

    Parameters
    ----------
    a : int
        First addend.
    b : int
        Second addend.

    Returns
    -------
    int
        The sum of ``a`` and ``b``.
    """
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    Subtract one integer from another.

    Parameters
    ----------
    a : int
        Minuend (number to subtract from).
    b : int
        Subtrahend (number that is subtracted).

    Returns
    -------
    int
        Result of ``a - b``.
    """
    return a - b


@mcp.tool()
def repeat_message(message: str, times: int = 1) -> str:
    """
    Repeat a message a given number of times, separated by spaces.

    Parameters
    ----------
    message : str
        Text to repeat.
    times : int, optional
        How many times to repeat the message, by default 1.

    Returns
    -------
    str
        The repeated message.

    Raises
    ------
    ValueError
        If ``times`` is less than 1.
    """
    if times < 1:
        raise ValueError("times must be at least 1")
    return " ".join([message] * times)


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """
    Get a personalized greeting message for the given name.

    Parameters
    ----------
    name : str
        Name of the person to greet.

    Returns
    -------
    str
        Greeting message including the given name.
    """
    return f"Hello, {name}!"


@mcp.resource("farewell://{name}")
def get_farewell(name: str) -> str:
    """
    Get a personalized farewell message for the given name.

    Parameters
    ----------
    name : str
        Name of the person to say goodbye to.

    Returns
    -------
    str
        Farewell message for the given name.
    """
    return f"Goodbye, {name}! See you soon."
