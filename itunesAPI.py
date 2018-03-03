#
# starting examples for cs35, week2 "Web as Input"
# name: Tiancheng(Tony) Jiang 

import requests
import string
import json


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# Problem 2 starter code
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#
#
#

def apple_api(artist_name):
    """ takes a string (name) returns the appleId
    """
    ### Use the search url to get an artist's itunes ID
    search_url = "https://itunes.apple.com/search"
    parameters = {"term":artist_name,"entity":"musicArtist","media":"music","limit":200}
    result = requests.get(search_url, params=parameters)
    data = result.json()

    # save to a local file so we can examine it
    filename_to_save = "appledata.json"
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    print("\nfile", filename_to_save, "written.")

    # Here, you should return the artist id:
    #
    # Note: it's helpful to find the iTunes artistId and return it here
    # (this hasn't been done yet... try it!) 
    filename_to_read="appledata.json"
    f = open( filename_to_read, "r" )
    string_data = f.read()
    data = json.loads( string_data )
    #print("the raw json data is\n\n", data, "\n")

    return data["results"][0]["artistId"]   # This is probably _not_ the correct answer...


#
# 
#
def apple_api_lookup(artistId):
    """ 
    Takes an artistId and grabs a full set of that artist's albums.
    "The Beatles"  has an id of 136975
    "Kendrick Lamar"  has an id of 368183298
    "Taylor Swift"  has an id of 159260351

    Then saves the results to the file "appledata_full.json"

    This function is complete, though you'll likely have to modify it
    to write more_productive( , ) ...
    """
    lookup_url = "https://itunes.apple.com/lookup"    
    parameters = {"entity":"album","id":artistId}    
    result = requests.get(lookup_url, params=parameters)
    data = result.json()

    # save to a file to examine it...
    filename_to_save="appledata_full.json"
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    print("\nfile", filename_to_save, "written.")

    # we'll leave the processing to another function...
    return



def apple_api_lookup_process():
    """  reads the file created above + parses it...
    """
    filename_to_read="appledata_full.json"
    f = open( filename_to_read, "r" )
    string_data = f.read()
    data = json.loads( string_data )
   # print("the raw json data is\n\n", data, "\n")

    # for live investigation, here's the full data structure
    return data

def more_productive(artist1, artist2):
    """ This function takes the 2 artists' names, as strings.  converts those names to AppleIDs
    and then makes another API call in order to gather all of the album/work information from iTunes.
    It should save those results into the filenames fname1 and fname2
    """
    ### Use the search url to get an artist's itunes ID
    search_url = "https://itunes.apple.com/search"
    parameters_a1 = {"term":artist1,"entity":"musicArtist","media":"music","limit":200}
    parameters_a2 = {"term":artist2,"entity":"musicArtist","media":"music","limit":200}
    result_a1 = requests.get(search_url, params=parameters_a1)
    result_a2 = requests.get(search_url, params=parameters_a2)
    data_a1 = result_a1.json()
    data_a2 = result_a2.json()

    # save to a local file so we can examine it
    filename_a1_to_save = "artist1.json"
    f = open( filename_a1_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data_a1, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
   # print("\nfile", filename_a1_to_save, "written.")

    filename_a2_to_save = "artist2.json"
    f = open( filename_a2_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data_a2, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    #print("\nfile", filename_a2_to_save, "written.")

    filename_to_read="artist1.json"
    f1 = open( filename_to_read, "r" )
    string_data = f1.read()
    data1 = json.loads( string_data )
    a_1id = data1["results"][0]["artistId"]

    filename_to_read="artist2.json"
    f2 = open( filename_to_read, "r" )
    string_data = f2.read()
    data2 = json.loads( string_data )
    a_2id = data2["results"][0]["artistId"]
    
    lookup_url = "https://itunes.apple.com/lookup"    
    parameters1 = {"entity":"album","id":a_1id}    
    result1 = requests.get(lookup_url, params=parameters1)
    data1 = result1.json()
    parameters2 = {"entity":"album","id":a_2id}    
    result2 = requests.get(lookup_url, params=parameters2)
    data2 = result2.json()

    # save to a file to examine it...
    filename_to_save1="artist1.json"
    f = open( filename_to_save1, "w" )     # opens the file for writing
    string_data = json.dumps( data1, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    print("\nfile", filename_to_save1, "written.")

    filename_to_save2="artist2.json"
    f = open( filename_to_save2, "w" )     # opens the file for writing
    string_data = json.dumps( data2, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    print("\nfile", filename_to_save2, "written.")


    return 

#
#
#
def most_productive_process():
    """ read in both artists json files, prints each artist's total number of albums, and returns 
    the name of the artistwho has most albums
    """
    filename_to_read="artist1.json"
    f_1 = open( filename_to_read, "r" )
    string_data = f_1.read()
    data_1 = json.loads( string_data )
    name1 = data_1["results"][0]["artistName"]
    print("# of results for ",name1,"==",data_1["resultCount"])

    filename_to_read="artist2.json"
    f_2 = open( filename_to_read, "r" )
    string_data = f_2.read()
    data_2 = json.loads( string_data )
    name2 = data_2["results"][0]["artistName"]
    print("# of results for ",name2,"==", data_2["resultCount"], "\n")

    if (data_1["resultCount"] >= data_2["resultCount"]):
        return name1
    else:
        return name2 

def most_pricy_album(artist1):
    """ This function takes a artist's name, as strings.  converts those names to AppleIDs
    and then makes another API call in order to gather all of the album/work information from iTunes.
    It should save those results into the filenames "artist"
    """
    ### Use the search url to get an artist's itunes ID
    search_url = "https://itunes.apple.com/search"
    parameters_a1 = {"term":artist1,"entity":"musicArtist","media":"music","limit":200}
    result_a1 = requests.get(search_url, params=parameters_a1)
    data_a1 = result_a1.json()

    # save to a local file so we can examine it
    filename_a1_to_save = "artist.json"
    f = open( filename_a1_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data_a1, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file


    filename_to_read="artist.json"
    f1 = open( filename_to_read, "r" )
    string_data = f1.read()
    data1 = json.loads( string_data )
    #find artist ID 
    a_1id = data1["results"][0]["artistId"]

    #grab artist's json files that include all of the artist's albums' informations
    lookup_url = "https://itunes.apple.com/lookup"    
    parameters1 = {"entity":"album","id":a_1id}    
    result1 = requests.get(lookup_url, params=parameters1)
    data1 = result1.json()
    

    # save to a file to the same "artist" file
    filename_to_save1="artist.json"
    f = open( filename_to_save1, "w" )     
    string_data = json.dumps( data1, indent=2 )  
    f.write(string_data)                        
    f.close()                                   
    print("\nfile", filename_to_save1, "written.")
 

    return 

#
#
#
def most_pricy_album_process():
    """ example opening and accessing a large appledata_full.json file...
        You'll likely want to do more!
    """
    filename_to_read="artist.json"
    f_1 = open( filename_to_read, "r" )
    string_data = f_1.read()
    data_1 = json.loads( string_data )
    name1 = data_1["results"][0]["artistName"]

    #finding what is the most expensive album price for this artist 
    most_expensive = 0
    for i in range(1,len(data_1["results"])):
        if (data_1["results"][i]["collectionPrice"] > most_expensive):
            most_expensive = data_1["results"][i]["collectionPrice"]

    print(name1, "'s most expensive album costs $", most_expensive,"\n")

    return 




#
# main()  for testing problem 2's functions...
#
def main():
    """ a top-level function for testing things... """
    # routine for getting the artistId
    # testing apple_api(aritst)
    if 1:
        print("1. testing for apple_api(aritst)")
        artistId = apple_api("The Beatles") # should return 136975
        #artistId = apple_api("Kendrick Lamar") # should return 368183298
        #artistId = apple_api("Taylor Swift") # should return 159260351
        print("artistId is for The Beatles", artistId)

    # testing apple_api_lookup(artistID) and apple_api_lookup_process()
    if 1:
        print("\n")
        print("2. testing for apple_api_lookup(artistID) and apple_api_lookup_process()")
        apple_api_lookup(368183298)
        #freates appledata_full json for an artist
        data = apple_api_lookup_process()
        #print(data)
    
    # testing more_productive(artist1, artist2)and most_productive_process()
    if 1: 
        print("\n")
        print("3. comparing which of the following two artists are more productive:")
        print("a. comparing Steve Perry and Katy Perry")
        more_productive("Steve Perry", "Katy Perry")
        print("the more productive artist out of the 2 is: ", most_productive_process())

        print("b. comparing The Beatles and Katy Perrry")
        more_productive("The Beatles", "Kendrick Lamar")
        print("the more productive artist out of the 2 is: ", most_productive_process())

        print("c. comparing Taylor Swift and Justin Timberlake")
        more_productive("Taylor Swift", "Justin Timberlake")
        print("the more productive artist out of the 2 is: ", most_productive_process())

    
    # tesing  most_pricy_album(artist1) and most_pricy_album_process()
    if 1: 
        print("\n")
        print("4. the Following tests my own question: what is the price of the most expensive album of one artist?")
        print("a. Katy Perry's most expensive's album price is: ")
        most_pricy_album("Katy Perry")
        most_pricy_album_process()
        print("b. Taylor Swift's most expensive's album price is: ")
        most_pricy_album("Taylor Swift")
        most_pricy_album_process()
        print("c. The Beatles's most expensive's album price is: ")
        most_pricy_album("The Beatles")
        most_pricy_album_process()


#
# passing the mic (of control) over to Python here...
#
if __name__ == "__main__":
    main()

