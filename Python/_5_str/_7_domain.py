email_id = str(input("Enter the email ID : "))
start = email_id.index("@") + 1
end = email_id.find(".",-8)
domain = email_id[start:end]
print("Domain = ",domain)


# bharati.yadav@yahoo.com

email_id = str(input("Enter the email ID : "))
start = email_id.index("@") + 1
end = email_id.rfind(".")
domain = email_id[start:end]
print("Domain = ",domain)


