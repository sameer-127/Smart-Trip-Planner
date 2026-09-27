# Smart Trip Planner


## Project Overview

Smart Trip Planner is a simple Python-based application that helps users create a basic travel plan according to their destination, number of days, total budget, travel style, and interests.

The program divides the total budget into different categories such as travel, hotel, food, activities, and emergency expenses. It also generates a daily budget and a day-wise travel plan based on the user's selected preference.

## Features

1. Accepts the travel destination from the user.
2. Takes the number of travel days.
3. Accepts the total travel budget.
4. Provides three travel styles:
    (a) Budget
    (b) Balanced
    (c) Luxury
5. Provides different travel preferences:
    (a)vAdventure
    (b) Nature
    (c) History
    (d) Food
    (e) Mixed
6. Automatically distributes the budget among:
    (a) Travel
    (b) Hotel
    (c) Food
    (d) Activities
    (e) Emergency
7. Calculates the daily travel budget.
8. Generates a day-wise travel plan.
9. Provides basic travel advice based on the daily budget.
10. Uses simple Python concepts suitable for beginners.


## Technologies Used

1. Python 3
2. input() for taking user input
3. if-elif-else for decision making
4. for loop for generating the daily travel plan
5. Variables and arithmetic operations
6. round() for displaying rounded budget values


## Project Structure

```text
Smart-Trip-Planner/
│
├── smart_trip_planner.py
└── README.md
```

## working of the program

Run the Program

Run the Python file using:

python smart_trip_planner.py

The program will ask you for:

1. Travel destination
2. Number of days
3. Total budget
4. Travel style
5. Travel preference

After entering the required information, the program will generate the trip analysis and travel plan.

## Example

```text
===================================================
             SMART TRIP PLANNER
===================================================

Where do you want to travel? Goa
How many days? 5
What is your total budget (₹)? 25000

Choose your travel style:
1. Budget
2. Balanced
3. Luxury

Enter choice: 2

What do you prefer?
1. Adventure
2. Nature
3. History
4. Food
5. Mixed

Enter choice: 1

The program will then display the budget plan, daily budget, day-wise travel activities, and travel advice.
```


## Instructions for Testing

Follow these steps to test the program:

### 1. Budget Travel

Enter:

Destination: Goa
Days: 5
Budget: 20000
Travel Style: 1
Preference: 1

Check that the program displays a budget-style distribution and adventure activities.

### 2. Balanced Travel

Enter:

Destination: Jaipur
Days: 4
Budget: 30000
Travel Style: 2
Preference: 3

Check that the program displays a balanced budget and historical activities.

### 3. Luxury Travel

Enter:

Destination: Mumbai
Days: 3
Budget: 60000
Travel Style: 3
Preference: 4

Check that the program displays a higher hotel allocation and food-related activities.

### 4. Mixed Preference

Enter:

Destination: Kerala
Days: 6
Budget: 40000
Travel Style: 2
Preference: 5

Check that the daily plan displays:

Sightseeing + food + local activity

### Expected Result

The program should successfully:

Calculate the budget distribution.
Calculate the daily budget.
Generate activities for each travel day.
Display appropriate travel advice.
Display the final message:
YOUR TRIP IS READY!


## Future Improvements

The project can be improved by adding:

1. Real-time hotel and flight prices.
2. Weather information.
3. Google Maps integration.
4. Actual tourist destinations based on location.
5. Distance and transportation cost calculation.
6. Hotel and restaurant recommendations.
7. Saving the generated itinerary to a file.
8. A graphical user interface (GUI).

