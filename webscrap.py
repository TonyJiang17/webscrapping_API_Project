#hw1pr3.py
#Name: Tiancheng(Tony) Jiang

#Question: I want to test whether ranker.com's The Best Moves of 2017 is accurate according to Rotten Tomato's score 
# Here is my approach to the winner and the score:
#
# 1. first I will create a function that takes in a movie name that grabs the movie's Rotten Tomato's site
# 2. then, use bs4 to parse the rotten tomato page and return the score of that movie out of 100
# 3. The same function would do the same thing for the second movie 
# 4. write another function that takes in the names of the two movies in the ranker.com page and grabs the page
# 5. then use bs4 to parse the IMDB 2017 movies ranking page and check the two movies' respective ranking is correct according to their rotten tomato scores
 

import requests
from bs4 import BeautifulSoup



def edit_movie_name(movie):
    """this function alters the movie name so that it can be used in the url line in later function
    """
    if (isinstance(movie, str)):
        if (movie != ""):
            movie = movie.lower()
            edit_name = ""
            for i in movie:
                if (i == " "):
                    edit_name = edit_name + "_"
                else:
                    edit_name = edit_name + i
            return edit_name
        else:
            print("movie name can't be empty'")
    else:
        print("movie name has to be a string")


def get_rotten_tomato_page(movie_name):
    """ This function requests the rotten tomato page of the input movie name
        and parses it with Beautiful Soup, returning the resulting
        Beautiful Soup object, soup
    """
    rotten_tomato_url = "https://www.rottentomatoes.com/m/" + edit_movie_name(movie_name) + "/"
    response = requests.get(rotten_tomato_url)   # request the page

    if response.status_code == 404:                 # page not found
        print("There was a problem with getting the page:")
        print(color_popularity_url)

    rotten_tomato_url = response.text                   # the HTML text from the page
    soup = BeautifulSoup(rotten_tomato_url,"lxml")      # parsed with Beautiful Soup
    return soup



def find_RTmovie_score( soup ):
    """ find_RTmovie_score takes in a soup, a Beautiful Soup object returned from a successful run of
        get_rotten_tomato_page
        
        find_RTmovie_score returns the movie's TOMATOMETER score found in the page 
        
    """
   
    div_score = soup.find('div', {'class': "critic-score meter"})      
    span_score = div_score.find('span', {'class': "meter-value superPageFontColor"})
        
    actual_score = 0                    # the deafult (integer) ranking: 0
    try:
        actual_score = int(span_score.span.text)  # try to convert it to an integer
    except:                                   # if it fails
        pass                                  # do nothing and leave it at 0
        
    return actual_score
        



def get_2017movies_ranking_page():
    """ get_2017movies_ranking_page requests the ranker.com page of 2017 movies ranking
        and parses it with Beautiful Soup, returning the resulting
        Beautiful Soup object, soup
    """
    imdb_rank_2017movies_url = "http://www.imdb.com/list/ls064079588/"
    response = requests.get(imdb_rank_2017movies_url)         # request the page
    
    if response.status_code == 404:                 # page not found
        print("There was a problem with getting the page")
        print(team_color_url)
        
    imdb_ranker_2017movies_url = response.text                   # the HTML text from the page
    soup = BeautifulSoup(imdb_ranker_2017movies_url,"lxml")      # parsed with Beautiful Soup
    return soup



def is_ranking_correct(movie1, movie2, soup):
    """ is_ranking_correct takes in a beautiful soup object, soup
        and uses Beautiful Soup to find if the two movies are ranked correctly according to rotten tomatoes
    
    """
    #finding ranking for movie1 and movie2:
    All_divs = soup.findAll('div', {'class':"lister-item-content"})# find all divs of the right class
    movie1_ranking = 0 
    movie2_ranking = 0
    for each_div in All_divs:
        title = each_div.find('a')
        try:
            ranking = int(each_div.h3.span.text[:-1])  # try to convert it to an integer
        except:                                   # if it fails
            pass
        
        if (movie1 == title.text):
            movie1_ranking = ranking

    for each_div in All_divs:
        title = each_div.find('a')
        try:
            ranking = int(each_div.h3.span.text[:-1])  # try to convert it to an integer
        except:                                   # if it fails
            pass
        
        if (movie2 == title.text):
            movie2_ranking = ranking

    #find rotten tomatoes score for both movies: 
    movie1_RT_soup = get_rotten_tomato_page(movie1)
    movie1_RTscore = find_RTmovie_score(movie1_RT_soup)
    print(movie1, "'s Rotten Tomato score is: ", movie1_RTscore, " and its IMDB ranking is: ", movie1_ranking)

    movie2_RT_soup = get_rotten_tomato_page(movie2)
    movie2_RTscore = find_RTmovie_score(movie2_RT_soup)
    print(movie2, "'s Rotten Tomato score is: ", movie2_RTscore, " and its IMDB ranking is: ", movie2_ranking)

    if ((movie1_ranking < movie2_ranking) and (movie1_RTscore >= movie2_RTscore)):
        print("IMBD ranking is also correct according to Rotten Tomatoes score")
        return True 
    elif ((movie1_ranking > movie2_ranking) and (movie1_RTscore <= movie2_RTscore)):
        print("IMBD ranking is also correct according to Rotten Tomatoes score")
        return True
    else:
        print("IMBD ranking is not correct according to Rotten Tomatoes score")
        return False




def main():
    """
    # Here is an example of using the Web's Wisdom to answer the question
    #
    #     Who will win the superbowl next weekend... ?
    #
    #     Not limited to last weekend's teams!
    """
    #testing all functions in the file
    #testing getting the right rotten tomato score for the right movie
    print("1. testing to get the right rotten tomato score for the movie\n")
    soup1 = get_rotten_tomato_page("Titanic")
    Titanic_RT_score = find_RTmovie_score( soup1 )
    print("According Rotten Tomato, Titanic' score is 88' and our function give us the result: ", Titanic_RT_score)
    print("\n")

    soup2 = get_rotten_tomato_page("Avatar")
    Avatar_RT_score = find_RTmovie_score( soup2 )
    print("According Rotten Tomato, Avatar' score is 83' and our function give us the result: ", Avatar_RT_score)
    print("\n")

    #testing IMDB ranking of any of 2 movies in the ranking page is right according their rotten tomato scores
    print("2. testing wheter IMDB ranking of any of 2 movies in the ranking page is right according their rotten tomato score\n")

    soup3 = get_2017movies_ranking_page()
    result0 = is_ranking_correct("Okja", "Call Me by Your Name", soup3)
    print(result0, "-- ranking between 'Okaja' and 'Call Me by Your Name' is False according to Rotten Tomato Scores")
    print("\n")
    result1 = is_ranking_correct("Murder on the Orient Express", "Lady Bird", soup3)
    print(result1, "-- ranking between 'Okaja' and 'Call Me by Your Name' is True according to Rotten Tomato Scores")



    return

if __name__ == "__main__":
    main()  # hike!

