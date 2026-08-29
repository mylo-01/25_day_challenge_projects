import re
from collections import Counter


def extract_emails(
    text: str, unique_only: bool = True, case_sensitive: bool = True, top_domain_only: bool = False
) -> list[str]:
    # Comprehensive email regex pattern
    email_pattern: str = (
        r'\b[A-Za-z0-9.!#$%&\'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?'
        r'(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*\.[A-Za-z]{2,}\b'
    )

    # Find all email addresses
    emails: list[str] = re.findall(email_pattern, text)

    if top_domain_only:
        #me lo robé a la chingada todo de la ai
        domain_counts = Counter(email.rsplit('@', 1)[-1] for email in emails)
        top_3_domains = set(domain for domain, _ in domain_counts.most_common(3))
        emails = [email for email in emails if email.rsplit('@', 1)[-1] in top_3_domains]

    if not case_sensitive:
        emails = [email.lower() for email in emails]

    if unique_only:
        # Remove duplicates while preserving order
        emails = list(dict.fromkeys(emails))

    return emails


def list_emails(path: str) -> None:
    emails: list[str] = []

    # Also show that this works with website source code
    with open(path, 'r') as f:
        text: str = f.read()
        emails = extract_emails(text)

    if emails:
        for email in emails:
            print(email)
    else:
        print('No emails found...')


def main() -> None:
    list_emails('file.txt')


if __name__ == '__main__':
    main()


# Homework:
# 1. Add an option that filters out all the lesser-known domains and keeps only
# the most popular ones (gmail, yahoo, etc, etc.)
