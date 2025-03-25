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
    with urlopen("http://insecure-api.com/get-data") as response:
        data = response.read().decode()
    return data


def save_to_db(data):
    """
    Insert data into a sample table in the database.

    Args:
        data (str): Data to be stored in the database.
    """
    # Safer parameterized query to avoid SQL injection
    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    with pymysql.connect(**db_config) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (data, "Another Value"))
        connection.commit()


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
