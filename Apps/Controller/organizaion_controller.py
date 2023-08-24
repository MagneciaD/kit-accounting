from Apps.Model.Organization import Organization
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


def read_all_organizations():
    organizations = Organization.read_all()

    if organizations:
        for org in organizations:
            print(f"Organization ID: {org.id}")
            print(f"Company Name: {org.company_name}")
            print(f"Email Address: {org.email_address}")
            print()  # Add a blank line between organizations
    else:
        print("No organizations found.")


def read_organization_by_id():
    org_id = input("Enter the organization ID you want to read: ")

    org = Organization.read(org_id)

    if org:
        print(f"Organization ID: {org.id}")
        print(f"Company Name: {org.company_name}")
        print(f"Email Address: {org.email_address}")
    else:
        print("Organization not found.")


def update_organization_from_input(org_id):
    company_name = input("Enter the new company name: ")
    company_address = input("Enter the new company address: ")
    email_address = input("Enter the new email address: ")
    company_logo = input("Enter the new company logo URL: ")
    phone_no = input("Enter the new phone number: ")
    website_link = input("Enter the new website link (optional): ")

    org = Organization(org_id, None, company_name, company_address, email_address, company_logo, phone_no, website_link)
    org.update()


def delete_organization_by_id(org_id):
    org = Organization()  # Create an empty Organization object
    org.id = org_id
    org.delete()
    print(f"Organization with ID {org_id} has been deleted.")
