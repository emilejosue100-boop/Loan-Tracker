import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
# I am creating an instance of the OpenAI client using the API key stored in the environment variable "OPENAI_API_KEY". This client will be used to make requests to the OpenAI API for generating advice and explanations based on the client's information and eligibility criteria.
openAI_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# This function takes a client's information and their risk status as input, and makes a request to the OpenAI API to generate a short, practical recommendation on how to handle that client going forward. The response from the API is then returned as a string.
def get_loan_advice_for_client(client,risk_status):
    response = openAI_client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[{"role": "user", "content": f'''You are a microfinance advisor for a youth cooperative in Goma, Congo. 
    A client named {client["name"]}, age {client["age"]}, runs a {client["business_field"]} business called {client["business_name"]}. 
    He took a {client["loan_amount"]}$ loan over {client["repayment_period"]} months and has paid {client["amount_paid"]}$ so far after {client["month_active"]} months active.
    His current risk status is {risk_status}.
    Give a short, practical recommendation in 4 sentences maximum.'''}])
    return response.choices[0].message.content

# This function takes an applicant's information and their eligibility status as input, and makes a request to the OpenAI API to generate a clear explanation of the result. If the applicant is eligible, the explanation will encourage them warmly. If the applicant is not eligible, the explanation will provide constructive guidance on how they can improve their chances of being accepted in the future. The response from the API is then returned as a string.
def get_eligibility_explanation(applicant,is_eligible):
    response = openAI_client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[{"role": "user", "content": f'''You are a microfinance advisor for a youth cooperative in Goma, Congo. 
    A applicant named {applicant["name"]}, age {applicant["age"]}, runs a {applicant["business_field"]} business called {applicant["business_name"]}. 
    He is recommended by {applicant["recommender"]} and has a {applicant["has_business_plan"]} business plan. He is asking a loan of {applicant["loan_amount"]}
    for a repayment period of {applicant["repayment_period"]}. Note that according to our comapny policies, if the applicant does not have a 
    business plan or a recommenderr who exist as a memeber in the cooperaive, he should not be accepted. The applicant is {"ELIGIBLE " if is_eligible else "NOT ELIGIBLE" }
    If eligible, encourage them warmly. If not, explain clearly and give constructive guidance.'''}])
    return response.choices[0].message.content