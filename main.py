import tkinter as tk
from gui import launch_app

root = tk.Tk()
root.title("Microfinance Manager")
root.geometry("400x300")
# This is the welcome screen that appears when the app is launched. It has a title, a subtitle, a description of the app, and a "Get Started" button that takes the user to the main application interface when clicked.
def get_started():
    root.destroy()
    launch_app()

label = tk.Label(root, text="Welcome to the Microfinance Manager", font=("Arial", 14))
label.pack(pady=20)

subtitle_label = tk.Label(root, text="Built for cooperative microfinance", font=("Arial", 12))
subtitle_label.pack(pady=5)

description = tk.Label(root, text='''Welcome to MicroFinance Manager, a desktop tool designed specifically for cooperative agents who manage youth microloans. This tool was built to simplify your daily work, reduce errors, and bring AI assistance directly into your decision making.
What this tool does:
With the Loan Tracker, you can register any current client by entering their basic information: name, age, business, loan amount, and repayment progress. The tool automatically calculates how much the client should have paid by now, flags their risk level, and uses AI to give you a short practical recommendation on how to handle that client going forward.
With the Eligibility Checker, you can evaluate any young person who wants to apply for a loan. Based on your cooperative's official policies, the tool checks if the applicant meets all required conditions and generates a clear AI explanation of the result, encouraging those who qualify and guiding those who do not yet meet the requirements.
Our cooperative policies:
Full eligibility criteria and cooperative rules are available on GitHub at:
github.com/your-username/loan-tracker''',wraplength=600, font=("Arial", 10))
description.pack(padx=50, pady=10)

button = tk.Button(root, text="Get Started", command=get_started)
button.pack()

root.mainloop()