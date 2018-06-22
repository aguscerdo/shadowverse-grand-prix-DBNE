import pandas as pd
from tools import *



def analyze(df):
    # ---- Single column distributions -----
    rank_count = count_col(df, "Rank")
    class_count = count_col(df, "Class")


    # Rank Statistics
    rank_class = count_col(df, ['Rank', 'Class'])
    rank_wins = count_col(df, ['Rank', 'Wins'])

    # Class Statistics
    class_archetype = count_col(df, ['Class', 'Archetype'])



