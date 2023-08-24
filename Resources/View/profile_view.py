from Apps.Model.User import User
from Apps.Model.Organization import Organization


def display_user_profile(user):
    if user:
        print("User Profile:")
        print(f"Email: {user.email}")
    else:
        print("User not found.")

def display_organization_profile(organization):
    if organization:
        print("Organization Profile:")
        print(f"Company Name: {organization.company_name}")
        print(f"Email Address: {organization.company_address}")
    else:
        print("Organization not found.")
