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

The traffic hotspot analyzer utilizes genetic algorithms to identify congested areas. Here's a brief overview of the algorithm:

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
