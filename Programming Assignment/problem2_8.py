def problem2_8(temp_list):
    sum = 0
    for i in range(0,len(temp_list)) :
        sum = sum + temp_list[i]
    average = sum/len(temp_list)
    print("Average:",average)
    print("High:",max(temp_list))
    print("Low:",min(temp_list))