import string


# 1. Create the blueprint
class PasswordValidator:
    def __init__(self) -> None:
        self.common_passwords: set[str] = self.load_common_passwords()

    @staticmethod
    def load_common_passwords() -> set[str]:
        with open('common_passwords.txt', 'r') as file:
            return {line.strip() for line in file if line}

    def is_common(self, password: str) -> bool:
        return password in self.common_passwords

    @staticmethod
    def char_rep(password:str  ) -> bool:
        last_char:str|None = None
        for char in password:
            if last_char is not None:
                if last_char[-1] == char:
                    last_char = last_char+char
                    if len(last_char) == 3:
                        return True
                else:
                    last_char = char
            else:
               last_char = char
        return False

    def rate(self, password: str) -> tuple[dict[str, bool], bool]:
        ref_dict = {
            'upper' : False,
            'punctuation' : False,
            'length' : False,
            'numbers' : False
        }
        repetition_flag: bool = False

        if self.is_common(password):
            return ref_dict, repetition_flag


        # Calculate score
        # score: int = 0
        if any(c.isupper() for c in password):  # Checks for uppercase characters
            ref_dict['upper'] = True

        if any(c in string.punctuation for c in password):  # Checks for punctuation
            ref_dict['punctuation'] = True

        if len(password) >= 10:  # Checks length
            ref_dict['length'] = True

        if any(c.isdigit() for c in password):
            ref_dict['numbers'] = True

        if self.char_rep(password):
            repetition_flag = True
        # Return rating
        return ref_dict, repetition_flag

# 2. Check for password
def main() -> None:
    # Link: https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt
    validator: PasswordValidator = PasswordValidator()
    print('🔒 Welcome to the Password Strength Checker!')
    print('Enter a password to get a quality rating.')

    while True:
        password: str = input('Enter password: ').strip()
        score, rep_flag = validator.rate(password)
        rating = sum(value for key, value in score.items())
        if rating == 4:
            print('✅ Your password is secure! ')
        elif rating <= 3:
            print('⚠️ Your password is of medium strength.')
            if rating == 0:
                print('⚠️ That password sucks!')
                print('Try adding symbols, uppercase letters, and increasing the length.')
            print('Your are missing:')
            print(f'{[key for key, value in score.items() if not value]}')
        if rep_flag:
            print('Also, too many repeating chars, you should probably fix that')


if __name__ == '__main__':
    main()

# Homework:
# 1. Add functionality that tells the user exactly what they are missing to make their password
# stronger, such as symbols, uppercase characters, and/or more characters.
# 2. Add functionality that detects when a user adds too many sequential characters, such
# as "aaa", "111", and so on.
# 3. Check if the password contains digits as well to reach the 'secure' rating.
