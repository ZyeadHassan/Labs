
# # .............................................................................................................
def validate(email):
    try:
        if '@' in email and '.' in email:
            username, domain = email.split('@')
            if username and domain:
                x, y = domain.split('.')
                if x and y:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    except:
        return False



# # ....................................................................................................
#
email = ["ali@gmail.com", "sara@yahoo.com",
         "mohamed@outlook.com", "noha@iti.gov.eg"]


domain = map(lambda i: i.split("@")[1], email)
print(list(domain))
# # ........................................................................................................
users = [{"name": "zyead", "pas": "123"}, {"name": "ahmed", "pas":  "456"}]


def check(x):
    for i in users:
        if x == i["name"]:
            password = input("enter ur pass: ")
            if password == i["pas"]:
                print("valid")
                break
            else:
                print("wrong pass")
                break
        else:
            continue
    else:
        print("notFound")


