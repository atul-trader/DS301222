import re
from operations import *

if __name__ == "__main__":
    while True:
        try:
            choice = int(input("Enter \n1.Register \n2.Login : \n3.Exit :\n"))
        except ValueError:
            print("Please enter valid choice!")
            continue

        if choice == 1:
            try:
                register_choice = int(input("Enter \n1.Register as Admin \n2.Register as Student \n3.Exit : \n"))
            except ValueError:
                print("Please enter valid choice!")
                continue

            if register_choice == 1:
                name = input("Enter your name : ")
                mobile_no = input("Enter your mobile no. : ")
                email_ID = input("Enter your email ID : ")
                password = input("Enter your password : ")

                name_re = re.findall("^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$",name)
                mobile_no_re = re.findall("^[1-9]{1}[0-9]{9}$",mobile_no)
                email_ID_re = re.findall("^[a-zA-Z0-9._]+[@]{1}[a-z]+[.]{1}[a-z]+$",email_ID)
                password_re = re.findall("^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&*?])[A-Za-z\d!@#$%&*?]{8,16}$",password)

                if name_re and mobile_no_re and email_ID_re and password_re:
                    register_flag = register("admin.json",name,mobile_no,email_ID,password)
                    print("Successfully Registered!!!") if register_flag else print("Registeration Failed!")
                
                else:
                    if not name_re:
                        print("Entered name format is incorrect!")
                        continue
                    if not mobile_no_re:
                        print("Entered mobile no format is incorrect!")
                        continue
                    if not email_ID_re:
                        print("Entered email ID format is incorrect!")
                        continue
                    if not password_re:
                        print("Entered password format is incorrect")
                        continue

            elif register_choice == 2:
                name = input("Enter your name : ")
                mobile_no = input("Enter your mobile no. : ")
                email_ID = input("Enter your email ID : ")
                password = input("Enter your password : ")

                name_re = re.findall("^[A-Za-z]{2,15}\s[A-Za-z]{2,15}$",name)
                mobile_no_re = re.findall("^[1-9]{1}[0-9]{9}$",mobile_no)
                email_ID_re = re.findall("^[a-zA-Z0-9._]+[@]{1}[a-z]+[.]{1}[a-z]+$",email_ID)
                password_re = re.findall("^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&*?])[A-Za-z\d!@#$%&*?]{8,16}$",password)

                if name_re and mobile_no_re and email_ID_re and password_re:
                    register_flag = register("student.json",name,mobile_no,email_ID,password)
                    print("Successfully Registered!!!") if register_flag else print("Registeration Failed!")
                
                else:
                    if not name_re:
                        print("Entered name format is incorrect!")
                        continue
                    if not mobile_no_re:
                        print("Entered mobile no format is incorrect!")
                        continue
                    if not email_ID_re:
                        print("Entered email ID format is incorrect!")
                        continue
                    if not password_re:
                        print("Entered password format is incorrect")
                        continue

            else:
                print("Thank You for connecting with Edyoda! See you next time ...")
                exit()

        elif choice == 2:
            try:
                login_choice = int(input("Enter \n1.Login as Admin \n2.Login as Student \n3.Exit : \n"))
            except ValueError:
                print("Please enter valid choice!")
                continue  

            if login_choice == 1:
                pass
            elif login_choice == 2:
                pass
            else: 
                print("Thank You for connecting with Edyoda! See you next time ...")
                exit()