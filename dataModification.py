# Author: Ashley DeMott
# Project: Using Pandas to create, read, update, and delete data in a DataFrame. Also read and save data to a file.
import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename):
    """Loads data from a specified file into a Pandas DataFrame"""
    # TODO: Determine Pandas function based on file ending

    data = pd.read_csv(filename)
    return data

def save_data(dataFrame):
    """Save the given DataFrame to a specified file"""

    filename = prompt_user("Please enter a filename")
    # TODO: assert filename has filetype on it (else save as a default? (choose between csv, excel, json, etc))

    # Save

# TODO: Add parameters, like columns to show, filtering, sorting
def print_data(dataFrame):
    """Display the given dataFrame in the console"""
    print(dataFrame)

def graph_data(data):
    """Graphs the specified data on a 2D plot"""

    # TODO: Error and user input handling. Data must be numerical
    # TODO: If only two columns, use those without prompting
    # Prompt the user for the data to display
    x_axis = prompt_user("Please enter the column to display on the x axis")
    y_axis = prompt_user("Please enter the column to display on the y axis")

    x = data[x_axis]
    y = data[y_axis]

    fig, ax = plt.subplots()
    ax.plot(x, y) # Plot the graph

    # Add titles and axis labels
    fig.suptitle(prompt_user("Please enter the graph's title"), fontsize=14, fontweight="bold")
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)

    # Show the plot in its own window
    plt.show()

def display_menu():
    """Display user's options"""
    # TODO: Currenlty just ideas

    # TODO: Add new rows of data to the DataFrame
    # TODO: Add new columns to the DataFrame (based on existing data)
    # TODO: Update a specified row/column in the DataFrame
    # TODO: Delete a given row in the DataFrame
    print("1. Create") # Could create sub-menus for each
    print("Create new row")    
    print("Create new column")

    print("2. Read")
    print("Show data in a table")
    print("Show data in a plot")
    print("Show specific rows")
    print("Show specific columns")

    print("3. Update")
    print("Update specific row/column")
    print("Update all matching (rename)")

    print("4. Delete")
    print("Delete row")
    print("Delete column")
    print("Delete all rows matching filter")

    print("Save data")
    print("Choose another dataset")
    print("Quit")

def prompt_user(prompt):
    """Prompts the user for input"""
    input = input(f"{prompt}: ")
    return input

def main():
    # load_file = prompt_user("Please enter a file to load data from")
    # data = load_data(load_file)
    # display_menu()
    # menu_choice = prompt_user("Pick a menu choice")
    # switch(user_choice) # <-- Display, sort, filter, add, update, delete, save, etc

    data = load_data("vgsales.csv")
    print_data(data.head().to_string(index=False)) # Print only the first few

if __name__ == "__main__":
    main()