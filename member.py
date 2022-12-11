class Member:
    def __init__(self):
        self.__user = {}
        self.__l_user = ""
        self.__l_pass = ""
        self.__new_name = str

    def password(self):
        with open("customer.txt", "r") as data:
            data_file = data.read().splitlines()
            while True:
                self.__new_name = input("Enter Name ").upper()
                if self.__new_name not in data_file:
                    ur = input("Create User ")
                    pa = input("Create Password ")
                    print("Create Success")
                    self.__user[ur] = pa
                    break
                else:
                    print("User name already exists.")
                    print("Pleas, try again. ")

        return self.__user

    def login(self):
        print(" ")
        print("---------LOGIN---------")
        self.__l_user = input("Username: ")
        self.__l_pass = input("Password: ")
        return self.__l_user, self.__l_pass

    @property
    def new_name(self):
        return self.__new_name



# member = Member()
# member.password()
# member.login()
# print(member.name)
# member.display()
