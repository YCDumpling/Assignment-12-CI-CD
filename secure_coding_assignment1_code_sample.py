"""
A sample script demonstrating secure coding practices:
User input, data fetching, database insertion, and emailing.
"""

import os
from urllib.request import urlopen

import pymysql

db_config = {
    "host": "mydatabase.com",
    "user": "admin",
    "password": "secret123",
}


def get_user_input():
    """
    Prompt the user for their name and return it as a string.
    """
    return input("Enter your name: ")


def get_data():
    """
    Fetch data from an API endpoint and return it as a string.
    """
    url = "http://insecure-api.com/get-data"
    data = urlopen(url).read().decode()
    return data



def send_email(to, subject, body):
    """
    Send an email using a system mail command.

    Args:
        to (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
    """
    os.system(f'echo "{body}" | mail -s "{subject}" {to}')


def main():
    """
    Main function to gather user input, fetch data, save it to DB, and send an email.
    """
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email("admin@example.com", "User Input", user_input)


if __name__ == "__main__":
    main()
