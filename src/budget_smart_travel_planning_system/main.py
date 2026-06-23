#!/usr/bin/env python
import sys
import asyncio
from budget_smart_travel_planning_system.crew import BudgetSmartTravelPlanningSystemCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

async def run():
    """
    Run the crew.
    """
    destination = input("Enter destination: ")
    budget = float(input("Enter budget (USD): "))
    duration = int(input("Enter trip duration (days): "))
    departure_location = input("Enter departure location: ")
    travel_dates = input("Enter travel dates: ")
    preferences = input("Enter travel preferences: ")

    inputs = {
        'destination': destination,
        'budget': budget,
        'duration': duration,
        'departure_location': departure_location,
        'travel_dates': travel_dates,
        'preferences': preferences
    }
    return await BudgetSmartTravelPlanningSystemCrew().crew().kickoff_async(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'destination': 'sample_value',
        'departure_location': 'sample_value',
        'travel_dates': 'sample_value',
        'preferences': 'sample_value',
        'budget': 'sample_value',
        'duration': 'sample_value'
    }
    try:
        BudgetSmartTravelPlanningSystemCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        BudgetSmartTravelPlanningSystemCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'destination': 'sample_value',
        'departure_location': 'sample_value',
        'travel_dates': 'sample_value',
        'preferences': 'sample_value',
        'budget': 'sample_value',
        'duration': 'sample_value'
    }
    try:
        BudgetSmartTravelPlanningSystemCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        asyncio.run(run())
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
