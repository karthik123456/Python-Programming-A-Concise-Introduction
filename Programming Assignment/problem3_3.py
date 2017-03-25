def problem3_3(month, day, year):
    """ Takes date of form mm/dd/yyyy and writes it in form June 17, 2016 
        Example6: problem3_5(6, 17, 2016) gives June 17, 2016 """
    months = ("January","February","March","April","May","June","July" \
    "August","September","October","November","December")
    monthStr = int(month)-1
    print(months[monthStr],str(day) + ",",year)