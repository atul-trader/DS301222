import pdb

def addition(no1,no2):
    add = no1 + no2
    return add

# pdb.set_trace()
if __name__ == "__main__":
    no1 = input("Enter no1 : ")
    no2 = input("Enter no2 : ")
    res = addition(no1,no2)
    print(f"Addition : {res}")

# Command to run the file in debug mode 
# python -m pdb .\Python\_17_pdb\_1_pdb_demo.py
