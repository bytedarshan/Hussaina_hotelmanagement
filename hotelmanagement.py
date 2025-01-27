import mysql.connector
import random
from tabulate import tabulate

# Establishing the connection with the MySQL database
mycon = mysql.connector.connect(
    host="localhost",
    user="root",
    password="useradmin@100",
    database="hotel_management"
)

def main_menu():
    print("\n--- Welcome to Hotel Taj, Ooty ---")
    print("1. Book a Room")
    print("2. Get Total Bill")
    print("3. Change Package")
    print("4. Search Customer Details")
    print("5. Cancel Booking")
    print("6. Show All Bookings")
    print("7. Exit")

def book_room():
    print("\n--- Room Booking ---")
    name = input("Enter your name: ")
    country = input("Enter your country: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    aadhar = input("Enter your Aadhar number: ")
    checkin_date = input("Enter check-in date (YYYY-MM-DD): ")
    checkout_date = input("Enter check-out date (YYYY-MM-DD): ")
    days = int(input("Enter number of days for your stay: "))
    customer_id = random.randint(1000, 9999)
    print(f"\nYour Customer ID is: {customer_id}")
   
    # Insert customer details into the customer_details table
    cursor = mycon.cursor()
    customer_query = """
        INSERT INTO customer_details (C_ID, C_name, country, C_email, C_phone_no, C_aadhar)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(customer_query, (customer_id, name, country, email, phone, aadhar))
    mycon.commit()
   
    # Room selection as done in change_package function
    print("\n--- Available Packages ---")
    print("1. PACK1: King Room, Indian veg cuisine with dessert, Bowling")
    print("2. PACK2: Deluxe Room, Chinese veg with dessert, VR")
    print("3. PACK3: Premier Room, Chinese veg and non-veg with dessert, Table Tennis and VR")
   
    package_choice = int(input("\nSelect a package (1, 2, or 3): "))
    room_choices = {1: "King Room", 2: "Deluxe Room", 3: "Premier Room"}
   
    # Define room rents and other details for each package
    package_details = {
        1: {"room_rent": 10000, "cuisine": "Indian veg with dessert", "cuisine_bill": 6000, "game": "Bowling", "game_bill": 350},
        2: {"room_rent": 15000, "cuisine": "Chinese veg with dessert", "cuisine_bill": 9000, "game": "VR", "game_bill": 500},
        3: {"room_rent": 25000, "cuisine": "Chinese veg and non-veg with dessert", "cuisine_bill": 14000, "game": "Table Tennis and VR", "game_bill": 900},
    }
   
    if package_choice in package_details:
        room_choice = room_choices[package_choice]
        details = package_details[package_choice]
       
        print(f"\nYou selected {room_choice} with the following package details:")
        print(f"Room Rent: {details['room_rent']}")
        print(f"Cuisine: {details['cuisine']}")
        print(f"Gaming: {details['game']}")
       
        # Generate a random room number
        room_no = random.randint(100, 999)
        print(f"Your Room Number is: {room_no}")

        # Insert booking records into the booking_records table
        booking_query = """
            INSERT INTO booking_records (C_ID, checkin_date, checkout_date, room_no, no_of_days)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(booking_query, (customer_id, checkin_date, checkout_date, room_no, days))
        mycon.commit()

        # Insert package details into the rooms table for the selected room
        room_query = """
            INSERT INTO rooms (C_ID, room_choice, room_rent)
            VALUES (%s, %s, %s)
        """
        cursor.execute(room_query, (customer_id, room_choice, details['room_rent']))
        mycon.commit()

        # Insert restaurant and gaming details
        restaurant_query = """
            INSERT INTO restaurent (C_ID, cuisine, bill)
            VALUES (%s, %s, %s)
        """
        cursor.execute(restaurant_query, (customer_id, details['cuisine'], details['cuisine_bill']))
        mycon.commit()

        gaming_query = """
            INSERT INTO gaming (C_ID, games, hours, bill)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(gaming_query, (customer_id, details['game'], 1, details['game_bill']))
        mycon.commit()

        # Insert total bill into 'total' table
        total_amount = details['room_rent'] + details['cuisine_bill'] + details['game_bill']
        total_query = """
            INSERT INTO total (C_ID, room_rent, restaurent_bill, gaming_bill, total_amount)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(total_query, (customer_id, details['room_rent'], details['cuisine_bill'], details['game_bill'], total_amount))
        mycon.commit()

        print("\nBooking successful!")
    else:
        print("Invalid package selection. Please try again.")


def get_total_bill():
    print("\n--- Get Total Bill ---")
    customer_id = int(input("Enter Customer ID: "))
    cursor = mycon.cursor()
   
    # Fix the query to select specific columns from the 'total' table
    query = """
        SELECT C_ID, room_rent, restaurent_bill, gaming_bill, total_amount
        FROM total
        WHERE C_ID = %s
    """
    cursor.execute(query, (customer_id,))
    record = cursor.fetchall()

    if record:
        headers = ["Customer ID", "Room Rent", "Restaurant Bill", "Gaming Bill", "Total Amount"]
        print(tabulate(record, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No bill found for the given Customer ID. Please ensure the booking has been completed.")
        print("Check if the total has been properly added to the 'total' table.")



def change_package():
    print("\n--- Change Package ---")
    cursor = mycon.cursor()

    # Display all clients with their current packages
    query = """
        SELECT customer_details.C_ID, customer_details.C_name, rooms.room_choice
        FROM customer_details
        INNER JOIN rooms ON customer_details.C_ID = rooms.C_ID
    """
    cursor.execute(query)
    records = cursor.fetchall()

    if records:
        headers = ["Customer ID", "Name", "Current Package"]
        print("\n--- Current Clients and Packages ---")
        print(tabulate(records, headers=headers, tablefmt="fancy_grid"))

        # Prompt user to select the customer and change the package
        customer_id = int(input("\nEnter the Customer ID to change the package: "))
        print("\n--- Available Packages ---")
        print("1. PACK1: King Room, Indian veg cuisine with dessert, Bowling")
        print("2. PACK2: Deluxe Room, Chinese veg with dessert, VR")
        print("3. PACK3: Premier Room, Chinese veg and non-veg with dessert, Table Tennis and VR")

        new_package = int(input("\nEnter the new package (1, 2, or 3): "))
        room_choices = {1: "King Room", 2: "Deluxe Room", 3: "Premier Room"}
        package_details = {
            1: {"room_rent": 10000, "cuisine": "Indian veg with dessert", "cuisine_bill": 6000, "game": "Bowling", "game_bill": 350, "total": 16350},
            2: {"room_rent": 15000, "cuisine": "Chinese veg with dessert", "cuisine_bill": 9000, "game": "VR", "game_bill": 500, "total": 24500},
            3: {"room_rent": 25000, "cuisine": "Chinese veg and non-veg with dessert", "cuisine_bill": 14000, "game": "Table Tennis and VR", "game_bill": 900, "total": 40000},
        }

        if new_package in package_details:
            details = package_details[new_package]

            # Update the package in the database
            cursor.execute("UPDATE rooms SET room_choice = %s, room_rent = %s WHERE C_ID = %s",
                           (room_choices[new_package], details["room_rent"], customer_id))
            cursor.execute("UPDATE restaurent SET cuisine = %s, bill = %s WHERE C_ID = %s",
                           (details["cuisine"], details["cuisine_bill"], customer_id))
            cursor.execute("DELETE FROM gaming WHERE C_ID = %s", (customer_id,))
            cursor.execute("INSERT INTO gaming (C_ID, games, hours, bill) VALUES (%s, %s, %s, %s)",
                           (customer_id, details["game"], 1, details["game_bill"]))
            cursor.execute("UPDATE total SET room_rent = %s, restaurent_bill = %s, gaming_bill = %s, total_amount = %s WHERE C_ID = %s",
                           (details["room_rent"], details["cuisine_bill"], details["game_bill"], details["total"], customer_id))
            mycon.commit()
            print(f"\nPackage for Customer ID {customer_id} updated successfully to {room_choices[new_package]}!")
        else:
            print("Invalid package selection. Please try again.")
    else:
        print("No clients found.")

from tabulate import tabulate

def search_customer_details():
    print("\n--- Search Customer Details ---")
    customer_id = int(input("Enter Customer ID: "))
    cursor = mycon.cursor()

    # Join customer_details with booking_records to fetch all required details
    query = """
        SELECT customer_details.C_ID, customer_details.C_name, customer_details.country,
               customer_details.C_email, customer_details.C_phone_no, customer_details.C_aadhar,
               booking_records.checkin_date, booking_records.checkout_date,
               booking_records.room_no, booking_records.no_of_days
        FROM customer_details
        INNER JOIN booking_records ON customer_details.C_ID = booking_records.C_ID
        WHERE customer_details.C_ID = %s
    """
    cursor.execute(query, (customer_id,))
    record = cursor.fetchall()

    if record:
        # Display customer details using tabulate
        customer_data = [
            ["Customer ID", record[0][0]],
            ["Name", record[0][1]],
            ["Country", record[0][2]],
            ["Email", record[0][3]],
            ["Phone Number", record[0][4]],
            ["Aadhar", record[0][5]],
        ]
        print("\n--- Customer Details ---")
        print(tabulate(customer_data, tablefmt="fancy_grid"))

        # Display booking details using tabulate
        booking_data = [
            ["Check-in Date", record[0][6]],
            ["Check-out Date", record[0][7]],
            ["Room No.", record[0][8]],
            ["Number of Days", record[0][9]],
        ]
        print("\n--- Booking Details ---")
        print(tabulate(booking_data, tablefmt="fancy_grid"))
    else:
        print("No details found for the given Customer ID.")




def cancel_booking():
    print("\n--- Cancel Booking ---")
    customer_id = int(input("Enter Customer ID: "))
    cursor = mycon.cursor()
    tables = ["booking_records", "customer_details", "rooms", "restaurent", "gaming", "total"]

    for table in tables:
        query = f"DELETE FROM {table} WHERE C_ID = %s"
        cursor.execute(query, (customer_id,))
        mycon.commit()

    print("Booking canceled successfully.")

def show_all_bookings():
    print("\n--- All Bookings ---")
    cursor = mycon.cursor()

    # Join booking_records with customer_details to fetch the necessary details (excluding Aadhar, Email, and Country)
    query = """
        SELECT customer_details.C_ID, customer_details.C_name,
               booking_records.checkin_date, booking_records.checkout_date,
               booking_records.room_no, booking_records.no_of_days
        FROM booking_records
        INNER JOIN customer_details ON booking_records.C_ID = customer_details.C_ID
    """
    cursor.execute(query)
    records = cursor.fetchall()

    if records:
        headers = ["Customer ID", "Name", "Check-in Date", "Check-out Date", "Room No.", "No. of Days"]
        print(tabulate(records, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No bookings found.")




# Main Program
while True:
    main_menu()
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_room()
        elif choice == 2:
            get_total_bill()
        elif choice == 3:
            change_package()
        elif choice == 4:
            search_customer_details()
        elif choice == 5:
            cancel_booking()
        elif choice == 6:
            show_all_bookings()
        elif choice == 7:
            print("Thank you for visiting Hotel Taj, Ooty!")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")

