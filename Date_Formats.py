
#------------- Code 1------------

# # "2026-07-16"
# from datetime import datetime
# date_str_1 = "2026-07-16"
# print(date_str)
# date_object = datetime.strptime(date_str, "%Y-%m-%d")
# print(date_object.date())


# date_str_2= "Jul 16, 2026"
# date_object_2 = datetime.strptime(date_str_2, "%b %d, %Y")
# print(date_object_2.date())


# ----------Code 2-----------------

# from datetime import datetime
# date_1 = datetime.strptime("2025, 7, 17", "%Y, %m, %d")
# date_2 = datetime.strptime("2026, 9, 18", "%Y, %m, %d")

# delta = date_2-date_1
# print(delta.days)

# ----------Code 3-------------------

# from datetime import datetime, timedelta
# date_O = datetime(2026, 7, 17)
# date_new = date_O + timedelta(days=7)
# print(date_new.date())

# -----------Code 4 ------------------

# from datetime import datetime
# print(datetime.now().date())

# ----------Code 5 -------------------

# from datetime import datetime, timedelta
# file_date = datetime.strptime("2026, 7, 15", "%Y, %m, %d").date()
# file_age  =datetime.now().date()- file_date
# if file_age.days > 1:
#     print("Stale data")
# else: 
#     print("New data")

# -----------------Code 6 -------------

# from datetime import datetime, timedelta

# ticket_date = datetime(2026, 7, 1).date()
# Current_date = datetime.now().date()
# print(Current_date)
# if ticket_date >= Current_date - timedelta(days=30):
#     print("SLA not breaced")
# else:
#     print("SLA breached")


# ----------------Code 7-------------------
# from datetime import datetime
# date_text_1 = "2026-07-17"
# date_object_1 = datetime.strptime(date_text_1, "%Y-%m-%d").date()
# print(date_object_1)

# date_text_2 = "17-Jul-2026"
# date_object_2 = datetime.strptime(date_text_2, "%d-%b-%Y").date()
# print(date_object_2)

#----------------------- Code 8 Refresher---------------------
# datestr = "17/07/2026"

# from datetime import datetime
# dt = datetime.strptime(datestr, "%d/%m/%Y")
# print (f"The date converted is {dt.date()}")


