import tkinter as tk
from tkinter import ttk
from calculator import calculate_interest, calculate_expected_amount, get_risk_status
from ai_advisor import get_loan_advice_for_client, get_eligibility_explanation
from tkinter import messagebox
from data.storage import save_client_info, load_clients_from_csv

# This function launches the main application interface after the welcome screen. It creates a window with two tabs: "Loan Tracker" and "Eligibility Checker". The "Loan Tracker" tab allows users to input client information, calculate loan details, get advice, and save the information. The "Eligibility Checker" tab allows users to input applicant information and check their eligibility for a loan based on predefined criteria. Both tabs include error handling for invalid inputs.
def launch_app():
    root = tk.Tk()

    root.title("Microfinance Manager")
    root.geometry("600x700")

    # This funcion is for the first tab, it takes the input from the user about the client, calculates the loan details, gets the risk status, and then uses AI to provide advice on how to handle that client. It also saves the client's information in a csv file for future reference.
    def calculate_and_advise():
        try:
            name = name_entry.get()
            age = int(age_entry.get())
            business_field = business_field_entry.get()
            business_name = business_name_entry.get()
            loan_amount = float(loan_entry.get())
            month_active = int(month_active_entry.get())
            amount_paid = float(amount_paid_entry.get())
            repayment_period = int(repayment_period_combo.get())
            is_member = is_member_combo.get() == "True"

            total_amount,monthly_payment = calculate_interest(loan_amount,is_member, repayment_period)
            expected_amount_paid_by_now = calculate_expected_amount(monthly_payment, month_active)
            risk_status = get_risk_status( amount_paid, expected_amount_paid_by_now)

            client_info={
                "name": name,
                "age": age,
                "business_field": business_field,
                "business_name": business_name,
                "loan_amount": loan_amount,
                "month_active": month_active,
                "amount_paid": amount_paid,
                "repayment_period": repayment_period,
                "is_member": is_member
            }
            advice = get_loan_advice_for_client(client_info, risk_status)

            result_text = f"total amount to repay: {total_amount:.2f}\nExpected Amount: {expected_amount_paid_by_now:.2f}\nRisk Status: {risk_status}\nAdvice: {advice}"
            messagebox.showinfo("Loan Analysis Result", result_text)
            save_client_info(client_info)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for age, loan amount, months active, and amount paid.")

    # this funcion displays all the clients in a new window when we click the "View all Clients" button in the first tab, it loads the clients from the csv file and shows their information in a readable format. If there are no clients, it shows a message indicating that no clients were found.
    def view_clients():
        clients_list = load_clients_from_csv()
        if not clients_list:
            messagebox.showinfo("Clients", "No clients found.")
            return

        window = tk.Toplevel(root)
        window.title("All Clients")
        window.geometry("500x400")
        # it iterates through the list of clients and creates a label for each client with their information formatted in a readable way, and packs it into the window. This allows the user to see all the clients they have entered into the system.
        for client in clients_list:
            tk.Label(window, text=f"Name: {client['name']}, Age: {client['age']}, Business: {client['business_name']} ({client['business_field']}), Loan: {client['loan_amount']}, Months Active: {client['month_active']}, Amount Paid: {client['amount_paid']}, Repayment Period: {client['repayment_period']} months, Is Member: {client['is_member']}").pack()

    # the function is for the second tab to help check the eligibilty of the applicant, it takes the input from the user about the applicant, checks if they meet the eligibility criteria, and then uses AI to provide an explanation of the result. It also includes error handling for invalid inputs.
    def check_eligibility():
        try:
            name = applicant_name_entry.get()
            age = int(applicant_age_entry.get())
            business_field = applicant_business_field_entry.get()
            business_name = applicant_business_name_entry.get()
            recommender = recommender_entry.get()
            has_business_plan = has_a_business_plan_combo.get() == "True"
            is_recommender_a_member = is_recommender_a_member_combo.get() == "True"
            loan_amount = float(applicant_loan_amount_entry.get())
            repayment_period = int(applicant_repayment_period_combo.get())

            applicant_info={
                "name": name,
                "age": age,
                "business_field": business_field,
                "business_name": business_name,
                "recommender": recommender,
                "has_business_plan": has_business_plan,
                "is_recommender_a_member": is_recommender_a_member,
                "loan_amount": loan_amount,
                "repayment_period": repayment_period
            }
            #based on the cooperative's eligibility criteria, the function checks if the applicant is eligible for a loan. The criteria include being at least 18 years old, having a business plan, and having a recommender who is a member of the cooperative. The result of the eligibility check is then passed to the AI function to generate an explanation for the user.
            is_eligible = age>=18 and has_business_plan and is_recommender_a_member
            explanation = get_eligibility_explanation(applicant_info, is_eligible)

            messagebox.showinfo("Eligibility Result", explanation)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for age, loan amount, and repayment period.")


    notebook = ttk.Notebook(root)
    # I am creating two tabs in the main application interface, one for the loan tracker and another for the eligibility checker. Each tab will contain the relevant input fields and buttons for their respective functionalities.
    tab1 = tk.Frame(notebook)
    tab2 = tk.Frame(notebook)

    notebook.add(tab1, text="Loan Tracker")
    notebook.add(tab2, text="Eligibility Checker")

    notebook.pack(fill="both", expand=True)

    # In the first tab, I am creating input fields for the client's name, age, business field, business name, loan amount, months active, amount paid, repayment period, and membership status. I also include a button to calculate the loan details, get advice, and save the client's information, as well as a button to view all clients.
    name_label = tk.Label(tab1, text="Client Name")
    name_label.pack()

    name_entry = tk.Entry(tab1)
    name_entry.pack()

    age_label = tk.Label(tab1, text="Client Age")
    age_label.pack()

    age_entry = tk.Entry(tab1)
    age_entry.pack()

    business_field_label = tk.Label(tab1, text="Business Field")
    business_field_label.pack()

    business_field_entry = tk.Entry(tab1)
    business_field_entry.pack()

    business_name_label = tk.Label(tab1, text="Business Name")
    business_name_label.pack()

    business_name_entry = tk.Entry(tab1)
    business_name_entry.pack()

    loan_label = tk.Label(tab1, text="Loan Amount")
    loan_label.pack()

    loan_entry = tk.Entry(tab1)
    loan_entry.pack()

    month_active_label = tk.Label(tab1, text="Months Active")
    month_active_label.pack()

    month_active_entry = tk.Entry(tab1)
    month_active_entry.pack()

    amount_paid_label = tk.Label(tab1, text="Amount Paid")
    amount_paid_label.pack()

    amount_paid_entry = tk.Entry(tab1)
    amount_paid_entry.pack()

    repayment_period_label = tk.Label(tab1, text="Repayment Period(6/12)")
    repayment_period_label.pack()

    repayment_period_combo = ttk.Combobox(tab1, values=["6", "12"], state="readonly")
    repayment_period_combo.pack()

    is_member_label = tk.Label(tab1, text="Is Member?(True/False)")
    is_member_label.pack()

    is_member_combo = ttk.Combobox(tab1, values=["True", "False"], state="readonly")
    is_member_combo.pack()


    calculate_button = tk.Button(tab1, text="Calculate, Get Advice and Save Info", command=calculate_and_advise)
    calculate_button.pack()

    view_clients_button = tk.Button(tab1, text="View all Clients", command=view_clients)
    view_clients_button.pack()


    # I am working on the 2nd tab and include all the necessary fields for the eligibilty check of he applicant such as name, age, business field, business name, recommender, whether they have a business plan, whether the recommender is a member, loan amount requested, and repayment period. I also include a button to check the eligibility of the applicant and get an explanation of the result.
    applicant_name_label = tk.Label(tab2, text="Applicant Name")
    applicant_name_label.pack()

    applicant_name_entry = tk.Entry(tab2)
    applicant_name_entry.pack()

    applicant_age_label = tk.Label(tab2, text="Applicant Age")
    applicant_age_label.pack()

    applicant_age_entry = tk.Entry(tab2)
    applicant_age_entry.pack()

    applicant_business_field_label = tk.Label(tab2, text=" Business Field")
    applicant_business_field_label.pack()

    applicant_business_field_entry = tk.Entry(tab2)
    applicant_business_field_entry.pack()

    applicant_business_name_label = tk.Label(tab2, text=" Business Name")
    applicant_business_name_label.pack()

    applicant_business_name_entry = tk.Entry(tab2)
    applicant_business_name_entry.pack()

    recommender_label = tk.Label(tab2, text="Recommender Name")
    recommender_label.pack()

    recommender_entry = tk.Entry(tab2)
    recommender_entry.pack()

    has_a_business_plan_label = tk.Label(tab2, text="Has a Business Plan?(True/False)")
    has_a_business_plan_label.pack()

    has_a_business_plan_combo = ttk.Combobox(tab2, values=["True", "False"], state="readonly")
    has_a_business_plan_combo.pack()

    is_recommender_a_member_label = tk.Label(tab2, text="Is Recommender a Member?(True/False)")
    is_recommender_a_member_label.pack()

    is_recommender_a_member_combo = ttk.Combobox(tab2, values=["True", "False"], state="readonly")
    is_recommender_a_member_combo.pack()

    applicant_loan_amount_label = tk.Label(tab2, text=" Loan Amount requested")
    applicant_loan_amount_label.pack()  

    applicant_loan_amount_entry = tk.Entry(tab2)
    applicant_loan_amount_entry.pack()

    applicant_repayment_period_label = tk.Label(tab2, text=" Repayment Period(6/12)")
    applicant_repayment_period_label.pack()

    applicant_repayment_period_combo = ttk.Combobox(tab2, values=["6", "12"], state="readonly")
    applicant_repayment_period_combo.pack()

    check_eligibility_button = tk.Button(tab2, text="Check Eligibility", command=check_eligibility)
    check_eligibility_button.pack()
    # Finally, I call the mainloop function to start the application's event loop, allowing the user to interact with the interface and use the functionalities provided in both tabs.
    root.mainloop()