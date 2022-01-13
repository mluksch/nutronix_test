import pandas as pd

import nutrition_service

# result = nutrition_service.analyze_exercise(input=input("What was your exercise today?\n"))
result = nutrition_service.analyze_exercise(input="I run 5km and cycled for 30mins and swim for 10 mins")
df = pd.DataFrame.from_records(data=result["exercises"])
for idx, row in df.iterrows():
    print(f"You burnt {row.nf_calories} calories by {row.name} for {row.duration_min} minutes.")
print(f"You have burnt {df.nf_calories.sum()} in total.")
