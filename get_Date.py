from datetime import *

class getDate:
    def __init__(self,name_of_day:str):
        # first get todays date
        self.day=name_of_day

    def date(self):
        name_of_day=self.day
        today = datetime.today()

        # format it to only get the string of the day
        today_string = datetime.today().strftime('%A')

        # iterate through a week (7 days) day by day
        for i in range(1, 8):
            # each iteration we are increasing our "day-step"
            day = timedelta(days=1)
            the_day = datetime.today() + (day * i)

            # each iterated new day is formatted to only get the string of the day
            the_day_str = the_day.strftime('%A')

            # if the string matches our search-day, we save the number of pasted days in i
            if name_of_day == the_day_str:
                day_difference = i
            else:
                continue
        # now we calculate the future date by adding "day_difference" on top of today
        day_date = today + timedelta(days=day_difference)
        day_date = day_date.strftime('%d-%m-%Y')
        return day_date