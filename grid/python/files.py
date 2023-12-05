#practicing files csv file type
with ("My-files.txt") as file_cvs:
    name= input("What is your first name? >: ")
    last_name= input("What is your last name? >: ")
    Phone_number= int(input("What is your phone number? >: "))

    file_cvs.write(name)
    file_cvs.write("\t")
    file_cvs.write(last_name)
    file_cvs.write("\t")
    file_cvs.write(Phone_number)
    print(file_cvs)