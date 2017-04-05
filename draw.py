import datetime
import matplotlib.pyplot as plt

def get_air(city,year):
    data = {}
    with open(city+'-'+str(year)+'.csv','r') as csv_file:
        lines = csv_file.readlines()
        lines.pop(0)
    for line in lines:
        line = line.rstrip()
        line = line.split(',')
        day = line[1]
        first_day = datetime.datetime.strptime(str(year)+'-01-01',"%Y-%m-%d")
        last_day = datetime.datetime.strptime(str(year)+'-12-31',"%Y-%m-%d")
        now_day = datetime.datetime.strptime(day,"%Y-%m-%d")
        if now_day < first_day or now_day > last_day:
            continue
        day_data = [line[2],line[3],line[4]]
        data[day] = day_data
    # data = sorted(data.items(), key=lambda e:e[0], reverse=False)
    return data

def get_AQI(data_dict):
    for key in data_dict.keys():
        data_dict[key] = data_dict[key][0]
    return data_dict

def get_AQI_list(AQI_dict):
    sort_AQI = sorted(AQI_dict.items(), key=lambda e:e[0], reverse=False)
    AQI_list =[]
    date = []
    for i in sort_AQI:
        AQI_list.append(int(i[1])) 
        date.append(i[0])
    return AQI_list

def get_date_list(dict):
    sort_AQI = sorted(AQI_dict.items(), key=lambda e:e[0], reverse=False)
    date = []
    for i in sort_AQI:
        date.append(i[0])
    return date

def main():
    #-------------------------------------
    city1 = '临汾市'
    year1 = 2015
    data_dict1 = get_air(city1,year1)
    AQI_dict1 = get_AQI(data_dict1) 
    AQI_list1 = get_AQI_list(AQI_dict1)
    #-------------------------------------
    city2 = '临汾市'
    year2 = 2016
    data_dict2 = get_air(city2,year2)
    AQI_dict2 = get_AQI(data_dict2) 
    AQI_list2 = get_AQI_list(AQI_dict2)
    # print(AQI_list)
    city3 = '临汾市'
    year3 = 2014
    data_dict3 = get_air(city3,year3)
    AQI_dict3 = get_AQI(data_dict3) 
    AQI_list3 = get_AQI_list(AQI_dict3)
    # print(AQI_list)
    plt.subplot(311)
    plt.plot(AQI_list3)
    plt.ylabel('2014')

    plt.subplot(312)
    plt.plot(AQI_list1)
    plt.ylabel('2015')
    # plt.axis(date)
    plt.subplot(313)
    plt.plot(AQI_list2)
    plt.ylabel("2016")
    plt.show()

if __name__ == '__main__':
    main()