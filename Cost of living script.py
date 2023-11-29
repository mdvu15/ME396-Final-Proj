# import numpy as np
def COL_calc():
    #Load data
    data = open('Cost of living data.csv','r')
    a = data.read() #read the data
    b = a.split('\n') #isolate numerical values
    city_list_nospaces = []
    dictionary = dict()
    for i in range(len(b)-1):
        first_comma = b[i].find(',')
        second_comma = b[i].find(',',first_comma+1)
        city_list_nospaces.append(b[i][0:second_comma].replace(' ','').upper())
        dictionary[b[i][0:second_comma].upper()] = float(b[i][second_comma+1:])
    # dictionary_keys = list(dictionary.keys())
    # dictionary_values = list(dictionary.values())
        
    # data2 = open('cbsa2fipsxw.csv','r')
    # a2 = data2.read() #read the data
    # b2 = a2.split('\n') #isolate numerical values
    # cbsa_dict = dict()
    # for i2 in range(len(b2)):
    #     b2[i2] = b2[i2].replace(' ','').replace('"','').upper()
    #     first_comma2 = b2[i2].find(',')
    #     second_comma2 = b2[i2].find(',',first_comma2+1)
    #     cbsa_dict[b2[i2][first_comma2+1:]] = b2[i2][0:first_comma2]
    # cbsa_keys = list(cbsa_dict.keys())
    # cbsa_values = list(cbsa_dict.values())
        
    current_location = input('Enter current location in format (city,state abbreviation): ').upper()
    user_salary = float(input('Enter yearly salary in current location ($): '))
    new_location = input('Enter new location in format (city,state abbreviation): ').upper()
    
    #Find values for each city
    index1 = float()
    while not bool(index1):
        try:
            index1 = dictionary[current_location]
        except KeyError:
            current_location = input('Enter valid current location in format (city,state abbreviation): ').upper()
            
    index2 = float()
    while not bool(index2):
        try:
            index2 = dictionary[new_location]
        except KeyError:
            new_location = input('Enter valid new location in format (city,state abbreviation): ').upper()
            
    difference = round(index2-index1,2)
    if difference > 0:
        print('Compared to',current_location+', the cost of living in',new_location,'is +'+str(difference)+'%')
    else:
        print('Compared to',current_location+', the cost of living in',new_location,'is',str(difference)+'%')
    print('To maintain your currently lifestyle, you must make at least $'+str(user_salary*((difference+100)/100)))

def find_CBSA():
    #Load data
    data = open('cost of living with cbsa with manual completed data2.csv','r')
    a = data.read() #read the data
    b = a.split('\n') #isolate numerical values
    city_list_nospaces = []
    dictionary = dict()
    for i in range(len(b)-1):
        first_comma = b[i].find(',')
        second_comma = b[i].find(',',first_comma+1)
        city_list_nospaces.append(b[i][0:second_comma].replace(' ','').upper())
        dictionary[b[i][0:second_comma].upper()] = int(b[i][second_comma+1:])
    
    state = input('Enter 2 letter state abbreviation: ').upper()
    city = input('Enter city name: ').upper()
    state_city = city + ','+ state
    while not bool(state_city in dictionary):
        state = input('Enter valid 2 letter state abbreviation: ').upper()
        city = input('Enter valid city name: ').upper()
        state_city = city + ','+ state
    CBSA = dictionary[state_city]
    print('The CBSA for',state_city,'is',CBSA)

#Call functions
COL_calc()
# find_CBSA()

#create cbsa file
# data_list = []
# for i3 in range(len(city_list_nospaces)):
#     if city_list_nospaces[i3] in cbsa_dict.keys():
#         data_list.append([dictionary_keys[i3],dictionary_values[i3],cbsa_values[cbsa_keys.index(city_list_nospaces[i3])]])
#     else: 
#         data_list.append([dictionary_keys[i3],dictionary_values[i3],0])

# np.savetxt("cost of living with cbsa.csv",
#         data_list,
#         delimiter =", ",
#         fmt ='% s')
    