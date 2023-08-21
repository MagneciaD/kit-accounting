from Apps.Model.Organization import Organization
from Apps.Model.User import User
import random
import string

def generate_org_id():
    numbers = ''.join(random.choices(string.digits, k=5))
    letters = ''.join(random.choices(string.ascii_letters, k=2))
    org_id = 'ORG' + numbers
    return org_id


def create_organization_from_input(user_id):
    try:
        print("User ID inside create_organization_from_input:", user_id)
        company_name = input("Enter company name: ")
        company_address = input("Enter company address: ")
        email_address = input("Enter email address: ")
        company_logo = input("Enter company logo URL: ")
        phone_no = input("Enter phone number: ")
        website_link = input("Enter website link (optional): ")
        org_id = generate_org_id()

        organization = Organization(org_id, user_id, company_name, company_address, email_address, company_logo, phone_no, website_link)
        organization.save()

        print("Organization created and saved successfully!")

    except Exception as e:
        print("An error occurred:", e)


