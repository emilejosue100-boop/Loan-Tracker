# MicroFinance Manager

## Description
MicroFinance Manager is a desktop application built in Python for cooperative 
agents who manage youth microloans in Goma, Democratic Republic of Congo. 
It combines automatic financial calculations with AI-powered advice to simplify 
daily loan management tasks. The tool was built as a final project for 
Stanford Code in Place 2026.

## Problem it Solves
Most small cooperatives in eastern Congo manage their client data manually, 
using notebooks or basic spreadsheets. This creates three problems:

- Data is easily lost or miscalculated
- There is no early warning system for clients at risk of defaulting
- Loan eligibility decisions are inconsistent depending on who you ask

MicroFinance Manager solves all three by digitizing the process, automating 
calculations, and adding AI assistance to every decision.

## Features

### Tab 1 - Loan Tracker
- Register existing clients with full details: name, age, business, 
  loan amount, repayment period, and membership status
- Automatic interest rate calculation: 5% for cooperative members, 
  10% for non-members
- Automatic calculation of total amount to repay and monthly payment
- Risk status flagging based on repayment progress:
  - On Track: paid 90% or more of expected amount
  - At Risk: paid between 60% and 90% of expected amount
  - Critical: paid less than 60% of expected amount
- AI-generated advice per client using OpenAI API
- Save client records to CSV for persistent storage
- View all saved clients in a separate window

### Tab 2 - Eligibility Checker
- Evaluate new loan applicants before any loan is given
- Checks three eligibility conditions based on cooperative policies:
  - Applicant must be 18 years or older
  - Recommender must be a cooperative member
  - Applicant must have a business plan
- AI-generated explanation of the eligibility result
- Encourages eligible applicants and gives constructive guidance 
  to those who do not yet qualify

## How to Install and Run

### Requirements
- Python 3.x
- An OpenAI API key

### Installation
1. Clone this repository:
   git clone https://github.com/emilejosue100-boop/Loan-Tracker.git

2. Navigate to the project folder:
   cd loan-tracker

3. Install required libraries:
   pip install openai python-dotenv

4. Create a .env file in the root folder and add your OpenAI API key:
   OPENAI_API_KEY=your-key-here

5. Run the application:
   python main.py

## Project Structure
loan-tracker/
│
├── main.py
├── gui.py
├── calculator.py
├── ai_advisor.py
├── clients.py
└── data/
├── storage.py
└── clients.csv
## Technologies Used
- Python 3 — core programming language
- Tkinter — graphical user interface with two tabs, forms, and popups
- CSV — persistent client data storage
- OpenAI API (gpt-5.4-mini) — AI advice and eligibility explanations
- python-dotenv — secure API key management

## Cooperative Policies
The eligibility rules implemented in this tool are based on the official 
policies of a youth cooperative in Goma, DRC. Full policy details are 
available in this repository.

## About the Developer
This project was built by Ngolo Maliyabwana Josue, a young leader and 
microfinance practitioner based in Goma, Democratic Republic of Congo, 
working at the intersection of technology, financial inclusion, and 
youth leadership.

Although this tool was originally designed for a youth cooperative in 
Goma, it is built to be useful for any microfinance cooperative or 
savings group around the world. If you work in financial inclusion and 
find this tool helpful, you are welcome to use it, adapt it, and 
build on it.

Connect on LinkedIn: https://www.linkedin.com/in/josuengolo

## Version 2.0 — Coming Soon
This first version establishes the core features of MicroFinance Manager. 
The following improvements are planned for Version 2.0:

### Planned Features
- Savings Group Manager: track informal savings groups (tontines and VSLAs), 
  weekly contributions, and loan rotation among members
- Youth Loan Eligibility Score: a weighted scoring system that gives each 
  applicant a numeric score with a detailed breakdown
- Automatic Date Tracking: calculate months active automatically from the 
  loan start date instead of manual entry
- Client Search and Filter: search clients by name, risk status, or 
  business field
- Export Report: generate a printable PDF summary of all clients and 
  their repayment status
- Multi-language Support: French and Swahili interface for agents in 
  eastern Congo
- Dashboard: a visual summary showing total loans, total amount recovered, 
  and number of clients per risk category

## License
MIT License — free to use, modify, and distribute with attribution.