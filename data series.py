import pandas as pd
import numpy as np

#               (    Data series                )


            # Series is a one-dimensional labeled array in Python that can hold data of any type
            # (integers, floats, strings, or Python objects), 
            # much like a single column in a spreadsheet or a database table.




# Creating a simple Series from a list
data = [10, 20, 30, 40]
s = pd.Series(data, index=['a', 'b', 'c', 'd'])

print(s)



# ==============================================

#               (How to Access Data)


#       (Iloc)
# • By Position (.iloc): Use integer locations like a regular list (s.iloc[0] returns 10).

#        ( LOC)
# • By Label (.loc): Use the custom index name (s.loc['b'] returns 20).




# Creating a simple Series from a list
data = [20, 40, 60, 80]
loc_and_iloc= pd.Series(data, index=['a', 'b', 'c', 'd'])

# 1. Using .loc (Looks up by the LABEL name)
print(s.loc['b'])   # Output: 20
print(s.loc['d'])   # Output: 40

# 2. Using .iloc (Looks up by the INDEX POSITION / integer, starting at 0)
print(s.iloc[1])    # Output: 20 (position 1 is 'b')
print(s.iloc[-1])   # Output: 40 (negative indexing works too, getting the last item)





