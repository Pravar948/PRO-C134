1. Import pandas and matplotlib module
2. Import the star_with_gravity.csv as dataframe
3. Filter out the stars with distance less than or equal to 100 light years
4. Make a new DataFrame for filtered starts
5. Filter out the stars having gravity in range of 150 to 350
6. Add these stars to the new DataFrame
7. Create a new csv file as filtered_starts.csv from the DataFrame and download it 



import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('star_with_gravity.csv')
filtered_df = df[df['Distance'] <= 100]
filtered_df = filtered_df[(filtered_df['Gravity'] >= 150) & (filtered_df['Gravity'] <= 350)]
filtered_df.to_csv('filtered_starts.csv', index=False)
print(filtered_df)
