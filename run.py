# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT =gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Trimester_Counter')

def get_trimester_data():
    """
    Get trimester data. 
    """
    print("Please enter months pregnant.")
    print("Data should be add as you progress through your weeks of pregnancy.")
    print("Example: 1 month, 2 months, 3 months")

    data_str = input("Enter your pregnancy month here:")
    print(f"The data provided is (data_str)")