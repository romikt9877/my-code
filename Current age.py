import datetime

def calcAge(year, month, day):
    if year < 1000:
        return "WRONG"
    if month > 12 or month < 1:
        return "WRONG"
    if day > 31 or day < 1:
        return "WRONG"
    current_date = datetime.date.today()
    user_date = datetime.date(year, month, day)
    return int((current_date - user_date).days / 365)

entry = list(map(int, input().split('/')))


print (calcAge(entry[0], entry[1], entry[2]))
