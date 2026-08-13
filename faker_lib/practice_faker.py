# let get into faker mode😁
import pandas as pd
import numpy as np
from faker import Faker

print("Practice started...!")

fake = Faker()

names = [(lambda: fake.name())()for _ in range(10)]
email = [(lambda: fake.email())() for _ in range(10)]
mob = [(lambda: fake.phone_number())() for _ in range(10)]

df = pd.DataFrame({'Name' : names,'EMAIL' : email,'MOB' : mob})

print(df.to_string)



