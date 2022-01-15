import requests

import config

BASE_URL = "https://trackapi.nutritionix.com/v2"


def analyze_exercise(input: str):
    """
    https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise

    :returns
        {
            'exercises': [
                {'tag_id': 317, 'user_input': 'ran', 'duration_min': 30, 'met': 9.8, 'nf_calories': 343, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}
            ]
        }
    """
    url = f"{BASE_URL}/natural/exercise"
    headers = {
        "x-app-id": config.APP_ID,
        "x-app-key": config.APP_SECRET
    }
    res = requests.post(url, json={
        "query": input
    }, headers=headers)
    res.raise_for_status()
    example = {
        'exercises': [
            {'tag_id': 317, 'user_input': 'ran', 'duration_min': 30, 'met': 9.8, 'nf_calories': 343,
             'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg',
                       'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg',
                       'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None,
             'benefits': None}
        ]
    }
    return res.json()
