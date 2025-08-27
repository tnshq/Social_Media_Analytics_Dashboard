import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

# --- Page Configuration ---
st.set_page_config(
    page_title="Social Media Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# --- Title and Description ---
st.title("📊 Social Media Analytics Dashboard")
st.markdown("""
This dashboard provides comprehensive analysis of social media data with interactive visualizations and detailed insights.
""")

# Define the path to your CSV file
csv_file_path = '/Users/tanishqsohal/streamlitproject/Viral_Social_Media_Trends.csv'

# --- Load Data and Preprocessing ---
try:
    # Load the CSV file
    df = pd.read_csv(csv_file_path)
    
    # Convert date column to proper datetime format
    df['Post_Date'] = pd.to_datetime(df['Post_Date'])
    
    # Calculate new metrics
    df['Engagement'] = df['Likes'] + df['Shares'] + df['Comments']
    df['Engagement_Rate'] = (df['Engagement'] / df['Views']).fillna(0) * 100

    # --- Create Tabs for Different Sections ---
    tab1, tab2 = st.tabs(["📊 Interactive Dashboard", "📈 Analytics & Charts"])

    with tab1:
        st.header("Live Analysis Dashboard")
        
        # Explanation box
        st.info("""
        🎛️ **How to Use the Interactive Filters**
        
        The **sidebar on the left** contains dynamic filters that allow you to customize your data analysis in real-time:
        
        • **Platform Filter:** Select specific social media platforms (TikTok, Instagram, Twitter, YouTube) to analyze
        • **Content Type Filter:** Choose particular content types (videos, images, stories, etc.) to focus your analysis
        • **Date Range Filter:** Pick a specific time period to examine trends within that timeframe
        
        When you change these filters, all charts and metrics below will automatically update to reflect your selection!
        """)
        
        # --- Sidebar Filters ---
        st.sidebar.header("Dashboard Filters")
        st.sidebar.markdown("Use these controls to filter the data dynamically:")
        
        # Platform filter
        platforms = st.sidebar.multiselect(
            "🔍 Filter by Platform:",
            options=df['Platform'].unique(),
            default=df['Platform'].unique(),
            help="Select one or more social media platforms to analyze"
        )
        
        # Content type filter
        content_types = st.sidebar.multiselect(
            "📄 Filter by Content Type:",
            options=df['Content_Type'].unique(),
            default=df['Content_Type'].unique(),
            help="Choose specific content types to focus your analysis"
        )
        
        # Date range filter
        min_date = df['Post_Date'].min().date()
        max_date = df['Post_Date'].max().date()
        date_range = st.sidebar.date_input(
            "📅 Filter by Date Range:",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
            help="Select the time period for your analysis"
        )

        # --- Apply Filters to Data ---
        start_date = datetime.combine(date_range[0], datetime.min.time())
        end_date = datetime.combine(date_range[1], datetime.max.time())
        
        filtered_df = df[
            (df['Platform'].isin(platforms)) &
            (df['Content_Type'].isin(content_types)) &
            (df['Post_Date'] >= start_date) &
            (df['Post_Date'] <= end_date)
        ]

        if filtered_df.empty:
            st.warning("No data found for the selected filters. Please adjust your filter criteria.")
        else:
            # --- Key Performance Indicators ---
            st.subheader("📊 Key Performance Indicators")
            
            # Calculate metrics
            total_posts = filtered_df.shape[0]
            total_views = int(filtered_df['Views'].sum())
            avg_engagement_rate = filtered_df['Engagement_Rate'].mean()
            
            # Display metrics in columns
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Posts", f"{total_posts:,}")
            col2.metric("Total Views", f"{total_views:,}")
            col3.metric("Avg. Engagement Rate", f"{avg_engagement_rate:.2f}%")

            st.divider()
            
            # --- Data Visualizations ---
            st.subheader("📈 Data Visualizations with Analysis")
            
            # Theory explanation for bar charts
            st.info("""
            **📊 Bar Chart Analysis Theory**
            
            **Purpose:** Bar charts are ideal for comparing categorical data across different groups. They show the magnitude of values for each category, making it easy to identify which platforms or content types perform best.
            
            **What to Look For:** The height of each bar represents the total value. Compare bar heights to understand relative performance between categories.
            """)
            
            # --- Row 1: Bar Charts ---
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Total Engagement by Platform**")
                platform_engagement = filtered_df.groupby('Platform')['Engagement'].sum().sort_values(ascending=False)
                
                fig1, ax1 = plt.subplots(figsize=(10, 6))
                colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
                bars = ax1.bar(platform_engagement.index, platform_engagement.values, 
                              color=colors[:len(platform_engagement)])
                
                ax1.set_xlabel("Platform")
                ax1.set_ylabel("Total Engagement")
                ax1.set_title("Total Engagement by Social Media Platform")
                ax1.grid(axis='y', alpha=0.3)
                
                # Add value labels on bars
                for bar in bars:
                    height = bar.get_height()
                    ax1.text(bar.get_x() + bar.get_width()/2., height,
                            f'{int(height):,}', ha='center', va='bottom')
                
                plt.xticks(rotation=45)
                plt.tight_layout()
                st.pyplot(fig1)

            with col2:
                st.markdown("**Top Content Types by Performance**")
                content_engagement = filtered_df.groupby('Content_Type')['Engagement'].sum().nlargest(8)
                
                fig2, ax2 = plt.subplots(figsize=(10, 6))
                bars = ax2.barh(content_engagement.index, content_engagement.values, color='skyblue')
                ax2.set_xlabel("Total Engagement")
                ax2.set_ylabel("Content Type")
                ax2.set_title("Top Content Types by Engagement")
                ax2.grid(axis='x', alpha=0.3)
                
                # Add value labels
                for bar in bars:
                    width = bar.get_width()
                    ax2.text(width, bar.get_y() + bar.get_height()/2.,
                            f'{int(width):,}', ha='left', va='center')
                
                plt.tight_layout()
                st.pyplot(fig2)

            # Theory for time series
            st.info("""
            **📈 Time Series Analysis Theory**
            
            **Purpose:** Time series charts show how data changes over time, revealing trends, patterns, and seasonal variations. The line plot with filled area helps visualize the magnitude of change.
            
            **What to Look For:** Upward/downward trends, periodic patterns, sudden spikes or drops, and overall trajectory of engagement over time.
            """)

            # --- Row 2: Time Series Chart ---
            st.markdown("**Engagement Trends Over Time**")
            monthly_data = filtered_df.set_index('Post_Date').resample('M')['Engagement'].sum()
            
            fig3, ax3 = plt.subplots(figsize=(12, 6))
            ax3.plot(monthly_data.index, monthly_data.values, marker='o', linewidth=2, markersize=6)
            ax3.fill_between(monthly_data.index, monthly_data.values, alpha=0.3)
            ax3.set_xlabel("Date")
            ax3.set_ylabel("Monthly Total Engagement")
            ax3.set_title("Engagement Trend Analysis Over Time")
            ax3.grid(True, alpha=0.3)
            
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig3)

            # Theory for advanced analytics
            st.info("""
            **🔬 Advanced Analytics Theory**
            
            **Scatter Plot:** Shows correlation between two continuous variables. Each point represents one data point. Clustering patterns reveal relationships.
            
            **Histogram:** Shows the distribution of a single variable. The shape reveals if data is normally distributed, skewed, or has multiple peaks.
            """)

            # --- Row 3: Advanced Analytics ---
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Views vs Engagement Correlation**")
                fig4, ax4 = plt.subplots(figsize=(10, 6))
                
                # Create scatter plot with platform-based coloring
                platforms_unique = filtered_df['Platform'].unique()
                colors_scatter = ['blue', 'red', 'green', 'orange', 'purple']
                
                for i, platform in enumerate(platforms_unique):
                    platform_data = filtered_df[filtered_df['Platform'] == platform]
                    ax4.scatter(platform_data['Views'], platform_data['Engagement'], 
                              alpha=0.6, s=50, color=colors_scatter[i % len(colors_scatter)], 
                              label=platform)
                
                ax4.set_xlabel("Views (Log Scale)")
                ax4.set_ylabel("Engagement (Log Scale)")
                ax4.set_title("Views vs Total Engagement by Platform")
                ax4.set_xscale('log')
                ax4.set_yscale('log')
                ax4.grid(True, alpha=0.3)
                ax4.legend()
                
                plt.tight_layout()
                st.pyplot(fig4)

            with col2:
                st.markdown("**Engagement Rate Distribution**")
                fig5, ax5 = plt.subplots(figsize=(10, 6))
                
                ax5.hist(filtered_df['Engagement_Rate'], bins=30, color='lightgreen', alpha=0.7)
                mean_engagement = filtered_df['Engagement_Rate'].mean()
                ax5.axvline(mean_engagement, color='red', linestyle='--', linewidth=2,
                           label=f'Mean: {mean_engagement:.2f}%')
                ax5.set_xlabel("Engagement Rate (%)")
                ax5.set_ylabel("Frequency")
                ax5.set_title("Distribution of Engagement Rates")
                ax5.legend()
                ax5.grid(True, alpha=0.3)
                
                plt.tight_layout()
                st.pyplot(fig5)

    with tab2:
        st.header("Detailed Analytics & Charts")
        st.markdown("This section contains comprehensive charts and statistical summaries for deeper analysis of the social media data.")

        # --- Data Flow Diagram ---
        st.subheader("📊 System Data Flow")
        st.markdown("**Data Processing Pipeline Overview**")
        
        # Simple text-based data flow diagram
        st.markdown("""
        ### 🔄 Data Processing Flow
        
        **📁 Step 1: Data Input**
        - **Source:** CSV File (Viral_Social_Media_Trends.csv)
        - **Size:** 5000+ social media posts
        - **Platforms:** TikTok, Instagram, Twitter, YouTube
        - **Metrics:** Views, Likes, Shares, Comments, Post Dates
        
        ⬇️
        
        **🐍 Step 2: Data Loading & Validation**
        - **Process:** Python Processing (pandas.read_csv)
        - **Actions:** Load CSV → Validate structure → Handle missing values
        - **Output:** Clean DataFrame ready for analysis
        
        ⬇️
        
        **🔧 Step 3: Data Transformation**
        - **Feature Engineering:**
          - Convert Post_Date to datetime format
          - Calculate Engagement = Likes + Shares + Comments
          - Calculate Engagement_Rate = (Engagement/Views) × 100
          - Create platform and content categorizations
        
        ⬇️
        
        **🌐 Step 4: Interactive Interface**
        - **Streamlit Dashboard Features:**
          - Dynamic Filters (Platform, Content Type, Date Range)
          - Real-time Chart Updates
          - Key Performance Indicators (KPIs)
          - Multiple Visualization Types
        
        ⬇️
        
        **📊 Step 5: Data Output**
        - **Visual Analytics:**
          - Interactive Charts & Graphs
          - Statistical Summary Tables
          - Trend Analysis Visualizations
          - Performance Comparison Metrics
        """)
        
        st.divider()

        # --- Comprehensive Visualizations ---
        st.subheader("📈 Comprehensive Visualizations")
        
        # Platform Performance Overview
        st.markdown("**Platform Performance Overview**")
        platform_metrics = df.groupby('Platform').agg({
            'Views': 'sum',
            'Engagement': 'sum',
            'Engagement_Rate': 'mean'
        }).reset_index()
        
        fig_report1, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Chart 1: Views by Platform
        bars1 = ax1.bar(platform_metrics['Platform'], platform_metrics['Views'], 
                        color=['lightblue', 'lightcoral', 'lightgreen', 'lightyellow'])
        ax1.set_title('Total Views by Platform', fontsize=14)
        ax1.set_xlabel('Platform')
        ax1.set_ylabel('Total Views')
        ax1.grid(axis='y', alpha=0.3)
        
        for bar in bars1:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height):,}', ha='center', va='bottom')
        
        # Chart 2: Average Engagement Rate
        bars2 = ax2.bar(platform_metrics['Platform'], platform_metrics['Engagement_Rate'], 
                        color=['lightblue', 'lightcoral', 'lightgreen', 'lightyellow'])
        ax2.set_title('Average Engagement Rate by Platform', fontsize=14)
        ax2.set_xlabel('Platform')
        ax2.set_ylabel('Engagement Rate (%)')
        ax2.grid(axis='y', alpha=0.3)
        
        for bar in bars2:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%', ha='center', va='bottom')
        
        plt.tight_layout()
        st.pyplot(fig_report1)

        # Content Type Analysis
        st.markdown("**Content Type Performance Analysis**")
        content_analysis = df.groupby('Content_Type')['Engagement'].sum().nlargest(10)
        
        fig_report2, ax = plt.subplots(figsize=(12, 8))
        bars = ax.barh(content_analysis.index, content_analysis.values, color='steelblue')
        ax.set_title('Top 10 Content Types by Total Engagement', fontsize=14)
        ax.set_xlabel('Total Engagement')
        ax.set_ylabel('Content Type')
        ax.grid(axis='x', alpha=0.3)
        
        for bar in bars:
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height()/2.,
                    f'{int(width):,}', ha='left', va='center')
        
        plt.tight_layout()
        st.pyplot(fig_report2)

        st.divider()

        # --- Summary Tables ---
        st.subheader("📋 Statistical Summary Tables")
        
        st.markdown("**Overall Dataset Statistics**")
        summary_stats = df[['Views', 'Likes', 'Shares', 'Comments', 'Engagement', 'Engagement_Rate']].describe()
        st.dataframe(summary_stats.round(2), use_container_width=True)

        st.markdown("**Platform Comparison Table**")
        platform_summary = df.groupby('Platform').agg(
            Total_Posts=('Platform', 'count'),
            Total_Views=('Views', 'sum'),
            Total_Likes=('Likes', 'sum'),
            Total_Shares=('Shares', 'sum'),
            Total_Comments=('Comments', 'sum'),
            Total_Engagement=('Engagement', 'sum'),
            Average_Engagement_Rate=('Engagement_Rate', 'mean')
        ).reset_index()
        
        # Format numbers for readability
        platform_summary['Total_Views'] = platform_summary['Total_Views'].apply(lambda x: f"{x:,}")
        platform_summary['Total_Engagement'] = platform_summary['Total_Engagement'].apply(lambda x: f"{x:,}")
        platform_summary['Average_Engagement_Rate'] = platform_summary['Average_Engagement_Rate'].apply(lambda x: f"{x:.2f}%")
        
        st.dataframe(platform_summary, use_container_width=True)

        st.markdown("**Top Performing Posts**")
        top_posts = df.nlargest(10, 'Engagement')[['Platform', 'Content_Type', 'Views', 'Likes', 'Shares', 'Comments', 'Engagement']]
        st.dataframe(top_posts, use_container_width=True)

except FileNotFoundError:
    st.error(f"Error: The file '{csv_file_path}' was not found.")
    st.error("Please make sure the CSV file is in the correct location.")
except Exception as e:
    st.error(f"An error occurred while processing the file: {e}")
    st.error("Please ensure you have a valid CSV file with the required columns.")
