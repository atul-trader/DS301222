import json

def register(filename,name,mobile_no,email_ID,password):

    details = {
        "Name":name,
        "Mobile No.":mobile_no,
        "Email ID":email_ID,
        "Password":password
    }
    file = open(filename,"r+")
   
    try:
        data = json.load(file)
        if data:
            if details not in data:
                data.append(details)
                file.seek(0)
                file.truncate()
                json.dump(data,file)
                file.close()
                return True
        else:
            return False

    except json.decoder.JSONDecodeError:
        lst = []
        lst.append(details)
        json.dump(lst,file)
        file.close()
        return True
    
    except Exception as ex:
        print("Exception in register function : ",ex)
        return False
    
    finally:
        file.close()

    return False


def login(filename,username,password):
    pass