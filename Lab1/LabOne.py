# print("Hello itians")
# ---------------------------------------------------------lab1--------------------------------------------------------

# prop1...write a prog that counts up the number of vowels [a,e,i,o,u] contained in the string


def CountVowels(x):
    counter = 0
    vowels = "aeiouAEIOU"
    for i in x:
        if i in vowels:
            counter += 1
    print(f'Number of vowels = {counter}')





# ........................................................................................................................
# prop2...write a prog that prints the locations of "i" character in any string you


def Ilocation(x):

    for y in range(len(x)):
        if x[y] == "i" or x[y] == "I":
            print(y+1)



# ........................................................................................................................
# prop3...write a prog that generate a multiplication table from 1 to the number passed


def MultTable(x):
    for i in range(x):
        i += 1
        for j in range(i):
            j += 1
            print(f"{i}*{j}={i*j}")



# .............................................................................................................................
# prop4...write a prog to build a mario pyramid


def MarioPyramid():
    for i in range(1, 5):
        print(" "*(5-i), "*"*i)



