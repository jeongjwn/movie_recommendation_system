

import sys
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import json
import csv

def get_score_actor():
    print('Which TV show would you want to search?')
    print('1. Squid Game   2. Derek   3. Self Made   4. Friends   5. You \n')
    quest= int(input('\n Enter a number between 1 to 5: \n'))
    if quest == 1: 
        print('You chose the tv show, Squid Game \n')
        content = requests.get('https://www.rottentomatoes.com/tv/squid_game')
        soup = BeautifulSoup(content.content, 'html.parser')
    elif quest == 2:
        print('You chose the tv show, Derek \n')
        content = requests.get('https://www.rottentomatoes.com/tv/derek')
        soup = BeautifulSoup(content.content, 'html.parser')
    elif quest == 3:
        print('You chose the tv show, Self Made \n')
        content = requests.get('https://www.rottentomatoes.com/tv/self_made_inspired_by_the_life_of_madam_cj_walker')
        soup = BeautifulSoup(content.content, 'html.parser')
    elif quest == 4:
        print('You chose the tv show, Friends \n')
        content = requests.get('https://www.rottentomatoes.com/tv/friends')
        soup = BeautifulSoup(content.content, 'html.parser')
    elif quest == 5:
        print('You chose the tv show, You \n')
        content = requests.get('https://www.rottentomatoes.com/tv/you')
        soup = BeautifulSoup(content.content, 'html.parser')
    else:
        print ('\n Number input out of range. Please enter a number between 1 to 5 \n')
        print('Restart...\n')
        return get_score_actor()

    percentage = soup.find_all("span",{"class":"mop-ratings-wrap__percentage"} and {"data-qa":"tomatometer"})
    percentage=percentage[0]
    percentage = percentage.get_text().strip()

    cast = soup.find_all("div",{"class":"media-body"})
    cast = cast[0].get_text()
    cast_lst = cast.split('\n')
    
    global actor
    actor=cast_lst[1].strip()
    


    main = soup.find(string=actor)
    main = main.find_parent("a")
    
    global link
    link = main.get('href').strip()
    link = str(link)
    
    tup = (actor, percentage)
    return tup


def get_three_movies(link):
    url = 'https://www.rottentomatoes.com{}'.format(link)
    content = requests.get(url)
    soup = BeautifulSoup(content.content, 'html.parser')

    mov_lst = {}
    global first
    firs = soup.find("div",{"slot":"caption"} and {"data-track":"scores"})
    firs = firs.get_text()
    first = firs.strip()
    mov_lst['first'] = first

    global second
    secon = soup.find("a",{"slot":"caption"} and {"data-track":"scores"})
    secon = secon.get_text()
    second = secon.strip()
    mov_lst['second']=second

    global third
    thir = soup.find_all("div",{"slot":"caption"} and {"data-track":"scores"})
    thir = thir[1]
    thir = thir.find('span')
    third = thir.get_text()
    mov_lst['third'] = third
    mov_lst = str(mov_lst)
    tup_2 = mov_lst
    return tup_2



def get_imdb_scores():

    movie_list = [first, second, third]
    name = actor
    # movie_list = ['deliver us from evil','assassination','the housemaid']
    # name = 'lee jung jae'

    def movie_request(name, movie_list): #movie_list is list of strings for movie names

        json_list = []
        name = name.replace(' ', '+')

        for movie in movie_list:
            film = movie.replace(' ', '+')
            url = "https://google-search3.p.rapidapi.com/api/v1/search/q={}+{}+imbd+movie&num=1".format(name,film)
            headers = {
            'x-user-agent': "desktop",
            'x-proxy-location': "US",
            'x-rapidapi-host': "google-search3.p.rapidapi.com",
            'x-rapidapi-key': "894908139emsh92b456a701aa261p16d15fjsn0af998a67950"
            }
            response = requests.request("GET", url, headers=headers)
            resp_json = response.json()
            json_list.append(resp_json)

        return json_list

    json_list = movie_request(name, movie_list)

    lst = []
    imdb_score = {}
    for result in json_list: 
        for json in result['results']:
            string = json['g_review_stars']
            start = string.find('Rating: ')
            end = string.find('/10')
            string = string[start:end]
            string = string.lstrip('Rating: ')
            try:
                string = float(string)
                lst.append(string)
            except:
                print('API network error. Re-running the function')
                get_imdb_scores()
    
    try: 
        imdb_score[first] = lst[0]
    except: 
        print ('API network error 1. Re-running the function')
        get_imdb_scores()
    try:
        imdb_score[second] = lst[1]
    except: 
        print ('API network error 2. Re-running the function')
        get_imdb_scores()
    try: 
        imdb_score[third] = lst[2]
    except: 
        print ('API network error 3. Re-running the function')
        get_imdb_scores()

    return imdb_score
    


def default_function():
    print("This program will mainly obtain four information of a inquired TV show from the list.")
    print('1. Rotten Tomato Score of a selected show')
    print('2. First Actor listed under the Cast list')
    print('3. Three top listed movies of that actor - Obtained by accessing the href associated with the actor')
    print('4. IMDb score of the each three movies - Obtained using Google Search API for each movie titles \n')
    print('Loading Rotten Tomato page for the selected tv show... \n')
    actor_percentage = get_score_actor()
    actor = actor_percentage[0]
    perc = actor_percentage[1]
    print('\n')
    print('Rotten Tomato score ', perc)
    print('First Actor in the Cast List: ', actor, '\n')
    print('... \n')
    print("Scraping actor's profile url from the tv show page... \n")
    print('... \n')
    print("Loading actor's profile page on Rotten Tomato \n")
    mov = get_three_movies(link)
    print('The Three highly ranked movies on Rotten Tomato ', actor, 'is acting in: ')
    print(mov, '\n')
    print('... \n')
    print('Using API to fetch IMDb score for each movies... \n')  
    print ('This make take up some time. Thank you for being patient. \n')
    imdb = get_imdb_scores()
    print('IMDb scores for the three movies: ', imdb,'\n')
    print('Program done')
    

def static_function():
    print('Which TV show would you want to search?')
    print('1. Squid Game   2. Derek   3. Self Made   4. Friends   5. You')
    quest= int(input('Enter the corresponding number from 1 to 5: '))
    if quest == 1:
        quest = 'Squid Game'
        print ('You chose, Squid Game')
    if quest == 2:
        quest = 'Derek'
        print('You chose, Derek')
    if quest == 3:
        quest = 'Self Made'
        print('You chose, Self Made')
    if quest == 4:
        quest = 'Friends'
        print('You chose, Friends')
    if quest == 5:
        quest = 'You'
        print ('You chose, You')
    lst = []
    with open('movie_lists.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for i in row:
              if row[0]==quest:
                lst.append(i)
        print('\n')
        print ('Rotten Tomato Rating: ', lst[2], '\n')
        print ('First Actor on the Cast List: ', lst[3], '\n')
        print ('Three highly ranked movies ', lst[3], 'is in: ', lst[5], '\n')
        movs = lst[5].split(',')
        scrs = lst[6].split(',')
        print ('IMDb scores of the three movies: ', movs[0], ' :', scrs[0], ';',movs[1], ' :', scrs[1], ';', movs[2], ' :', scrs[2])


if __name__ == '__main__':
    if len(sys.argv) == 1:
        default_function()
    elif sys.argv[1] == '--static':
        static_function()
