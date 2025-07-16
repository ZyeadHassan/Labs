
def validate():
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        email = input("Enter your email: ")

        try:
            if '@' in email and '.' in email:
                username, domain = email.split('@')
                if username and domain and '.' in domain:
                    x, y = domain.split('.')
                    if x and y:
                        print("Email is valid.")
                        return email
        except:
            pass

        attempts += 1
        print(f"Invalid email. Attempt {attempts} of {max_attempts}.")

    raise "Blocked"
