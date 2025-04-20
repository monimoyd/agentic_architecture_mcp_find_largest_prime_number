# basic import 
from mcp.server.fastmcp import FastMCP, Image
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from mcp import types
from PIL import Image as PILImage
import math
import sys
import time
from models import FindPrimeNumbersInput, FindPrimeNumbersOutput, GetLargestNumberInput, GetLargestNumberOutput, ExcludeNumberInput, ExcludeNumberOutput


# instantiate an MCP server client
mcp = FastMCP("PrimeNumberCalculator")

# DEFINE TOOLS

#addition tool
@mcp.tool()
def find_prime_numbers(input: FindPrimeNumbersInput) -> FindPrimeNumbersOutput:
    """
    Given a list of numbers, find which are prime numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of prime numbers from the input list.
    """

    prime_numbers = []
    for number in input.a:
        if number > 1:  # Prime numbers are greater than 1
            is_prime = True
            for i in range(2, int(number**0.5) + 1):  # Check divisibility up to the square root
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(number)
    return FindPrimeNumbersOutput(result=prime_numbers)

@mcp.tool()
def find_largest(input: GetLargestNumberInput) -> GetLargestNumberOutput:
    """
    Given a list of numbers, find the largest integer.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: A list of prime numbers from the input list.
    """

    return GetLargestNumberOutput(result=max(input.a))

@mcp.tool()
def exclude_number(input: ExcludeNumberInput) -> ExcludeNumberOutput:
    """
    Given a list of numbers, exclude a given input by removing from list of numbers if present.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: A list of numbers by excluding a given input
    """
    if input.b in input.a:
        input.a.remove(input.b)

    return ExcludeNumberOutput(result=input.a)
    
@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING THE SERVER AT AMAZING LOCATION")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  # Run with stdio for direct execution
