import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'Chicago': 'chicago.csv',
    'New York City': 'new_york_city.csv',
    'Washington': 'washington.csv'
}

def get_filters():
    while True:
        print('\nHello! Let\'s explore some US bikeshare data!')
        city = input("\nWhich city would you like to analyze? "
                     "Chicago, New York City, or Washington?\n").strip().title()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city selection. Please choose from Chicago, New York City, or Washington.")

    while True:
        month = input("\nWhich month would you like to filter by? "
                      "January, February, March, April, May, June, or type 'all' for no filter?\n").strip().title()
        if month in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
            break
        else:
            print("Invalid month selection. Please choose from January to June or 'all'.")

    while True:
        day = input("\nAre you looking for a specific day of the week? "
                    "Enter the day name (e.g., Monday) or type 'all' for no filter.\n").strip().title()
        if day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All'):
            break
        else:
            print("Invalid day selection. Please enter a valid day name or 'all'.")

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name()

    if month != 'All':
        month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6}
        month_num = month_dict.get(month)
        df = df[df['Month'] == month_num]

    if day != 'All':
        df = df[df['Day'] == day]

    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    popular_month = df['Month'].mode()[0]
    print('Most Common Month:', popular_month)

    popular_day = df['Day'].mode()[0]
    print('Most Common Day of the Week:', popular_day)

    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', start_station)

    end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', end_station)

    most_common_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print('Most Common Trip from Start to End:', most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time, 'seconds')

    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    if 'Gender' in df:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types)
    else:
        print('\nGender Types: No data available for this city.')

    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])

        print('\nEarliest Birth Year:', earliest_birth_year)
        print('Most Recent Birth Year:', most_recent_birth_year)
        print('Most Common Birth Year:', most_common_birth_year)
    else:
        print('\nBirth Year Statistics: No data available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_raw_data(df):
    start_loc = 0
    while True:
        view_data = input("\nWould you like to view 5 rows of raw data? Enter yes or no.\n").strip().lower()
        if view_data != 'yes':
            break
        else:
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').strip().lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()

