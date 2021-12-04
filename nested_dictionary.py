# Store the indian world cup ssquad data for 2021. You should be able to declare the stats of any player from the data

import pandas as pd


# def my_squad():
squad = {'Bats-man': {'Rohit Sharma': {'Matches': 207,
                                           'Runs': 10110,
                                           'Average': 47.4,
                                           'Highest Score': 546},
                          'Virat Kohli': {'Matches': 210,
                                          'Runs': 12145,
                                          'Average': 57,
                                          'Highest Score': 656},
                          'Shikar Dhawan': {'Matches': 200,
                                            'Runs': 1012,
                                            'Average': 33.5,
                                            'Highest Score': 365}},
             'Bowlers': {'Jaspreet Bumrah': {'Matches': 55,
                                             'Wickets': 50,
                                             'Average': 44,
                                             'Best': 20 / 55},
                         'Bhumneshwar Kumar': {'Matches': 60,
                                               'Wickets': 39,
                                               'Average': 22,
                                               'Best': 30 / 60},
                         'Yuzi Cahal': {'Matches': 76,
                                        'Wicket': 55,
                                        'Average': 30},
                         'Best': 55 / 76},
             'All Rounder': {'Kedar Jadhav': {'Matches': 80,
                                              'Run': 113,
                                              'Average': 22.2,
                                              'Wicket': 30},
                             'Ravindra Jadeja': {'Matches': 110,
                                                 'Run': 105,
                                                 'Wicket': 20,
                                                 'Average': 33},
                             'Hardik Pandeya': {'Matches': 205,
                                                'Run': 112,
                                                'Wicket': 50,
                                                'Average': 45}},
             'Wicket Keeper': {'M.S.Dhoni': {'Matches': 450,
                                             'Run': 220,
                                             'Average': 110,
                                             'Higest Score': 225},
                               'Dinesh Kartik': {'Matches': 310,
                                                 'Run': 110,
                                                 'Average': 55.6,
                                                 'Highest Score': 362}}

             }
df1 = pd.DataFrame(squad['Bats-man']['Rohit Sharma'], index=[1])
df2 = pd.DataFrame(squad['Bowlers']['Jaspreet Bumrah'], index=[1])
df3 = pd.DataFrame(squad['All Rounder']['Kedar Jadhav'], index=[1])
df4 = pd.DataFrame(squad['Wicket Keeper']['M.S.Dhoni'], index=[1])
df = pd.DataFrame(squad['Bats-man'])
dfb = pd.DataFrame(squad['Bowlers'])
dfw = pd.DataFrame(squad['Wicket Keeper'])
dfa = pd.DataFrame(squad['All Rounder'])

print("\n")
print("The Best batesmen are : \n")
print(df, "\n")
print("The Best Bowlers are : \n")
print(dfb, "\n")
print("Best WicketKippers are : \n")
print(dfw, "\n")
print("The Best All Rounders are : \n")
print(dfa, "\n")







