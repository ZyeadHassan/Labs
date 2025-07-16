# # Lab2
# # prob1: Fill an array of 5 elements from the user ,sort it in desc and asc orders then display the output
num = []

def listing():

    for i in range(5):
        x = input("insert number: ")
        num.append(x)
    print(sorted(num))
    print(sorted(num, reverse=True))



# # ....................................................................................................................
# # prob2: write a prog that generate a multiplication table from 1 to the number passed


def MultiplcationTable(x):
    Multiplication_table = []
    for i in range(x):
        total = []
        i += 1
        for j in range(i):
            j += 1
            z = i*j
            total.append(z)
        Multiplication_table.append(total)
    print(Multiplication_table)



# # ............................................................................................................................
# # # prob3
def MarioList():
    l = [' ', ' ', ' ', ' ', ' ']
    for i in range(5):
        l.insert(len(l), "*")
        l.remove(" ")
        print(l)



# # ................................................................................................................................
# # #prob4: Ask the user for his name then confirm that he has enterd his name (not an empty string/integers).then proceed to ask him for his
# # email and print all this data

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
