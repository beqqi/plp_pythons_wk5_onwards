# Part 1: Imports and Data Loading
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    df = pd.read_csv('metadata.csv')
except FileNotFoundError:
    st.error("Error: 'metadata.csv' not found. Please make sure the file is in the same directory as the script.")
    st.stop()

# Part 2: Data Cleaning and Preparation
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

# Handle missing data by dropping rows with no title, abstract, or journal
df.dropna(subset=['title', 'abstract', 'journal'], inplace=True)

# Part 3: Data Analysis and Visualization
# Plot 1: Publications by Year
year_counts = df['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax1, palette='viridis')
ax1.set_title('Number of Publications by Year', fontsize=16)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Papers', fontsize=12)
ax1.grid(axis='y', linestyle='--')
plt.xticks(rotation=45)
plt.tight_layout()

# Plot 2: Top 10 Publishing Journals
top_journals = df['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots(figsize=(12, 8))
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax2, palette='magma')
ax2.set_title('Top 10 Publishing Journals', fontsize=16)
ax2.set_xlabel('Number of Papers', fontsize=12)
ax2.set_ylabel('Journal', fontsize=12)
plt.tight_layout()

# Part 4: Streamlit Application
st.title("CORD-19 Data Explorer")
st.write("A simplified analysis of the COVID-19 research dataset.")
st.write("---")

# Display plots
st.header("Publications Over Time")
st.pyplot(fig1)

st.header("Top Publishing Journals")
st.pyplot(fig2)

# Display a sample of the data
st.header("Sample Data")
st.write("Here is a random sample of 5 papers from the dataset:")
st.dataframe(df[['title', 'journal', 'publish_time']].sample(5))

# Part 5: Documentation and Reflection
st.markdown("---")
st.markdown("""
### Project Findings and Reflection

**Findings:**
- The analysis shows a significant surge in COVID-19 related publications in the years **2020** and **2021**.
- The top journals identified are key sources of research in this field.

**Reflection:**
This project provided a practical introduction to the data science workflow, including data cleaning, basic analysis, and visualization. The biggest challenges were handling missing data and preparing the dataset for plotting. Streamlit proved to be a powerful tool for quickly presenting these findings in an interactive format.
""")