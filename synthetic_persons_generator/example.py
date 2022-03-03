#----------------------------------------------------------------------------
# Created By  : Henry Dalton
# Created Date: 29/12/2021
# version ='1.0'
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------

import random
import pandas as pd
from faker import Faker
fake = Faker()




def get_sample_from_distribution(n_samples: int, distribution: dict):
    """Wrapper around random.choices given a formatted distribution dic of {value: weight, ...}"""
    values = list(distribution.keys())
    weights = distribution.values()
    sample = random.choices(values, weights=weights, k=n_samples)
    return sample

def fake_persons_dataframe(num_people, standard_fields=None, custom_dict={}):

    fake_persons_list = []

    for person in range(num_people):
        customer = fake.profile(standard_fields)
        print(customer)
        customer["customer_id"] = person + 1
        fake_persons_list.append(customer)

    df = pd.DataFrame(fake_persons_list)
    df = df.rename(columns={"name": "customer_name"})
    # Get categorical
    for category in custom_dict:
        df[category] = get_sample_from_distribution(
            n_samples=len(df),
            distribution=custom_dict[category])





    return df



# pd.set_option('display.max_columns', 5)
# print(fake_persons_dataframe(5, ['name', 'ID', 'age', 'location'], {'name' : ['bob', 'joe', 'frank', 'sally', 'dude'], 'ID' : [111, 222, 333, 444, 555], 'age' : [35, 45, 65, 72, 42], 'location' : ['CA', 'OR', 'NY', 'WA', 'TX']}))
# print(fake_persons_dataframe(5))

customers_df = fake_persons_dataframe(
    num_people=100,
    standard_fields=["name", "address", "mail"],
    custom_dict={
        "sex": {"Male": 52, "Female": 48},
        "MI": {"A": 50, "I": 25, "R": 25}
    }
    )

# print(customers_df)
print(customers_df.head().T)
