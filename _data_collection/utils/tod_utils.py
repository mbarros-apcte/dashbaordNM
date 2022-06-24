import datetime

import pandas as pd


def _decimalToBinary(n):
    n = int(n)
    return bin(n).replace("0b", "")


def _get_days_of_week():
    reg_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    sched_order = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
    return reg_order, sched_order


def _get_present_days(week_binary):
    days = _get_days_of_week()[1]

    present_days = []
    for ii in range(len(days)):
        if week_binary[ii] == "1":
            present_days.append(days[ii])
    return present_days


def get_days_of_week(n):
    # fulfill the string to have 8 characters
    week_binary = _decimalToBinary(n)
    for ii in range(8 - len(week_binary)):
        week_binary = "0" + week_binary

    present_days = _get_present_days(week_binary)
    return present_days


def _get_hour_minute(number):
    hour = int(number / 100)
    minute = int(number % 100)
    return datetime.time(hour, minute, 0)


def get_tod_for_each_day(df_tod_int):
    df_res = pd.DataFrame(data=[])
    all_days = _get_days_of_week()[0]
    for day in all_days:
        col_name = "dayX_present"
        df_tod_int[col_name] = df_tod_int["present_days"].apply(lambda x: True if day in x else False)

        df_day = df_tod_int[df_tod_int[col_name] == True].reset_index(drop="index")
        df_day = df_day.sort_values(by=['TIME'], ascending=True).reset_index(drop="index")

        df_day["DAY"]=day
        df_day["TIME_START"] = df_day['TIME'].apply(_get_hour_minute)
        end_time = list(df_day["TIME_START"])[1:]
        end_time.append(datetime.time(23, 59, 59))
        df_day["TIME_END"] = end_time

        df_day = df_day[["INTID", "DAY", "TIME_START", "TIME_END", "PLAN"]]

        if len(df_res) == 0:
            df_res = df_day
        else:
            df_res = pd.concat([df_res, df_day])

    return df_res
