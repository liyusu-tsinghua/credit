import numpy as np 

#20010101 is monday
weekday_of_20010101 = 0

def calender_get_index(number,weekday_init,if_366_year):
    month_length = [31,28 + int(if_366_year),31,30,31,30,31,31,30,31,30,31]
    weekdays = (weekday_init + number - 1)%7
    month_index = 0
    for i in range(12):
        month_index += month_length[i]
        if month_index >= number:
            months = i
            return months,weekdays

def calender_get_weekday_init(year):
    cycles = (year - 2001)//4
    res = (year - 2001)%4
    days = weekday_of_20010101 + cycles * (365*4 + 1) + res * 365
    return days%7

def calender_get_12_7_bool(input_list):
    year = input_list[0]
    weekday_init = calender_get_weekday_init(year)
    answer = np.zeros((12,7))
    if_366_year = (year%4 == 0)
    for i in input_list[1:]:
        if i>0:
            if i<=(365 + int(if_366_year)):
                index = calender_get_index(i,weekday_init,if_366_year)
                answer[index] = answer[index] or 1
    return answer

def output_i(np_array_7):
    if sum(np_array_7)==7:
        return 'alldays'
    elif sum(np_array_7[:5])==0:
        if sum(np_array_7) == 2:
            return 'weekend'
    elif sum(np_array_7[:5])==5:
        return 'weekday'
    weekdays = 'mtwtfss'
    answer = ''
    for i in range(7):
        answer += weekdays[i] * int(np_array_7[i]) + ' ' * int(1-np_array_7[i])
    return answer

def calender_output_part1(answer_bool_12_7_array):
    answer = ''
    for i in answer_bool_12_7_array:
        answer +=  output_i(i) + ','
    return answer

def calender_part1(input_list):
    return calender_output_part1(calender_get_12_7_bool(input_list))

def calender_part2(string):
    for i in range(96):
        if string[i] == ' ':
            year = 2001 + i
            break
    answer = [year]
    if_366_year = (year%4 == 0)
    month_length = [31,28 + int(if_366_year),31,30,31,30,31,31,30,31,30,31]
    weekday_init = calender_get_weekday_init(year)
    month_first_day = [1] * 12
    for i in range(1,12):
        month_first_day[i] = month_first_day[i-1] + month_length[i-1]
    month_monday = [i + 7 - (i + weekday_init - 1)%7 for i in month_first_day]
    for i in range(12):
        month_info = string[i*8:i*8+7]
        if month_info=='alldays':
            answer += [month_monday[i] + j for j in range(7)]
        elif month_info=='weekday':
            answer += [month_monday[i] + j for j in range(5)]
        elif month_info=='weekend':
            answer += [month_monday[i] + j for j in range(5,7)]
        else :
            for j in range(7):
                if month_info[j] != ' ':
                    answer += [month_monday[i] + j]
    return answer






   