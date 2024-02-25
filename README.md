# Pandas Data Analysis

## Overview
This program was created to learn how to analyze data using Pandas and Python. It uses functions such as groupby, size, and max to filter data. Matplotlib is also used to create graphs to display the data in a more readable way. I wanted to learn more about how to use these libraries to analyze data.

A video game sales data set was found on kaggle.com, originally from [a scrape done on vgchartz](https://zenodo.org/records/5898311#.Y9Y2K9JBwUE). It details the sales for video games that have surpassed 100,000 units sold, as well as their platform, genre, and release year. When working with data, it is important to know how the information was gathered and when it was last updated. Some of the data headings may be misleading, such as "Year" actually meaning "Release Year." There is also no indication for when sales counting last occurred, or why there aren't many games from 2016 onward.

[Software Demo Video]()

## Data Analysis Results
Questions:
* What is the highest selling game for each platform?
* What release year has titles with the most sales?

Results:
* I was able to create a table that displays the best selling game per platform, with Wii Sports being the overall best-seller with 82 million copies sold for the Wii
* 2008's titles had the most video game sales with 678 million copies sold

## Development Environment
* Python (3.11.7)
* Pandas (2.2.1)
* Matplotlib (3.8.3)
* Visual Studio Code (1.86.2)

## Useful Websites
* [Kaggle Data Set](https://www.kaggle.com/datasets/thedevastator/global-video-game-sales)
* [Pandas - Filtering Data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)

## Future Work
* Create different types of graphs
* Save created DataFrames to a file
* Display tables using Matplotlib/another graphics library
* Additional questions/user determined questions

## Additional Ideas
* User can specify a file to get data from
* Work with other filetypes (determine function to use based on file ending)
* Implement CRUD (Create Read Update Delete)
