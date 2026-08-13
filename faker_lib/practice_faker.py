# let get into faker mode😁
import pandas as pd
import numpy as np
from faker import Faker

print("Practice faker...!")

fake = Faker(locale='en_US')

job_list = ['Web_dev', 'Front_end_dev', 'Full_stack_dev', 'Back_end_dev', 'App_dev', 'Manager']

first_name = [(lambda: fake.first_name())()for _ in range(10)]
last_name = [(lambda: fake.last_name())() for _ in range(10)]
email = [(lambda: fake.email())() for _ in range(10)]

# mob = [(lambda: fake.phone_number())() for _ in range(10)]
# mob = [(lambda: fake.msisdn())() for _ in range(10)]
# mob = [(lambda: fake.numerify(text='+01##########'))() for _ in range(10)]
mob = [(lambda: fake.bothify(text='+91-##########'))() for _ in range(10)]

job = [(lambda: fake.random_element(elements=job_list))() for _ in range(10)]
city = [(lambda: fake.city())() for _ in range(10)]

salary = [(lambda: fake.random_int(min=20000, max=100000, step=20000))() for _ in range(10)]

df = pd.DataFrame({'FIRST_NAME' : first_name, 'LAST_NAME': last_name, 'EMAIL' : email,'MOB' : mob,
                   'SALARY': salary, 'JOB': job, 'CITY': city})

print(df.info())



