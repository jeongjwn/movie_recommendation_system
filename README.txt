How to run the code?

In order to run this code, several libraries should be imported. Libraries are sys, urllib.request, urllib.parse, urllib.error, BeautifulSoup, requests, csv, and json. These libraries are already included to be imported in the coding. 

The name of the file containing the script is 'movie_recommendation_system.py'. When the script is run, the user will be asked to select from 1 to 5 with corresponding tv shows, Squid Game, Derek, Self Made, Friends, and You.
Then, the program will get four information about a selected tv show.
1. Rotten Tomato Score 
2. Actor’s name of the first under the cast list.
3. Three movies that are highly rated score (Rotten Tomato) of the actor.
4. The IMDB score for the three movies.
 
The first and second data is obtained by an html scraping the Rotten Tomato's Squid Game page. 
As it is getting the actor's name, it also gets the href corresponding to the actor. That new link will have the actor's filmography, which will be scraped for the third data, three highly-rated movies.  
When the third data is obtained, it will be used for the fourth data, which will be obtained by using API. Each movie title will be used to scrape the IMDB score using API. This part may take up some time since it is looping three times to obtain the data of three movies using the API.
To obtain the fourth data using API, it requires API key:  '91894908139emsh92b456a701aa261p16d15fjsn0af998a67950'. This key is already included in the script. The user does not need to input it. 
 
Because these data are interconnected, it is important to run the whole coding to obtain the full data.  
 
The code has a likelihood of breaking if the code behind the Rotten Tomato web content or the IMDB web content changes. Another possibility is if an API key is expired. 
Because the last data obtained using API takes a bit of time to print the outcome as it is running the code three times (for three movies), it may result in an unexpected outcome when repeatedly run. If that is the case, I recommend running the program again. The script includes the code to be re-run when the outcome is not collected, but an error still may occur when the program takes too long to fetch the inquired data. 

If this is the case, I recommend running the static_function to first grasp the idea of what the outcome data should be. 

The static_function uses the dataset named 'movie_list.csv', which contains the collected data on the web. Therefore, will output the data without scraping the web and API.
 
The result may differ from the default_function as the default_function is scraping the dynamic data from the web. The ratings are continuously collected from the reviewers, therefore the outcome may differ from the already collected data (movie_list.csv), which was collected on December 6th, 2021. 