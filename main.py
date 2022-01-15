import datetime

import pandas as pd

import nutrition_service
import sheety_service

# result = nutrition_service.analyze_exercise(input=input("What was your exercise today?\n"))
result = nutrition_service.analyze_exercise(input="I run 5km and cycled for 30mins and swim for 10 mins")
df = pd.DataFrame.from_records(data=result["exercises"])
# {'tag_id': 317, 'user_input': 'ran', 'duration_min': 30, 'met': 9.8, 'nf_calories': 343, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}
now = datetime.datetime.now()
df["date"] = now.strftime("%d.%m.%Y")
df["time"] = now.strftime("%H:%M:%S")
df.rename(columns={
    "name": "exercise", "duration_min": "duration", "nf_calories": "calories"
}, inplace=True)
print(df)

# import tabular data via sheety to google sheets:
# Date	Time	Exercise	Duration	Calories
for idx, row in df[["date", "time", "exercise", "duration", "calories"]].iterrows():
    sheety_service.create_row(**row.to_dict())
