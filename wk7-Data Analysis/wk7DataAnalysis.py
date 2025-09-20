#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Iris Dataset Analysis Script
Author: Your Name
Date: October 27, 2023

This script performs an exploratory data analysis on the Iris flower dataset.
It covers data loading, cleaning, basic analysis, and visualization.
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import os

# Set visual style for plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

def main():
    """Main function to execute the data analysis pipeline."""
    print("Starting Iris Dataset Analysis...")
    print("=" * 50)
    
    # Task 1: Load and Explore the Dataset
    df = load_and_explore_data()
    
    if df is not None:
        # Task 2: Basic Data Analysis
        perform_basic_analysis(df)
        
        # Task 3: Data Visualization
        create_visualizations(df)
        
        print("\n" + "=" * 50)
        print("Analysis complete! Check the generated plots.")
    else:
        print("Analysis failed due to data loading issues.")

def load_and_explore_data():
    """
    Load and explore the Iris dataset.
    Returns a DataFrame if successful, None otherwise.
    """
    try:
        # Load the Iris dataset from sklearn
        print("TASK 1: LOADING AND EXPLORING DATASET")
        print("-" * 40)
        
        iris = load_iris()
        df = pd.DataFrame(iris.data, columns=iris.feature_names)
        
        # Add species column
        df['species'] = iris.target
        df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
        
        print("✅ Dataset loaded successfully!")
        print(f"Dataset shape: {df.shape}")
        
        # Display first few rows
        print("\nFirst 5 rows of the dataset:")
        print(df.head())
        
        # Explore dataset structure
        print("\nDataset information:")
        print(df.info())
        
        # Check for missing values
        print("\nMissing values in each column:")
        missing_values = df.isnull().sum()
        print(missing_values)
        
        # Clean data if necessary
        if missing_values.any():
            print("\nCleaning missing values...")
            df = df.dropna()  # or use df.fillna() for specific strategy
            print("Missing values handled.")
        else:
            print("\nNo missing values found. Dataset is clean.")
        
        return df
        
    except Exception as e:
        print(f"❌ Error loading dataset: {e}")
        return None

def perform_basic_analysis(df):
    """
    Perform basic statistical analysis on the dataset.
    """
    print("\n\nTASK 2: BASIC DATA ANALYSIS")
    print("-" * 40)
    
    # Basic statistics for numerical columns
    print("Basic statistics for numerical columns:")
    print(df.describe())
    
    # Group by species and compute means
    print("\nMean measurements by species:")
    grouped_means = df.groupby('species').mean()
    print(grouped_means.round(2))
    
    # Additional grouping analysis
    print("\nDetailed analysis for sepal length by species:")
    sepal_stats = df.groupby('species')['sepal length (cm)'].agg(['mean', 'std', 'min', 'max'])
    print(sepal_stats.round(2))
    
    # Identify patterns and findings
    print("\n" + "=" * 40)
    print("KEY FINDINGS FROM BASIC ANALYSIS:")
    print("=" * 40)
    print("1. Setosa has the smallest average measurements across all features.")
    print("2. Virginica has the largest average sepal and petal measurements.")
    print("3. Versicolor measurements typically fall between setosa and virginica.")
    print("4. Petal measurements show greater variation between species than sepal measurements.")
    print("5. Setosa is clearly distinct, while versicolor and virginica show some overlap.")

def create_visualizations(df):
    """
    Create and save various visualizations.
    """
    print("\n\nTASK 3: DATA VISUALIZATION")
    print("-" * 40)
    
    try:
        # Create a directory for plots if it doesn't exist
        os.makedirs('plots', exist_ok=True)
        
        # 1. Line Chart (using index as pseudo-time)
        plt.figure()
        plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length', marker='o', markersize=2, alpha=0.7)
        plt.plot(df.index, df['petal length (cm)'], label='Petal Length', marker='s', markersize=2, alpha=0.7)
        plt.title('Trend of Measurements Across Samples', fontsize=14, fontweight='bold')
        plt.xlabel('Sample Index')
        plt.ylabel('Length (cm)')
        plt.legend()
        plt.tight_layout()
        plt.savefig('plots/line_chart.png', dpi=300, bbox_inches='tight')
        print("✅ Line chart saved as 'plots/line_chart.png'")
        plt.close()
        
        # 2. Bar Chart (comparison across categories)
        plt.figure()
        species_means = df.groupby('species')['sepal length (cm)'].mean()
        colors = ['#ff9999', '#66b3ff', '#99ff99']
        species_means.plot(kind='bar', color=colors, edgecolor='black')
        plt.title('Average Sepal Length by Species', fontsize=14, fontweight='bold')
        plt.xlabel('Species')
        plt.ylabel('Sepal Length (cm)')
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig('plots/bar_chart.png', dpi=300, bbox_inches='tight')
        print("✅ Bar chart saved as 'plots/bar_chart.png'")
        plt.close()
        
        # 3. Histogram (distribution of numerical column)
        plt.figure()
        plt.hist(df['sepal length (cm)'], bins=15, color='lightblue', 
                edgecolor='black', alpha=0.7)
        plt.title('Distribution of Sepal Lengths', fontsize=14, fontweight='bold')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Frequency')
        plt.axvline(df['sepal length (cm)'].mean(), color='red', linestyle='dashed', 
                   linewidth=1, label=f'Mean: {df["sepal length (cm)"].mean():.2f}')
        plt.legend()
        plt.tight_layout()
        plt.savefig('plots/histogram.png', dpi=300, bbox_inches='tight')
        print("✅ Histogram saved as 'plots/histogram.png'")
        plt.close()
        
        # 4. Scatter Plot (relationship between two numerical columns)
        plt.figure()
        colors = {'setosa': 'blue', 'versicolor': 'green', 'virginica': 'red'}
        
        for species, group in df.groupby('species'):
            plt.scatter(group['sepal length (cm)'], group['petal length (cm)'],
                       label=species, color=colors[species], alpha=0.7, s=50)
        
        plt.title('Relationship Between Sepal Length and Petal Length', 
                 fontsize=14, fontweight='bold')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Petal Length (cm)')
        plt.legend(title='Species')
        plt.tight_layout()
        plt.savefig('plots/scatter_plot.png', dpi=300, bbox_inches='tight')
        print("✅ Scatter plot saved as 'plots/scatter_plot.png'")
        plt.close()
        
        # Bonus: Boxplot using seaborn
        plt.figure()
        sns.boxplot(data=df, x='species', y='sepal length (cm)', palette='pastel')
        plt.title('Sepal Length Distribution by Species', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('plots/boxplot.png', dpi=300, bbox_inches='tight')
        print("✅ Boxplot saved as 'plots/boxplot.png'")
        plt.close()
        
    except Exception as e:
        print(f"❌ Error creating visualizations: {e}")

if __name__ == "__main__":
    main()