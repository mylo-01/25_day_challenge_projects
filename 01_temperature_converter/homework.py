import re

# Constants
MILES_TO_KILOMETERS = 1.609344

# Updated regex to support decimals (e.g., "1.5 km")
KM_PATTERN = re.compile(r"(\d+(?:\.\d+)?)\s*km", re.IGNORECASE)
MILES_PATTERN = re.compile(r"(\d+(?:\.\d+)?)\s*miles?", re.IGNORECASE)

print('Hello')
distance = input('Enter the length \n(suffix with "km" for kilometers \nor "miles" for miles): ')

# Calculations
km_match = KM_PATTERN.search(distance)
miles_match = MILES_PATTERN.search(distance)

output = None
unit = None

if km_match:
    output = float(km_match.group(1)) / MILES_TO_KILOMETERS
    unit = 'Miles'
elif miles_match:
    output = float(miles_match.group(1)) * MILES_TO_KILOMETERS
    unit = 'Kilometers'

# Check against None to avoid the "0" bug
if output is not None:
    print(f'Your distance converted is:\n{output:.3f} {unit}')
else:
    print('Wrong input, read instructions carefully.')
