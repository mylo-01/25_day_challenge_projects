# Imports
import re
# Constants
# %%
# If from km to miles, multiply, else divide
MILES_TO_KILOMETERS = 1.609344

KM_PATTERN = re.compile(r"(\d+)\s*km", re.IGNORECASE)
MILES_PATTERN = re.compile(r"(\d+)\s*miles", re.IGNORECASE)


print('Hello')
distance = input('Enter the lenght \n(sufix with km for "kilometers" \n and miles for "miles"): ')
# print(f'You entered: {distance}')

# %%
# Calculations.
km_object = KM_PATTERN.search(distance)
miles_object= MILES_PATTERN.search(distance)

if km_object:
   output, unit = (float(km_object.group(1)) / MILES_TO_KILOMETERS), 'Miles'
elif miles_object:
    output, unit = (float(miles_object.group(1)) * MILES_TO_KILOMETERS), 'Kilometers'
else:
    output, unit = None, None

print(f'Your distance converted is: \n {output:.3f} {unit}') if output else print('Wrong input, read instructions carefully')
