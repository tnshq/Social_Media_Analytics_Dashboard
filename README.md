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
## Screenshots

<img width="1449" height="753" alt="Screenshot 2025-08-27 at 7 04 56 PM" src="https://github.com/user-attachments/assets/a8d3ca5b-af84-48b6-9bc2-74fba9f25ba7" />
<img width="1340" height="672" alt="Screenshot 2025-08-27 at 7 05 38 PM" src="https://github.com/user-attachments/assets/e2defcf1-31f8-4e43-9964-549c30b93f81" />
<img width="1379" height="819" alt="Screenshot 2025-08-27 at 7 05 50 PM" src="https://github.com/user-attachments/assets/171cee58-d551-44b0-a90e-6a7512d3dd59" />
<img width="1356" height="610" alt="Screenshot 2025-08-27 at 7 05 57 PM" src="https://github.com/user-attachments/assets/f6379867-447a-43f8-b685-85abf541ecb7" />
<img width="1349" height="301" alt="Screenshot 2025-08-27 at 7 06 16 PM" src="https://github.com/user-attachments/assets/bada8251-8006-41ab-b830-e5b1bed0342e" />

