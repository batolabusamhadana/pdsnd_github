import pandas as pd
import time

# Filenames
CITY_FILES = {
    'chicago': 'chicago.csv',
    'new york': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_city():
    """Prompt the user to select a city and validate input."""
    while True:
        # Ask the user to choose a city
        city = input("\nHello! Let's explore some US bikeshare data!\n"
                     "Would you like to see data for Chicago, New York, or Washington?\n").strip().lower()
        # Check if the input matches available cities
        if city in CITY_FILES:
            return CITY_FILES[city]
        print("Invalid input. Please enter 'Chicago', 'New York', or 'Washington'.")

def get_time_period():
    """Prompt the user to specify a time filter and validate input."""
    while True:
        # Ask the user to choose a time filter
        time_period = input("\nWould you like to filter the data by 'month', 'day', or not at all? Type 'none' for no time filter.\n").strip().lower()
        # Check if the input is valid
        if time_period in ['month', 'day', 'none']:
            return time_period
        print("Invalid input. Please enter 'month', 'day', or 'none'.")

def get_month():
    """Prompt the user to select a month and validate input."""
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        # Ask the user to choose a month
        month = input("\nWhich month? January, February, March, April, May, or June?\n").strip().lower()
        # Check if the input is valid
        if month in months:
            return months.index(month) + 1
        print("Invalid input. Please enter a valid month.")

def get_day():
    """Prompt the user to select a day of the week and validate input."""
    while True:
        # Ask the user to choose a day
        day = input("\nWhich day? Please type your response as an integer (1 for Monday, 7 for Sunday).\n")
        # Check if the input is valid
        if day.isdigit() and 1 <= int(day) <= 7:
            return int(day)
        print("Invalid input. Please enter an integer between 1 and 7.")

def load_data(city_file, time_period, month=None, day=None):
    """Load and filter the data based on user input."""
    # Load the data from the selected city file
    data = pd.read_csv(city_file)
    data['Start Time'] = pd.to_datetime(data['Start Time'])

    # Filter data by month if applicable
    if time_period == 'month':
        data = data[data['Start Time'].dt.month == month]
    # Filter data by day if applicable
    elif time_period == 'day':
        data = data[data['Start Time'].dt.weekday == (day - 1)]

    return data

def display_data(data):
    """Display raw data in chunks of 5 rows upon user request."""
    start_loc = 0
    while True:
        # Ask the user if they want to see raw data
        display = input("\nWould you like to view individual trip data? Type 'yes' or 'no'.\n").strip().lower()
        if display == 'yes':
            # Display 5 rows of data
            print(data.iloc[start_loc:start_loc + 5])
            start_loc += 5
        elif display == 'no':
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def popular_month(data):
    """Find and return the most popular month for start time."""
    # Get the most common month
    return data['Start Time'].dt.month.mode()[0]

def popular_day(data):
    """Find and return the most popular day of the week for start time."""
    # Get the most common day of the week
    return data['Start Time'].dt.day_name().mode()[0]

def popular_hour(data):
    """Find and return the most popular hour for start time."""
    # Get the most common hour
    return data['Start Time'].dt.hour.mode()[0]

def trip_duration(data):
    """Calculate and return total and average trip durations."""
    # Calculate total and average duration
    total_duration = data['Trip Duration'].sum()
    avg_duration = data['Trip Duration'].mean()
    return total_duration, avg_duration

def popular_stations(data):
    """Find and return the most popular start and end stations."""
    # Get the most common start and end stations
    start_station = data['Start Station'].mode()[0]
    end_station = data['End Station'].mode()[0]
    return start_station, end_station

def popular_trip(data):
    """Find and return the most popular trip (start station to end station)."""
    # Get the most common trip
    trip = data.groupby(['Start Station', 'End Station']).size().idxmax()
    return trip

def user_counts(data):
    """Count user types and return results."""
    # Count the number of each user type
    return data['User Type'].value_counts()

def gender_counts(data):
    """Count gender and return results (if available)."""
    # Check if gender data is available
    if 'Gender' in data.columns:
        return data['Gender'].value_counts()
    return "No gender data available."

def birth_years(data):
    """Calculate earliest, most recent, and most popular birth years (if available)."""
    # Check if birth year data is available
    if 'Birth Year' in data.columns:
        earliest = int(data['Birth Year'].min())
        most_recent = int(data['Birth Year'].max())
        most_popular = int(data['Birth Year'].mode()[0])
        return earliest, most_recent, most_popular
    return "No birth year data available."

def statistics():
    """Calculate and display statistics based on user choices."""
    # Get user input for city and time period
    city_file = get_city()
    time_period = get_time_period()

    # Initialize variables for filtering
    month = None
    day = None
    if time_period == 'month':
        month = get_month()
    elif time_period == 'day':
        day = get_day()

    # Load filtered data
    data = load_data(city_file, time_period, month, day)

    # Display statistics for the data
    print(f"\nMost popular month: {popular_month(data) if time_period == 'none' else 'Filtered by time period'}")
    print(f"Most popular day: {popular_day(data) if time_period != 'month' else 'Filtered by time period'}")
    print(f"Most popular hour: {popular_hour(data)}")

    # Display trip duration statistics
    total_duration, avg_duration = trip_duration(data)
    print(f"\nTotal trip duration: {total_duration} seconds")
    print(f"Average trip duration: {avg_duration:.2f} seconds")

    # Display popular stations
    start_station, end_station = popular_stations(data)
    print(f"\nMost popular start station: {start_station}")
    print(f"Most popular end station: {end_station}")

    # Display popular trip
    trip = popular_trip(data)
    print(f"\nMost popular trip: {trip[0]} to {trip[1]}")

    # Display user type counts
    print(f"\nUser type counts:\n{user_counts(data)}")
    
    # Display gender counts if available
    print(f"\nGender counts:\n{gender_counts(data)}")

    # Display birth year statistics if available
    birth_year_data = birth_years(data)
    if isinstance(birth_year_data, tuple):
        print(f"\nEarliest birth year: {birth_year_data[0]}")
        print(f"Most recent birth year: {birth_year_data[1]}")
        print(f"Most popular birth year: {birth_year_data[2]}")
    else:
        print(f"\n{birth_year_data}")

    # Ask if user wants to see raw data
    display_data(data)

    # Ask if user wants to restart
    restart = input("\nWould you like to restart? Type 'yes' or 'no'.\n").strip().lower()
    if restart == 'yes':
        statistics()

if __name__ == "__main__":
    statistics()
