import numpy as np, pandas as pd
from fuzzywuzzy import fuzz

def name_similarity_array(input_name, source_array):
    
    results = []
    source_array = source_array.drop_duplicates() #removing unneccessary duplicates
    
    i = 0
    while i < len(source_array):
        test1 = fuzz.partial_ratio(input_name, source_array.loc[i][0]) #similarity across independent words
        test2 = fuzz.token_sort_ratio(input_name, source_array.loc[i][0]) #alphabetical sorting to account for different orders of names e.g. John Doe and Doe, John
        test3 = fuzz.token_set_ratio(input_name, source_array.loc[i][0]) #breaking down strings where

        if (test1 == 100 or test2 == 100 or test3 == 100): results.append(100)
        else: results.append((test1 + test2 + test3)/3)
        
        i += 1
    
    return np.mean(results)