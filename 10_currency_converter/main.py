# %%
import json

# 1. Load the data
def load_exchange_rates() -> dict[str, float]:
    with open('currencies.json', 'r') as file:
        return json.load(file)


# 2. Create instructions
def instructions() -> None:
    print('1. Type <amount><CURRENCY>, e.g. 10USD, to convert a currency.')
    print('2. Type LIST to list available currencies.')
    print('3. Type PRINT to show the last conversion.')
    print('4. Type QUIT to exit.')


def convert(user_input: str, rates: dict[str, float]) -> dict[str, float] | None:
    # Prepare data
    currency_codes: list[str] = list(rates.keys())
    input_currency_code: str = user_input[-3:]  # Gets the last three characters of a string

    # Check whether the user specifies a valid currency
    if input_currency_code not in currency_codes:
        print(f'Currency code: "{input_currency_code}" is invalid.')
        return

    # Check whether the user specifies a valid amount
    try:
        input_amount: float = float(user_input[:-3])  # Gets everything besides the last three characters
    except ValueError:
        print(f'"{user_input}" is invalid. Try something like: "10 AUD"')
        return

    # Base conversion - USD is the base currency in the file so any currency we specify
    # will be converted to that first.
    base_conversion: float = input_amount / rates.get(input_currency_code)

    # Build dictionary
    out_dict: dict[str, float] = {
        currency_code: base_conversion * rates.get(currency_code)
        for currency_code in currency_codes
    }
    return out_dict


def print_dict(input_dict:dict[str, float]) -> None:
    print('*' * 20)
    for key, value in input_dict.items():
        print(f'{key}: ${value}')

    # Display the conversion
    # print(f'{round(input_amount, 2):>16} {input_currency_code}')
    # print('-' * 20)
    # for currency_code in currency_codes:
    #     converted_amount: float = base_conversion * rates[currency_code]
    #     print(f'= {round(converted_amount, 2):>14} {currency_code}')
    # print('-' * 20)


def main() -> None:
    # 1. Display instructions
    instructions()

    # 2. Load exchange rate data
    exchange_rates: dict[str, float] = load_exchange_rates()

    # 3. Run
    database: dict[str, float] | None = None
    while True:
        user_input: str = input('Convert: ').upper().strip()

        if user_input == 'LIST':
            print(f'Available currencies: {', '.join(exchange_rates.keys())}')
            continue
        elif user_input == 'PRINT':
            if database:
               print_dict(database)
            else:
                print('User must convert a currency')
        elif user_input == 'QUIT':
            print('Exiting.')
            break

        database = convert(user_input, exchange_rates)

if __name__ == '__main__':
    main()

# Homework:
# 1. Split "convert()" into two functions: this shit hard and boring
# - One that returns all the conversions as a dictionary.
# - One that displays the converted data.
