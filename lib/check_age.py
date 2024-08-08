from datetime import datetime

def check_age(date):
    format = "%Y-%m-%d"
    
    if False == bool(datetime.strptime(date, format)):
        raise Exception("Sorry wrong format insert dat as YYYY-MM-DD")

    user_age = datetime.strptime(date, format)
    today = datetime.today()
    diff = today - user_age

    if int(diff.days) >= 5840:
        return "Access granted"
    else:
        return f"Access denied yur age is {int(int(diff.days)/365)} required age is 16"
    