import os

from fastmcp import FastMCP

mcp = FastMCP("Calculator MCP Server")


@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers and return the sum."""
    return a + b


@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the difference."""
    return a - b


@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers and return the product."""
    return a * b


@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide a by b and return the quotient. Raises an error if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    # Locally this runs over stdio (e.g. for Claude Desktop).
    # When deployed to a host that sets PORT (Render, Railway, Fly.io, etc.)
    # it switches to streamable-http so it's reachable over the network.
    port = os.environ.get("PORT")
    if port:
        mcp.run(transport="streamable-http", host="0.0.0.0", port=int(port))
    else:
        mcp.run()
