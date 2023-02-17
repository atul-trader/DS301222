from bs4 import BeautifulSoup

file = open("C:\\Users\\vashi\\OneDrive\\Documents\\DS301222\\Python\\_23_xml_file_handling\\demo.xml")
soup = BeautifulSoup(file,'html.parser')
# print(soup)

# find_all converts the data into list
data = soup.find_all("student")
# print(data)

# find is used to fetch data on the bases of tag passed
# name = soup.find("student_name")
# print(name)
# print(name.text)


for i in data:
    print(i.find("student_name").text)


name = soup.find("student_name",{"name":"third"})
print("Name : ",name.text)