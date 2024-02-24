# Author: Ashley DeMott
# Project: Data Analysis using Pandas and MatPlotLib 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

FILENAME = "vgsales.csv"

def get_data_set():
    """ Returns a Pandas DataFrame from a file"""
    # FUTURE TODO:
    # Can prompt data set from user
    # Determine pandas function based on filetype

    data = pd.read_csv(FILENAME)
    return data

def get_platform_best_sellers(vg_sales):
    """ Given the sales data for video games, returns a DataFrame with the best selling games per platform"""
    
    # Get the highest global sales, grouped by platform
    platform_best = vg_sales.groupby("Platform")["Global_Sales"].idxmax()

    # Get the entire row for each platform best sellers
    platform_best  = vg_sales.loc[platform_best]

    # Sort the values by global sales, most to least
    platform_best = platform_best[["Platform", "Name", "Global_Sales"]].sort_values("Global_Sales", ascending=False)
    
    # TODO: Doesn't rename column?
    #platform_best.rename(columns={"Global_Sales": "Global Sales (millions)"})

    return platform_best

def get_year_global_sales(vg_sales):
    """ Given the sales data for video games, returns a DataFrame with total sales per year"""
        
    # Drops rows with a N/A in them (N/A for year, global sales)
    year_best = vg_sales[["Year", "Global_Sales"]].dropna()

    # Explicitly cast each column to a specific data type (Year defaults to float)
    year_best = year_best.astype({"Year": int, "Global_Sales": float})

    # Group games sold in the same year together
    year_best = year_best.groupby("Year")["Global_Sales"].sum()
    
    #year_best = year_best.sort_values(ascending=False)

    #vg_sales.groupby("Year")["Global_Sales"].agg('sum')
    year_best = pd.DataFrame({"Year": year_best.index, "Global Sales": year_best})

    return year_best

def get_year_num_games(vg_sales):
    """ Gets the number of games (that sold 100k+ copies) that were released each year"""
    #year_games = vg_sales[["Year", "Name"]]
    year_games = vg_sales[["Year", "Name"]].dropna().astype({"Year": int})
    year_games = year_games.groupby("Year").count()
    year_games = year_games.rename(columns={"Year": "Year", "Name": "Games with 100k sales"})
    year_games = year_games.sort_values("Games with 100k sales", ascending=False)
    #year_games = vg_sales[["Year", "Name"]].dropna()
    #year_games = year_games.astype({"Year": int, "Name": str})
    
    #year_games = year_games.groupby("Year").sum()
    #year_games["Count"] = year_games.groupby("Year").sum()

    #year_games = year_games.sort_values("Count", ascending=False)

    return year_games

def get_genre_by_year(vg_sales):
    """ Get the most common genre sold each year"""
    year_genre = vg_sales[["Year", "Genre"]].dropna().astype({"Year": int})
    
    year_genre = year_genre.groupby("Year")["Genre"].agg(pd.Series.mode)

    #year_genre.rename("Most popular genre by year")

    # Series do not have columns?
    #year_genre.rename(columns= {year_genre.columns[1]: "Most popular genre"})

    return year_genre

def graph_global_sales(year_global_sales):
    """ Graphs the global sales by year"""
        
    # Data to be graphed
    x = year_global_sales["Year"]
    y = year_global_sales["Global Sales"]

    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Add titles and axis labels
    fig.suptitle("Game Sales by Year", fontsize=14, fontweight="bold")
    ax.set_title("*Only includes games that sold over 100,000 units", fontsize=10)

    plt.xlabel("Year")
    plt.ylabel("Global Sales in millions")

    # Show the plot
    plt.show()

vg_sales = get_data_set()

# Question 1: What are the best selling games per platform?
# Displays DataFrame to console, removes index column
print("Best selling games per platform:")
platform_best_sellers = get_platform_best_sellers(vg_sales)
print(platform_best_sellers.to_string(index=False))

# Question 2: What year sold the most games?
#print(get_year_num_games(vg_sales).to_string())
print("Global sales (in millions) per year (of games with 100k sales):")
year_global_sales = get_year_global_sales(vg_sales)
print(year_global_sales.sort_values("Global Sales", ascending=False).to_string(index=False))
graph_global_sales(year_global_sales)

# Additional questions
# Most popular genre for each year
#print(get_genre_by_year(vg_sales).to_string())

#print(vg_sales.head())
#print(vg_sales.dtypes)

# Game that sold best for each platform
#platform = vg_sales[["Platform", "Name", "Global_Sales"]].copy()

#platform = vg_sales.groupby("Platform")["Global_Sales"].first()
#platform["Name"] = vg_sales["Name"].transform()

#platform.insert(1, "Rank", platform.sort_values("Global_Sales", ascending=False).index, True)

#print(platform.groupby("Platform")["Global_Sales"].max().reset_index())

#print(platform.sort_values("Global_Sales", ascending=False))

#print(platform["Platform"].value_counts())

#platform = vg_sales.groupby(["Platform", "Name"])["Global_Sales"].transform("max") == vg_sales["Global_Sales"]
#print(vg_sales[platform])

#print(vg_sales.groupby(["Platform"])["Global_Sales"].agg("max"))
#print(vg_sales.groupby(["Platform"])["Global_Sales"].max().reset_index().sort_values(["Global_Sales"], ascending=False))

#print(vg_sales[["Platform", "Name", "Global_Sales"]].groupby("Platform").max())

# Year with most global sales
#print(vg_sales[["Year", "Global_Sales"]].groupby("Year").sum().sort_values("Global_Sales", ascending=False))

#year_best = vg_sales.loc[vg_sales.groupby("Year")["Global_Sales"].agg()]
#year_best = year_best[["Year", "Global_Sales"].sort_values("Year")]