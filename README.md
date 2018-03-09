# Webscrapping and API Project 
Overview: 
This project focuses on accesssing online information through webscrapping html contents 
and APIs. There are five mini projects within the repository. Three of the projects involves
using APIs such as the Google Map API. I retrieveed data from API into json files and further
processed the data using python in order to pinpoint the key information I want. 

The other two mini projects involved webscrapping raw html contents of a website using 
beautiful soup. Similar to the API projects, I would want to further process the raw data 
to find the key information I want to return. 

Specific Files:
1. google_map_API.py: 
This is the python file where I used the open source google map API and build a python function
takes in city locations in the US and outputs the distances between each city in a table display
in the terminal.
(sub-files: distances.json *this file would be regenerated each time google_map_API is ran)

2. itunesAPI.py:
In this python file, I used the Apple Itunes API that includes all of its artists record and alum informations. 
This python file first generates singer list json which is used to pinpoint a specific artist's ID and then is ued 
to retrieve another json file that includes all album information of that speciifc singer. I then wrote functions that 
calculate interesting facts about a specific artist or compare certain information between 2 artists.
(sub-files: appledata.json, appledata_full.json, artist.json, artists1.json,artist2.json)

3. usgs_earth_equake_API.py:
This is again an API application where I retrieved information from the usgs earthquake API and used a function to 
parse that information. The function return a display of the number of earthquakes that had happened in any specific week
(input any date) and the date that has the most earthquakes. 
(subfiles: earthquakes.json)

4: webscrap.py:
This python file uses beautiful soup to scrap the web. I parsed the html files from two movie ranking sites, and 
compared the results to see whether the two website information are in agreement or not. 

5. silly_SuperBowl_Prediction: 
This is also a webscrapping mini project using beautiful soup. The SuperBowl was right around the corner when I was working 
on this project, so I decided to create a very silly game predictor solely based off of how likeable the team's logo colors are. 
Thus, I parsed a website that includes the SuperBowl teams' logos and another site where ranks people's favortie colors. I then 
wrote a simple function that compares the team logo's color ranking based on the that and used that score to predict which team 
is mostly to win. (Ya iknow silly)

Final Thoughts:
Very fun and useful tool and can be applied to almost any task or project. 
