from pydantic import BaseModel
from typing import List

# Input/Output models for tools

class FindPrimeNumbersInput(BaseModel):
    a: List

class FindPrimeNumbersOutput(BaseModel):
    result: List

class GetLargestNumberInput(BaseModel):
    a: List

class GetLargestNumberOutput(BaseModel):
    result: int

class ExcludeNumberInput(BaseModel):
    a: List
    b: int

class ExcludeNumberOutput(BaseModel):
    result: List


