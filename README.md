# Social Media Analytics Dashboard

## 📊 Overview
The Social Media Analytics Dashboard is an interactive Streamlit application designed to provide comprehensive analysis and visualization of social media data. It enables users to explore trends, compare platform performance, and gain actionable insights from posts across TikTok, Instagram, Twitter, and YouTube.

---

## 🚀 Features

- **Interactive Filters:**  
  Filter data by platform, content type, and date range using the sidebar for real-time analysis.
- **Key Performance Indicators (KPIs):**  
  View total posts, total views, and average engagement rate for selected filters.
- **Dynamic Visualizations:**  
  - Bar charts for platform and content type engagement  
  - Time series analysis of engagement trends  
  - Scatter plots for correlation analysis  
  - Histograms for engagement rate distribution
- **Comprehensive Analytics:**  
  - Platform performance comparison  
  - Top content types by engagement  
  - Statistical summary tables  
  - Top performing posts
- **Data Flow Explanation:**  
  Step-by-step overview of the data processing pipeline.

---

## 🗂️ Project Structure

- `app.py`: Main Streamlit dashboard application.
- `Viral_Social_Media_Trends.csv`: Source data file containing social media post metrics.

---

## 📦 Dependencies

- Python **3.9** or **3.10** (recommended)
- `streamlit`
- `pandas`
- `matplotlib`
- `seaborn`
- `numpy`

**Install with pip:**
```bash
pip install streamlit pandas matplotlib seaborn numpy
```

---

## 📁 Data Requirements

The CSV file (`Viral_Social_Media_Trends.csv`) should contain the following columns:

- `Platform` (e.g., TikTok, Instagram, Twitter, YouTube)
- `Content_Type` (e.g., video, image, story)
- `Post_Date` (date of post)
- `Views`
- `Likes`
- `Shares`
- `Comments`

---

## 🏗️ How It Works

1. **Data Loading & Preprocessing**
   - Loads CSV data using pandas.
   - Converts `Post_Date` to datetime format.
   - Calculates:
     - **Engagement:** `Likes + Shares + Comments`
     - **Engagement Rate:** `(Engagement / Views) * 100`

2. **Interactive Dashboard**
   - **Sidebar Filters:** Select platforms, content types, and date range.
   - **KPIs:** Total posts, total views, average engagement rate.
   - **Visualizations:** Bar charts, time series, scatter plots, histograms.

3. **Analytics & Charts**
   - **Platform Performance:** Total views and average engagement rate by platform.
   - **Content Type Analysis:** Top content types by engagement.
   - **Summary Tables:** Descriptive statistics, platform comparison, top posts.

4. **Error Handling**
   - Displays user-friendly error messages if the CSV file is missing or invalid.

---

## 📊 Data Flow Pipeline

- **Data Input:**
  - Source: CSV file
  - Metrics: Views, Likes, Shares, Comments, Post Dates

- **Data Loading & Validation:**
  - Load CSV, validate structure, handle missing values

- **Data Transformation:**
  - Feature engineering (date conversion, engagement metrics)

- **Interactive Interface:**
  - Streamlit dashboard with dynamic filters and real-time updates

- **Data Output:**
  - Visual analytics, summary tables, trend analysis

---

## 🖥️ Running the Dashboard

1. Place `Viral_Social_Media_Trends.csv` in the project folder.
2. Install dependencies (see above).
3. Run the app:
   ```bash
   streamlit run app.py
   ```
4. Open the provided local URL in your browser to interact with the dashboard.

---

## 📚 Customization

- **Add new platforms/content types:**  
  Update the CSV file with additional categories.
- **Modify visualizations:**  
  Edit `app.py` to add or change charts and metrics.