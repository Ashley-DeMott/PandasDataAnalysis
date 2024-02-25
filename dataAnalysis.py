# Author: Ashley DeMott
# Project: Data Analysis using Pandas and MatPlotLib 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# The file where the data is read from
FILENAME = "vgsales.csv"

def get_data_set():
    """Returns a Pandas DataFrame from a file"""
    # FUTURE TODO:
    # Can prompt data set from user
    # Determine pandas function based on filetype

    data = pd.read_csv(FILENAME)
    return data

def get_platform_best_sellers(vg_sales):
    """Given the sales data for video games, returns a DataFrame with the best selling games per platform"""
    # Get the highest global sales, grouped by platform
    platform_best = vg_sales.groupby("Platform")["Global_Sales"].idxmax()

    # Get the entire row for each platform best sellers
    platform_best  = vg_sales.loc[platform_best]

    # Sort the values by global sales, most to least
    platform_best = platform_best[["Platform", "Name", "Global_Sales"]].sort_values("Global_Sales", ascending=False)
    
    # Rename column to clarify data
    platform_best = platform_best.rename(columns={"Global_Sales": "Global Sales (in millions)"})

    return platform_best

def get_year_global_sales(vg_sales):
    """ Given the sales data for video games, returns a DataFrame with total sales per year"""
    # Drops rows with a N/A in them
    year_best = vg_sales[["Year", "Global_Sales"]].dropna()

    # Explicitly cast each column to a specific data type (Year defaults to float)
    year_best = year_best.astype({"Year": int, "Global_Sales": float})

    # Group games sold in the same year together
    year_best = year_best.groupby("Year")["Global_Sales"].sum()

    # Create a new DataFrame with Year and Global Sales as separate named columns
    year_best = pd.DataFrame({"Year": year_best.index, "Global Sales (in millions)": year_best})
    year_best.sort_values("Global Sales (in millions)", ascending=False)

    return year_best

def get_year_num_games(vg_sales):
    """ Gets the number of games (that sold 100k+ copies) that were released each year"""
    # Using only the Year and Genre columns, drop rows with N/A
    #  and make sure Year column is integers and not float
    year_games = vg_sales[["Year", "Name"]].dropna().astype({"Year": int})

    # Get the years and the number of names for each year
    year_games = pd.DataFrame({"Year": year_games["Year"].unique(), "Num Games": year_games.groupby("Year").size() })

    # Drop the indicies (groupby adds year as index)
    year_games = year_games.reset_index(drop=True)

    # Sort the years by the number of games
    year_games = year_games.sort_values("Year", ascending=False)

    return year_games

def get_year_num_games_million(vg_sales):
    """ Gets the number of games that sold 1 million copies, by release year"""
    # Using only the Year and Genre columns, drop rows with N/A
    #  and make sure Year column is integers and not float
    year_games = vg_sales[["Year", "Global_Sales"]].dropna().astype({"Year": int})

    year_games_million = year_games[year_games["Global_Sales"] > 1.0]

    # Get the years and the number of names for each year
    year_games_million = pd.DataFrame({"Year": year_games_million["Year"].unique(), "Num Games": year_games_million.groupby("Year").size() })

    # Drop the indicies (groupby adds year as index)
    year_games_million = year_games_million.reset_index(drop=True)

    # Sort the years by the number of games
    year_games_million = year_games_million.sort_values("Year", ascending=False)

    return year_games_million

def get_genre_year(vg_sales):
    """ Get the most popular genre per year with how many games sold 100k+"""
    # Using only the Year and Genre columns, drop rows with N/A
    #  and make sure Year column is integers and not float
    year_genre = vg_sales[["Year", "Genre"]].dropna().astype({"Year": int})

    # Grouping by Year, get the counts for each Genre
    year_genre = year_genre.groupby("Year")["Genre"].value_counts()

    # Get the maximum count for year/genre Series, unzip the tuple into year and genre
    year, genre = zip(*year_genre.groupby("Year").idxmax().values)

    # Create a new DataFrame with the Year, Genre, and the max counts per Year
    best_year_genre = pd.DataFrame({"Year": year, "Genre": genre, "Count": year_genre.groupby("Year").max()})

    return best_year_genre

def graph_global_sales(year_global_sales):
    """Graphs the total global sales by year"""        
    # Data to be graphed
    x = year_global_sales["Year"]
    y = year_global_sales["Global Sales (in millions)"]

    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Add titles and axis labels
    fig.suptitle("Game Sales by Year", fontsize=14, fontweight="bold")
    ax.set_title("*Only includes games that sold over 100,000 units", fontsize=10)

    plt.xlabel("Year")
    plt.ylabel("Global Sales (in millions)")

    # Show the plot
    plt.show()

def graph_game_per_year(year_games):
    """Graphs the number of games selling 100k+ copies, by release Year"""
    # Data to be graphed
    x = year_games["Year"]
    y = year_games["Num Games"]

    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Add titles and axis labels
    fig.suptitle("Video Games Selling 100k copies", fontsize=14, fontweight="bold")

    plt.xlabel("Release Year")
    plt.ylabel("Number of Games")

    # Show the plot
    plt.show()

def graph_game_per_year_million(year_games_million):
    """Graphs the number of games selling 1M+ copies, by release year"""   
    # Data to be graphed
    x = year_games_million["Year"]
    y = year_games_million["Num Games"]

    fig, ax = plt.subplots()
    ax.plot(x, y)

    # Add titles and axis labels
    fig.suptitle("Video Games Selling 1 Million copies", fontsize=14, fontweight="bold")

    plt.xlabel("Release Year")
    plt.ylabel("Number of Games")

    # Show the plot
    plt.show()

def main():
    vg_sales = get_data_set()

    # Question 1: What are the best selling games per platform?
    # Displays DataFrame to console, removes index column
    print("Best selling games per platform:")
    platform_best_sellers = get_platform_best_sellers(vg_sales)
    print(platform_best_sellers.to_string(index=False))
    #print(f"Best seller overall: {platform_best_sellers.loc[platform_best_sellers['Global Sales (in millions)'].idxmax()]}")

    # Question 2: What year sold the most games (out of games selling over 100k copies)?
    print("\nGlobal sales per year (of games with 100k sales):")
    year_global_sales = get_year_global_sales(vg_sales)
    print(year_global_sales.to_string(index=False))
    print(f"Best selling year: {year_global_sales.loc[year_global_sales['Global Sales (in millions)'].idxmax()]}")

    # Display a graph for global sales by year (pauses terminal)
    graph_global_sales(year_global_sales)

    # Additional Questions

    # Most popular genre for each year
    print("\nMost popular genre grouped by release year:")
    year_genre = get_genre_year(vg_sales)
    print(year_genre.to_string(index=False))

    # Games that sold 100k+ per year
    print("\nNumber of games selling 100k units, grouped by release year:")
    year_games = get_year_num_games(vg_sales)
    print(year_games.sort_values("Num Games", ascending=False).to_string(index=False))
    #print(f"Total: {year_games['Games with 100k sales'].sum()}")

    # Display graph for successful games per release year (pauses terminal)
    graph_game_per_year(year_games.sort_values("Year", ascending=False))

    # Only including games that sold 1 million units
    print("\nNumber of games selling 1 million units, grouped by release year:")
    year_games_million = get_year_num_games_million(vg_sales)
    print(year_games_million.sort_values("Num Games", ascending=False).to_string(index=False))

    # Display graph for games selling 1 million, grouped by release year (pauses terminal)
    graph_game_per_year_million(year_games_million.sort_values("Year", ascending=False))

if __name__ == "__main__":
    main()