import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington D.C': 'washington.csv' }
# Data only includes firs 6 months of 2017
MONTH_DATA = { 'january': 1,  
               'february': 2,
               'march': 3,
               'april': 4,
               'may':5,
               'june': 6,
               'all': 7}
DAY_LIST = ['monday', 
            'tuesday', 
            'wednesday', 
            'thursday', 
            'friday', 
            'saturday', 
            'sunday',
            'all']         
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please select a city, options are: Chicago, New York City or Washington D.C: ")
    while True: 
            if city in CITY_DATA.keys():
                print("Thank you, that is valid.")
                break
        
            else:
                print("Sorry, incorrect input. Try again make sure you have the correct format. Type Chicago, New York City or Washington D.C: ")
                city = input("Please select a city:")
    
    print("You have selected " + city)
           
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please select a month between January and June to filter data by or type All for all months. ").lower()
    while True: 
            if month in MONTH_DATA.keys():
                print("That is valid")
                break
        
            else:
                print("Sorry, incorrect input. Try again make sure you have the correct format. The input is case sensitive.")
                month = input("Please select a month:")
    
    print("You have selected to filter by " + month)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please select a day of the week to filter by, or type all for all days: " ).lower()
    while True:
        if day in DAY_LIST:
            print("Thank you that is valid")
            break
            
        else: 
            print("Sorry try agin make sure day is spelled correctly and fully")
            day = input("Enter day of the week or select all: ")
            
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time']) #looks at colum and converts to needed format
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #Filter by month to create the new dataframe
        df = df[df['Month'] == month]
    
    if day != 'all':
        df = df[df['Day'] == day.capitalize()] #Filter it further by day.
    
    return df 


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popularMTH = df['Month'].mode()[0]
    printableMTH = months[popularMTH -1] #month 6 needs to be 5 due to months starting at index 0
    print('The most popular month is ' + printableMTH.capitalize())
    # TO DO: display the most common day of week
    popularDay = df['Day'].mode()[0]
    print ('The most popular day is ' + popularDay.capitalize())
 
    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour # Adds a new column to the dataset which is filled with just the hour from the Start Time column.
    
    startHour = df['Start Hour'].mode()[0]
    print(str(startHour) + ' is the most popular start time')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popStartStation = df['Start Station'].mode()[0]
    print(popStartStation)
    # TO DO: display most commonly used end station
    popEndStation = df['End Station'].mode()[0]
    print(popEndStation)
    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] =  df['Start Station'].str.cat(df['End Station'], sep=" to ")
    popCombo = df['trip'].mode()[0]
    
    print(popCombo + 'is the most popular trip')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTravelTime = df['Trip Duration'].sum()
    print('The total travel time is ' + str(totalTravelTime / 3600) + ' hours')
    
    # TO DO: display mean travel time
    meanTravelTime = df['Trip Duration'].mean()
    print('The mean travel time is ' + str(meanTravelTime / 3600) + ' hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    countsOfUsers = df['User Type'].value_counts()
    print('The counts of user types are below.')
    print(countsOfUsers)
    # TO DO: Display counts of gender

    if "Gender" in df.columns:
        countsOfGender = df['Gender'].value_counts()
        print('The counts of Genders are below.')
        print(countsOfGender)
    else:
        print('Gender data is not available.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliestYOB = int(df['Birth Year'].min()) 
        recentYOB = int(df['Birth Year'].max())
        commonYOB = int(df['Birth Year'].mode()[0])

        print(str(earliestYOB) + ' is the earliest year of birth')
        print(str(recentYOB) + ' is the most recent year of birth.')
        print(str(commonYOB) + ' is the most common year of birth.')
    else:
       print('Date of Birth info not available')
        
    print("\nThis took %s seconds." % (time.time() - start_time))   
    print('-'*40) 

def display_data(df):
    index=0
    user_input=input('Would you like to display 5 rows of raw data? (yes or no) ').lower()
    while user_input == 'yes' and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('Would you like to display 5 more rows of raw data? (yes or no) ').lower()
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
