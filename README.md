# Traffic-Hotspot-Analysis
Link for clusters : https://docs.google.com/spreadsheets/d/1VjruqSdH23siGX02QeTW6gPvpM3m550IURdzH1xuJlE/edit#gid=657859843
Link for the on which the clusters are plotted: https://datastudio.google.com/reporting/d14e5250-f701-4e9a-a7ce-9f9e3a4aa1c3/page/8vJ7C




# Traffic Hotspot Analyzer using Genetic Algorithms

This repository contains a traffic hotspot analyzer implemented using genetic algorithms. The analyzer aims to identify areas with high traffic congestion and provide recommendations for potential solutions.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Overview](#algorithm-overview)
- [Results](#results)
- [Contributors](#contributors)
- [License](#license)

## Introduction
Traffic congestion is a significant problem in urban areas, leading to increased travel times, fuel consumption, and air pollution. This project aims to address this issue by implementing a traffic hotspot analyzer using genetic algorithms. The analyzer takes traffic data as input and provides insights into areas with high congestion levels.

## Installation
To use the traffic hotspot analyzer, follow these steps:

1. Clone the repository:

```shell
git clone https://github.com/Krishanadave671/Traffic_hotspot_Analyzer-using-genetic-Algorithms.git
```
2. Navigate to the project Directory 
```
cd Traffic_hotspot_Analyzer-using-genetic-Algorithms
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
## Usage 
1. Prepare your traffic data in a suitable format. The expected input format can be found in the data/ directory.

2. Run the traffic hotspot analyzer:
```
python analyzer.py
```
3. Follow the on-screen prompts to provide the necessary information and parameters for the analysis.

4. Once the analysis is complete, the analyzer will generate a report with hotspot locations and recommendations for potential solutions.

## Algorithm overview 

## Motivation :-
Twitter is a social media app used for contacting officials and lodging complaints by tagging their Twitter accounts. People all over the globe have started using Twitter, and nowadays they are very active on the platform. They tweet their complaints, and even the Mumbai Traffic Police has created a Twitter account to address the daily traffic issues faced by Mumbaikars.

The official Twitter handle of the Mumbai Traffic Police is @MTPHereToHelp. They provide traffic updates and accept complaints or updates about traffic blockages from other Twitter users who tag them. @MTPHereToHelp has a Twitter bot that replies to the user's tweet and forwards the complaint to the respective traffic division from where the complaint originated.

The replies given by the bot follow a particular pattern. We have observed that their replies often look like this and mostly involve complaints regarding traffic: "We have escalated your request with Nagpada Traffic Division for necessary action."

These complaints are specific to a particular division, indicating that there is traffic in that particular location. Therefore, we can conclude that the number of tweets to which @MTPHereToHelp has replied indicates the level of traffic, as more users are facing that traffic issue.

However, it would be incorrect to conclude the most traffic hotspot zones based solely on this data. The number of tweets may be less in a particular traffic division, as it depends on the users tweeting about the traffic. Therefore, claiming that the areas with the most tweets are the most traffic-congested zones would yield inaccurate results.

Nevertheless, we can create clusters of users where more traffic complaints are received. This can help the Mumbai Traffic Police make strategic decisions based on the clustering analysis. It will assist them in addressing the traffic issues efficiently.

## Algorithmic Overview 
for this clustering analysis , procedure or algorithm to find data insights as follows :-

1. # Fetch the data from twitter :
      Twitter Api is available for developers which can be used to fetch the twitter data from @MTPHereToHelp account Tweepy is a library in python for extracting data from twitter 
      since we needed the retweets from MTpHereToHelp account so we fetched the retweets 
      ```
      search_words = "from:MTPHereToHelp -filter:retweets"
      ```
      we were able to fetch the tweets of just last 7 days since twitter api was providing this much timeline in free tier it would be more better in result if we would have provided data of more than 100 days   
      
      dataset columns features include :- 'Tweets', 'id', 'len', 'date', 'time', 'source', 'likes',
       'retweets'
      data length - 867 
       [click to view dataset](https://docs.google.com/spreadsheets/d/1VjruqSdH23siGX02QeTW6gPvpM3m550IURdzH1xuJlE/edit?usp=sharing)

2. # Extracting the location from the tweets : 
       our tweets mostly have patterns like this 
       for eg :- "We have escalated your request with Nagpada Traffic Division for necessary action."
       since we want to cluster based on location and each tweet we can see location by traffic division so we need to Extract the location from given tweets 

    - First Approach : 
      since there are only 34 locations of traffic division available in Mumbai so we got all the traffic divisions from this data available on official website of Mumbai traffic police [click here](https://trafficpolicemumbai.maharashtra.gov.in/wp-content/uploads/2021/01/Traffic-Division.pdf) 

    - Second Approach :
      second approach is we can use an NLP technique on text 
      i.e. NER (named entity recoginition) and extract the traffic divisions from text as Traffic divisions are entity 
      Also we can use [spacy](https://spacy.io/) library for extracting entity from the text and add it to the new column 
      since first was the easiest and to avoid complexity  we did gone for first approach since using NLP there might be some constraints we need to handle 
 
3. # Cleaning the data :
       some of tweets might not contain locations in the text since we want to analyze the tweets which contains traffic division location and we want to cluster the hotspot of traffic zones so those tweets whose location is not mentioned cannot be used for analyzing so we drop that rows 
   After dropping  
   data length - 409 

4. # Grouping the data by Traffic Divisons :- 
       we grouped the data according to traffic division since we have traffic divison and their tweet counts 
5. # Kmeans algorithm :- 
       Kmeans algorithm applied on grouped data using [sklearn](https://scikit-learn.org/stable/) library and made (k = 4) clusters and plot on the Bubble map so traffic police can get insights about data  about which traffic division has most complaints or where more attention traffic police required. 

6. # Genetic algorithm :-          
       

Initialization: The algorithm starts by creating an initial population of potential solutions, representing different combinations of traffic hotspot locations.

Evaluation: Each solution in the population is evaluated based on its fitness, which measures the congestion levels in the corresponding hotspot locations.

Selection: The fittest solutions from the population are selected for further breeding.

Crossover: The selected solutions undergo crossover, where their genetic information is exchanged to create new offspring solutions.

Mutation: Some of the offspring solutions undergo random mutations to introduce diversity and explore new areas of the search space.

Replacement: The offspring solutions replace a portion of the existing population.

Termination: The algorithm iteratively performs the above steps until a termination criterion is met, such as reaching a maximum number of generations or achieving a desired level of fitness.

## Results 
The analyzer generates a report containing the identified traffic hotspots and recommendations for potential solutions. These recommendations could include infrastructure improvements, traffic signal optimization, or changes in traffic flow management.

## Contributors
- [Bhavesh Daphale](https://www.linkedin.com/in/bhavesh-daphale-681598238/)
- [Krishana Dave](https://www.linkedin.com/in/krishana67/)
- [Prajwal Dhule](https://www.linkedin.com/in/prajwal-dhule/)
- [Ayush dodia](https://www.linkedin.com/in/ayush-dodia/)

# Mentors 
- [Ujwala Bharambe](https://www.linkedin.com/in/drujwala2702/)

## License
This project is licensed under the MIT License.

Feel free to reach out if you have any questions or need further assistance. Happy analyzing!
