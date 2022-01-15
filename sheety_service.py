import requests

import config

BASE_URL = "https://api.sheety.co/022c0e25ee3adc65cedc67dc65f372d6/workouts/workouts"


def create_workout_row(date: str, time: int, exercise: str, duration: int, calories: float):
    res = create_row({"date": date, "time": time, "exercise": exercise, "duration": duration, "calories": calories})
    res.raise_for_status()
    print(res.json())
    return res.json()


def create_row(**kwargs):
    """Column names are lowercase"""
    res = requests.post(BASE_URL, json={
        "workout": kwargs
    }, headers={
        "Authorization": f"Bearer {config.SHEETY_TOKEN}"
    })
    res.raise_for_status()
    print(res.json())
    return res.json()
