import pandas as pd

# read excel sheet
df = pd.read_excel(r'/Users/ryanmelink/Downloads/database.xlsx')

# define & create input for user email address
user = input("school email: ")

# drop classes that user is not enrolled in
df = df.loc[:, (df == user).any()]


# Organize students by frequency of occurrence in descending order. Include classes.
output_df = (
    df.melt(var_name='class name', value_name='student name')
    .groupby('student name', as_index=False)
    .agg(class_count=('class name', 'count'), classes=('class name', tuple))
    .sort_values('class_count', ascending=False, ignore_index=True)
)

# delete user row as we don't want to match user with user
output_df = output_df.loc[output_df["student name"] != user]

# print top 5 results
print(output_df.head())
