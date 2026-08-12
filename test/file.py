import pandas as pd
import numpy as np
import random

df = pd.read_csv('test/employee_data.csv')

df = df.fillna({
    'EMAIL': df['FIRST_NAME'].str.upper().str[0] + df['LAST_NAME'].str.upper(),
    'PHONE_NUMBER': str(random.randint(101, 999)) + "." + str(random.randint(101, 999)) + "." + str(random.randint(101, 999))
    })

print(df.info())
group = df.groupby("JOB_ID")

print(group["JOB_ID"].count())
