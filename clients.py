# this file does not acively conribue to the app because it is replaced by gui.py and storage.py but it served me for understanding the logic of the app and how to structure the data about clients, I am keeping it here for reference and for the future in case I want to add a feature that allows me to manage clients directly from the command line interface instead of the graphical user interface.
# I am writing the information about my clients
client_1={"name":"Ngolo Maliyabwana Josue",
          "age":19,
          "sex":"Male",
          "is_member":True,
          "business_field":"Technology",
          "business_name":"Your_Solution",
          "recommender":"Elon Musk",
          "loan_amount":300,
          "repayment_period":12,
          "month_active":2,
          "amount_paid":0}

client_2={"name":"Furaha Sifa Axella",
          "age":20,
          "sex":"Female",
          "is_member":True,
          "business_field":"Agriculture",
          "business_name":"Bon-Repas",
          "recommender":"Elon Musk",
          "loan_amount":450,
          "repayment_period":6,
          "month_active":3,
          "amount_paid":100}

# clients_list stores the information about our clients
clients_list=[client_1,client_2]

# this function helps to add new clients to our listt
def add_new_clients_to_list(clients_list):

    # I should work first about the name of the new client
    client_number_index=len(clients_list)+1
    new_client_name=f"client_{client_number_index}"
    print(f"--- Adding of {new_client_name} ---")

    # then we input the information about the client
    name=input("Name: ")
    age=int(input("Age: "))
    sex=input("Sex (Male/Female): ")
    is_member=input("Is a Member (True/False): ").lower()=="true"
    business_field=input("Business field: ")
    business_name=input("Business name: ")
    recommender=input("Recommender: ")
    loan_amount=float(input("Loan_amount: "))
    repayment_period=int(input("Repayment period: "))
    month_active=int(input("month_active: "))
    amount_paid=0
    client_dict={"name":name,
                 "age":age,
                 "sex":sex,
                 "is_member":is_member,
                 "business_field":business_field,
                 "business_name":business_name,
                 "recommender":recommender,
                 "loan_amount":loan_amount,
                 "repayment_period":repayment_period,
                 "month_active":month_active,
                 "amount_paid":amount_paid,
                 } 
    # this helps just to dynamically assign the name of clients  not something that impact the logic of the code
    globals()[new_client_name]=client_dict
    # we add the client now to our list with all the information we got
    clients_list.append(globals()[new_client_name])
    # this serves for purpose of signaling
    print(f"\n The {new_client_name} has been added successfully to our clients list !")
