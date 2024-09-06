import mysql.connector

def check_credentials(email, password):
    # Establish connection to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",       # your MySQL host
        user="root",            # your MySQL username
        password="Hardik50",# your MySQL password
        database="face_recognizer"  # your database name
    )

    cursor = connection.cursor()

    # Query to select the user data
    query = "SELECT password FROM register WHERE email = %s"
    cursor.execute(query, (username,))

    # Fetch the result
    result = cursor.fetchone()

    # Close the database connection
    cursor.close()
    connection.close()

    if result:
        # Compare the entered password with the stored password
        if password == result[0]:
            return True  # Correct username and password
        else:
            return False  # Incorrect password
    else:
        return False  # Username not found

# Example usage
username = input("Enter username: ")
password = input("Enter password: ")

if check_credentials(username, password):
    print("Login successful!")
else:
    print("Invalid username or password.")
