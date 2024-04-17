import re


def extract_emails(text):
    email_pattern = re.compile(r'[\w.-]+@\w+\.\w+')
    return email_pattern.findall(text)


example_text = "Contact us at info@example.com or support@example.com for assistance. test.test_test-test@example.com"

emails = extract_emails(example_text)
print(emails)
