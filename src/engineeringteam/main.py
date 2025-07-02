#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from engineeringteam.crew import Engineeringteam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
A simple cash-flow tracker for rental properties.
The system should allow users to register a property, storing an auto-generated UUID, address, purchase price, optional monthly mortgage payment, and a start date that defaults to today.
The system should allow users to record income events (type = “rent” or “other”, amount, date, notes) and expense events (category, amount, date, notes), each linked to a property.
The system should calculate the net cash flow for any property for a given month or year.
The system should calculate the cash-on-cash return for a property for a given year, based on the net cash flow and the initial cash invested.
The system should summarize the entire portfolio, reporting totals across all properties.
The system should list the full ledger of cash-flow events for a property, optionally filtered by a start and end date.
The system should export a property’s ledger to a CSV file at a user-supplied path.
The system should reject negative amounts (expenses are recorded as positive numbers) and disallow events dated before the property’s start date.
The system stores everything in memory for version 1, uses uuid.uuid4() for IDs and datetime.date for dates, and ignores currency conversions.
"""
module_name = "rentals.py"
class_name = "PropertyManager"

def run():
    """
    Run the crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = Engineeringteam().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        Engineeringteam().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Engineeringteam().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        Engineeringteam().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()
