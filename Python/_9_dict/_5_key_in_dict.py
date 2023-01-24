# size=int(input("entee the size: "))
# dct={}
# for i in range(size):
#     key=input("enter the key : ")
#     value=input("enter the value : ")
#     dct[key]=value
# print(dct)

# key1=input("enter the key you want to check : ")
# if key1 in dct.keys():
#     print("the key is present ")
# else:
#     print("key is not present")




# dict = {'Aman': 110, 'Rajesh': 440, 'Suraj': 990}
# key = 'Bharati'
 
# if dict[key]:
#     print('The key exists in the dictionary')
# else :
#     print("The key doesn't exist in the dictionary")




n = int(input("enter a the size of dictionary:"))
d = {}

for i in range(n):
    print("enter the key:")
    keys = input() 
    print("enter the value:")
    values = input() 
    d[keys] = values
print(d)

print("to check the key present in the dict enter a key:")
key = input()

if d.get(key):
    print("yes key exist in the dictionary in")
else:
    print("no key is not present in")    

print(d)