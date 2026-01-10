# for each file in the data folder, remove the 'Unnamed: 0' column and save the cleaned data to a new folder
import pandas as pd
import os
# for each *csv and *json in this directory

# directory of this file
thisFile = os.path.dirname(__file__)
for file in os.listdir(thisFile):
    data = None
    filePath = os.path.join(thisFile, file)
    if file.endswith('.csv'):
        data = pd.read_csv(filePath)
    elif file.endswith('.json'):
        data = pd.read_json(filePath)
    else:
        continue

    # remove the 'Unnamed: 0' column if it exists
    if 'Unnamed: 0' in data.columns:
        data = data.drop('Unnamed: 0', axis=1)
        
        if file.endswith('.csv'):
            data.to_csv(filePath, index=False)
        elif file.endswith('.json'):
            data.to_json(filePath, orient='records', index=False)
    # save the cleaned data to a new folder

    os.makedirs('cleaned_data', exist_ok=True)

    