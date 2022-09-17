import numpy as np 

capacity12 = np.ones((100,100)) * 100
capacity34 = np.array([[50,0] * 50 for i in range(100)]) + capacity12

def part13(rate,time,row,col,capacity):
    flux = capacity * 0
    flux[0,0] = rate * time
    if row == 0:
        return min(flux[row,col],capacity[row,col])
    for i in range(1,row+1):
        fluxi = list(max(flux[i-1,:-2] - capacity[i-1,:-2],0))
        flux[i] = (np.array(fluxi+[0]) +  np.array([0] + fluxi)) * 0.5
    return min(flux[row,col],capacity[row,col])

def part24(rate,cap,row,col,capacity):
    #sove(part13(rate,time,row,col,capacity)==cap)
    #return round(x)
    def f(t):
        return part13(rate,t,row,col,capacity)
    min = 0
    max = 999
    while (max-min) > 1:
        mid = round((min + max)/2 - 0.5) + 0.5
        if f(mid) == cap:
            return round(mid)
        elif f(mid) > cap:
            max = mid
        else :
            min = mid 
    return round(0.5 * (min + max))
    
def all(json_list):
    answer_list = []
    answer = {"part1": 20.00,"part2": 1,"part3": 60.00,"part4": 2}
    for i in json_list:
        capacity = capacity12
        rate = i['part1']['flow_rate']
        time = i['part1']['time']
        row = i['part1']['row_number']
        col = i['part1']['col_number']
        answer['part1'] = part13(rate,time,row,col,capacity)
        rate = i['part2']['flow_rate']
        cap = i['part2']['amount_of_soup']
        row = i['part2']['row_number']
        col = i['part2']['col_number']
        answer['part2'] = part24(rate,cap,row,col,capacity)
        capacity = capacity34
        rate = i['part3']['flow_rate']
        time = i['part3']['time']
        row = i['part3']['row_number']
        col = i['part3']['col_number']
        answer['part3'] = part13(rate,time,row,col,capacity)
        rate = i['part4']['flow_rate']
        cap = i['part4']['amount_of_soup']
        row = i['part4']['row_number']
        col = i['part4']['col_number']
        answer['part4'] = part24(rate,cap,row,col,capacity)
        answer_list += [answer.copy()]
    return answer_list

    



