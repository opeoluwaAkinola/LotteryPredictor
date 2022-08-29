from Predictor_Gui import *
import Fetch_results
import get_Date
import predictor

#Columns that i will use for my pandafram n that
columns=["Day","Date_day","Date_month","Date_year","n-1","n_2","n_3","n_4","n_5","n_star_1","n_start_2"]
target_categories1=list(range(1,51))
target_categories2=list(range(1,13))

#Was too lazy to type the years out on after the other so i did this below
years=[]
for n in range(2021,2023):
    years.append(n)
print(years)
for n in range(0,len(years)):
    years[n]=str(years[n])
#Got the urls
url="https://www.euro-millions.com/results-history-"

#Get the information from the website using this sexy method "get_info"
Dt=Fetch_results.fetchResults(years,url,columns)

Df_all=Dt.results().iloc[:,4:9]
print(Dt.results())

if Dt.results().iloc[-1]["Day"] == "Tuesday":
    lottery_date=get_Date.getDate("Friday").date()
elif Dt.results().iloc[-1]["Day"] == "Friday":
    lottery_date=get_Date.getDate("Tuesday").date()

normal_balls=predictor.predict(Df_all,59).return_prediction()
Df_all=Dt.results().iloc[:,9:11]
star_balls=predictor.predict(Df_all,11).return_prediction()

gui=Gui(normal_balls,star_balls,lottery_date)



