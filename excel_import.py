import pandas as pd
# Import Excel file to List


# Please change your file path
excel_path = r"C:\Users\eyyub.eren\Desktop\Selenium-python\user_data.xlsx"

excel_file = pd.read_excel(excel_path, sheet_name = "user_login")
df = pd.DataFrame(excel_file, columns = ["username","password"])

usernames = list(df.username)
passwords = list(df.password)

userlist = {
    "username" : [],
    "password" : []
}

for value in range(len(usernames)):
    userlist["username"].append(usernames[value])
    userlist["password"].append(passwords[value])

