def check_email(email):
    if "@" in email and "." in email.split("@")[-1]:
        name, domain = email.split("@", 1)
        if name and domain and "." in domain:
            return True
    return False

emails = ["user@mail.com", "noatsign.com", "wrong@domain", "test@site.org"]

for e in emails:
    print(f"{e} → {'Valid' if check_email(e) else 'Invalid'}")

