
"""
"""
from collections import Counter


def get_domain(email_address: str) -> str:
    return email_address.lower().split('@')[-1]

assert get_domain('imranshah@gmail.com') == 'gmail.com'



with open('fake_emails.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
    for line in f
    if "@" in line)
    print(domain_counts)