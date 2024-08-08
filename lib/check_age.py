from datetime import datetime
# def right_format(date_string,date_format):
#     try:
#         datetime.strptime(date_string, date_format)
#         return True
#     except ValueError:
#         return False 

# def check_age(date):
#     format = "%Y-%m-%d"

    
#     if not right_format(date,format):
#         raise ValueError("Sorry wrong format insert dat as YYYY-MM-DD")

#     user_age = datetime.strptime(date, format)
#     today = datetime.today()
#     diff = today - user_age

#     if int(diff.days) >= 5840:
#         return "Access granted"
#     else:
#         return f"Access denied yur age is {int(int(diff.days)/365)} required age is 16"
    

def check_age(date):
    format = "%Y-%m-%d"

    try:
        datetime.strptime(date, format)
    except ValueError:
        raise ValueError("Sorry wrong format insert dat as YYYY-MM-DD")

    user_age = datetime.strptime(date, format)
    today = datetime.today()
    diff = today - user_age

    if int(diff.days) >= (365 * 16):
        return "Access granted"
    else:
        return f"Access denied yur age is {int(int(diff.days)/365)} required age is 16"
    


