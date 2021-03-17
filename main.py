import sys
from pymongo import MongoClient
from bson.son import SON
import query1 as q1
import query2 as q2
# import query3 as q3
import query4 as q4
import query5 as q5
import query6 as q6
import query7 as q7
import query8 as q8
import query9 as q9



client = MongoClient("mongodb://127.0.0.1:27017/")
database = client["Project"]
collection = database["players"]


def menu(ch):
        if ch==1:
            q1.query1()
        elif ch==2:
            q2.query2()
        elif ch==3:
            q4.query4()
        elif ch==4:
            q5.query5()
        elif ch==5:
            q6.query6()
        elif ch==6:
            q7.query7()
        elif ch==7:
            q8.query8()
        elif ch==8:
            q9.query9()
        elif ch==0:
            sys.exit()
        elif ch==99:
            print("--------------------------------------------------------------\n"
                  "1.  Find best players in their country. \n"
                  "2.  Find the weak skills of any player.\n"
                  "3.  List the top 10 goalkeepers.\n"
                  "4.  Players that your club needs to lay off.\n"
                  "5.  List the players that need to resign.\n"
                  "6.  Find the team that performs best in the specified skill. \n"
                  "7.  Best options for buying players. \n"
                  "8.  Check if any player has improved since the last year.\n"
                  "99. Show menu\n"
                  "--------------------------------------------------------------\n")

        else:
            print("Invalid input")



print("\nWelcome to world soccer player information wizard!\n")
print("--------------------------------------------------------------\n"
                  "1.  Find best players in their country. \n"
                  "2.  Find the weak skills of any player.\n"
                  "3.  List the top 10 goalkeepers.\n"
                  "4.  Players that yor club needs to lay off.\n"
                  "5.  List the players that need to resign.\n"
                  "6.  Find the team that performs best in the specified skill. \n"
                  "7.  Best options for buying players. \n"
                  "8.  Check if any player has improved since the last year.\n"
                  "99. Show menu\n"
                  "--------------------------------------------------------------\n")

s=1
while 1:
    s = int(input("\nChoose Operation: "))
    menu(s)




