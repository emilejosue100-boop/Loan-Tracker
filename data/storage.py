import csv

# the funcion saves the client info in the csv file to be used in the future for the analysis and the machine learning model if necessary
def save_client_info(client_info):

    import os
    file_exists = os.path.exists("data/clients.csv")
    with open("data/clients.csv", "a", newline="") as file:
       writer = csv.DictWriter(file, fieldnames=["name", "age","business_field","business_name", "loan_amount", "month_active", "amount_paid", "repayment_period", "is_member"])
       if not file_exists:
           writer.writeheader()
       writer.writerow(client_info)

# this function load the clients from the csv file and return a list of our cliens, it reads the csv file and creates a list of dictionaries where each dictionary represents a client with their information. If the file does not exist, it returns an empty list and prints a message indicating that no existing client data was found.
def load_clients_from_csv():
    clients_list = []
    try:
        with open("data/clients.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                client_info = {
                    "name": row["name"],
                    "age": int(row["age"]),
                    "business_field": row["business_field"],
                    "business_name": row["business_name"],
                    "loan_amount": float(row["loan_amount"]),
                    "month_active": int(row["month_active"]),
                    "amount_paid": float(row["amount_paid"]),
                    "repayment_period": int(row["repayment_period"]),
                    "is_member": row["is_member"].lower() == "true"
                }
                clients_list.append(client_info)
    except FileNotFoundError:
        print("No existing client data found. Starting with an empty list.")
    return clients_list