import requests
import string
import json
import datetime



def convert_milisecond_todate(ms):
    """takes ms as an integer type and output the date that it represent in 'year-month-dates' format
    """
    s = ms / 1000.0
    return datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d')


def usgs_api(start, end):
    """this function takes in a start and end date in string formate "YEAR-MONTH-DATES" 
    and converts the earthquakes data provided from usgs into a json file named "earthquakes.json"
    """
    
    url="https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"


    inputs={"starttime":start,"endtime":end}

    result = requests.get(url,params=inputs)
    data = result.json()

    
    filename_to_save = "earthquakes.json"
    f = open( filename_to_save, "w" )     
    string_data = json.dumps( data, indent=2 )  
    f.write(string_data)                        
    f.close()                                   
    print("\nFile", filename_to_save, "written.")
    return



from collections import defaultdict      

def usgs_process(threshold):
    """ this function takes a parameter threshold, which is an integer for the threshold of earthquake mag
    and returns the number of earthquakes per date for the past 7 days and the date with most number of quakes
    """
    #load "earthquakes.json"
    filename_to_read = "earthquakes.json"
    f = open( filename_to_read, "r" )
    string_data = f.read()
    JD = json.loads( string_data )  

    #creates a default dictionary that uses date as key and the number of earthquakes of that date as value
    dates = defaultdict(int)

    #inputs all earthquakes with magnitude over the threshold into the dictionary
    earth_quake_data = JD['features']
    for i in range(len(earth_quake_data)):
        each_earthquake = earth_quake_data[i]
        each_mag = each_earthquake["properties"]["mag"]
        if (each_mag >= threshold):
            date_eq = convert_milisecond_todate(each_earthquake["properties"]["time"])
            dates[date_eq] += 1

    #find the date that have most number of earthquakes
    date_with_mostquakes = ""
    counter = 0
    for d in dates.keys():
        if (dates[d] > counter):
            counter = dates[d]
            date_with_mostquakes = d
    

    for d in dates.keys():
        quake_number = dates[d]
        print("On", d, ", there are this many earthquakes: ",quake_number)
    
    print("the date with most number of earthquakes is: ", date_with_mostquakes, " and it has ", counter, " earthquakes")

    return date_with_mostquakes
    


def main():
    """checks for all functions above  
    """
    print("The function prints out the number of earthquakes for each of the previous 7 days -- in addition, it should determine which day (of the previous 7) had the most earthquakes\n")
    #creates 'earthquakes.json''
    usgs_api('2018-01-29', '2018-02-04')
    #runs usgs_process(threshold)
    usgs_process(2.42)

   



if __name__ == "__main__":
    main()

