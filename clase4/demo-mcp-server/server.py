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


@mcp.prompt()
def explain_tool_usage() -> dict:
    """
    Prompt template to explain how the demo MCP tools work.

    Returns
    -------
    dict
        A prompt definition compatible with MCP prompt handling, containing
        one or more messages to guide the model.
    """
    return {
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an assistant that explains how to use the MCP demo "
                    "server tools: add, subtract, and repeat_message. "
                    "Give short, clear examples for each tool."
                ),
            }
        ]
    }


@mcp.prompt()
def math_coach(operation: str, a: int, b: int) -> dict:
    """
    Prompt template to guide the model as a math coach.

    Parameters
    ----------
    operation : str
        The arithmetic operation to explain (e.g., 'add', 'subtract').
    a : int
        First operand.
    b : int
        Second operand.

    Returns
    -------
    dict
        A prompt definition instructing the model to explain the requested
        arithmetic operation step by step.
    """
    return {
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a friendly math coach. Explain operations step by "
                    "step and keep the tone simple and didactic."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Explain how to {operation} the numbers {a} and {b}, and "
                    "then give the final result."
                ),
            },
        ]
    }
