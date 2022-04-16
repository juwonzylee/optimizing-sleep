# Project 3: Optimizing Sleep
College students are constantly sleep-deprived. Deadlines after deadlines, students compromise on sleep. For this project, I optimize my weekly sleep time using linear programming.

## Data Collection
Based on data obtained from the 'Health' app in my phone, I collected the [average sleep](./sleep_data.xlsx) in the past four months.
The scope has been decided for one semester as other semesters have different schedules and it would be hard to average sleep time.

Taking the weekly average sleep time of 13 weeks, I derived that my weekly average sleep is 6 hours and 16 minutes. 
The average daily sleep for the days are as follows:

H:M | Mon | Tues | Wed | Thurs | Fri | Sat | Sun
-- | -- | -- | -- | -- | -- | -- | --
Average Sleep time | 7:13 | 6:54| 7:04 | 7:02 | 7:05| 6:50 | 7:02

Really, not that interesting. This is because there were factors that influenced the regularity of sleep this semester that did not allow for an interesting average to tell a story about the sleep cycle. 

## Formulation of the LP
The objective function is to maximize weekly sleep time based on the decision variables are the sleep time of Monday through Sunday. 
```(python)
Max z = x1 + x2 + x3 + x4 + x5 + x6 + x7
```
The cost functions are derived from the data collected.
```(python)
x1 >= 7

```