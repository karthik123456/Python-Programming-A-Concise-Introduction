def problem3_4(mon, day, year):
    """ Takes date such as July 17, 2016 and write it as 7/17/2016 """
    months = {"January":1, "February":2, "March":3, "April":4, "May":5, \
              "June":6, "July":7, "August":8, "September":9, "October":10, \
              "November":11, "December":12}
    print(str(months[mon]), str(day), year, sep='/')