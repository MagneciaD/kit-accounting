from Apps.Model.Organization import Organization

def create_organization_from_input():
    company_name = input("Enter company name: ")
    company_address = input("Enter company address: ")
    email_address = input("Enter email address: ")
    phone_no = input("Enter phone number: ")
    website_link = input("Enter website link: ")

    organization = Organization(company_name, company_address, email_address, phone_no, website_link)
    organization.save()

create_organization_from_input()