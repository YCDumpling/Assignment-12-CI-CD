import os
import pymysql
from urllib.request import urlopen

db_config = {
    "host": "mydatabase.com",
    "user": "admin",
    "password": "secret123",
}


def get_user_input():
    """
    Prompt the user for their name.

    Returns:
        str: The name entered by the user.
    """
    return input("Enter your name: ")


def send_email(to, subject, body):
    """
    Send an email using a system mail command.

    Args:
        to (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
    """
    os.system(f'echo "{body}" | mail -s "{subject}" {to}')


def get_data():
    """
    Fetch data from an API endpoint and return it as a string.

    Returns:
        str: The fetched data.
    """
    url = "http://insecure-api.com/get-data"
    data = urlopen(url).read().decode()
    return data


def save_to_db(data):
    """
    Insert the given data into the database.

    Args:
        data (str): Data to be stored in the database.
    """
    query = (
        "INSERT INTO mytable (column1, column2) "
        f"VALUES ('{data}', 'Another Value')"
    )
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute(query)
    connection.commit()
    connection.close()


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
