>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
January 2025

### Project Title
Bikeshare Project

### Description
The Bikeshare Project allows users to analyze bikeshare data for cities such as Chicago, New York, and Washington. Users can choose the city, apply filters based on time periods (month or day), and view important statistics related to bike usage, including popular stations, trip duration, and user demographics. This project uses data from the Bike Share program in these cities to offer insights on bike sharing trends.

### Files used
`bikeshare.py`
`chicago.csv`
`new_york_city.csv`
`washington.csv`

### Credits
Used https://www.geeksforgeeks.org/ for some syntax problems i faced.
Used the built in Udacity AI to help me fix minor issues and understand exactly what is expected from me in the project

## Instalation

To set up and run the Bikeshare project locally, follow the steps below:

### Step 1: Clone the Repository

First, clone the repository from GitHub to your local machine. Open your terminal or Git Bash and run:
git clone https://github.com/yourusername/pdsnd_github.git

### Step 2: Install Python
This project requires Python to run. If you don't have Python installed, you can download it from Python's official website.

Follow the installation instructions on the website for your operating system.

### Step 3: Install Required Dependencies
Once you have Python installed, you’ll need to install the necessary Python library: Pandas. This can be done using pip, the Python package manager.

To install Pandas, open your terminal or Git Bash and run:
pip install pandas

### Step 4: Prepare the CSV Data Files
The project requires three CSV files containing the bikeshare data for Chicago, New York, and Washington. These files are already included in the repository, but make sure you have them in the correct folder.

The CSV files are:

chicago.csv
new_york_city.csv
washington.csv
These files are located in the same project repository.

### Step 5: Run the Project
After installing the dependencies and ensuring the data files are in place, you're ready to run the project. In your terminal or Git Bash, navigate to the project folder and run the following command:
python bikeshare.py

This will start the program, and you will be prompted to choose a city (Chicago, New York, or Washington) and select time filters (month or day).

### Step 6: View the Output
After selecting your filters, the program will display various statistics, such as:

Most popular month
Most popular day
Most popular hour
Total and average trip durations
Most popular start and end stations
Most popular trip (from start station to end station)
User type counts (Subscribers and Customers)
Gender and birth year statistics (if available)

The program will also ask if you would like to view raw data in chunks of 5 rows, and you can restart the analysis as needed.
