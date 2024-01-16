import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
movie_data = pd.read_csv('Top Rated Movie Database.csv', low_memory=False)

# Set up Streamlit page
st.title("Top Rated Movies Dashboard")

# Plot: Average Vote by Year
avg_vote_by_year = movie_data.groupby('year')['Vote Average'].mean().reset_index()
fig1 = px.bar(avg_vote_by_year, x='year', y='Vote Average', 
              title='Average Vote by Year', color='Vote Average')

# Plot: Popularity Distribution
fig2 = px.histogram(movie_data, x='Popularity', title='Popularity Distribution')

# Plot: Vote Count by Year
vote_count_by_year = movie_data.groupby('year')['Vote Count'].sum().reset_index()
fig3 = px.line(vote_count_by_year, x='year', y='Vote Count', 
               title='Vote Count by Year')

# Plot: Trend Analysis of Popularity Over Years
trend_popularity = movie_data.groupby('year')['Popularity'].mean().reset_index()
fig4 = px.line(trend_popularity, x='year', y='Popularity', 
               title='Trend of Popularity Over Years')

# Plot: Movies Distribution by Year (Pie Chart)
movies_distribution = movie_data['year'].value_counts().reset_index()
movies_distribution.columns = ['year', 'Number of Movies']
fig5 = px.pie(movies_distribution, names='year', values='Number of Movies', 
              title='Movies Distribution by Year')

# Plot: Box Plot for Vote Averages
fig6 = px.box(movie_data, x='year', y='Vote Average', 
              title='Vote Averages by Year')

# Plot: Scatter Plot for Vote Count vs. Popularity
fig7 = px.scatter(movie_data, x='Vote Count', y='Popularity', color='year', 
                  title='Vote Count vs. Popularity')

# Layout for side-by-side graphs
col1, col2 = st.columns(2)
col1.plotly_chart(fig1)
col2.plotly_chart(fig2)

col1, col2 = st.columns(2)
col1.plotly_chart(fig3)
col2.plotly_chart(fig4)

col1, col2 = st.columns(2)
col1.plotly_chart(fig5)
col2.plotly_chart(fig6)

st.plotly_chart(fig7)
