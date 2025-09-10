# 🐼 Pandas Exploratory Data Analysis (EDA)

## 📌 Overview  
This project is part of my **mlcourse.ai journey** and focuses on **Exploratory Data Analysis (EDA)** with **Pandas**, one of the most essential libraries in a data scientist’s toolkit.  

While machine learning often gets the spotlight, **70–80% of real-world data science work** is data preparation and exploration. Here I demonstrate how to clean, transform, and analyze tabular data, along with first attempts at predictive insights using **customer churn data**.  

The datasets used in this project were obtained from **[Kaggle](https://www.kaggle.com/)**.  

---

## 🛠️ Key Steps & Methods

### 1. Preliminary Data Analysis with Pandas  
- Loading and inspecting data (`.shape`, `.info()`, `.columns`)  
- Descriptive statistics with `describe()` (for numeric & categorical features)  
- Type conversion (`astype`), missing values check, and encoding categorical variables  
- Boolean indexing and conditional filtering  
- Sorting, grouping, pivot tables, and summary statistics  

### 2. Customer Churn Case Study (Telecom Dataset)  
- Distribution of churn vs. loyal customers (`value_counts`, `crosstab`)  
- Feature impact exploration:  
  - 📞 **Customer Service Calls** – higher calls correlate with higher churn  
  - 🌍 **International Plan** – customers with this plan churn significantly more  
  - Combined effect: Customers with both high service calls and international plan churn ~68% of the time  

### 3. Data Transformations  
- Adding derived features (`Total calls`, `Total charges`)  
- Dropping unnecessary rows/columns with `drop()`  
- Creating binary flags (e.g., *Many_service_calls > 3*)  

### 4. Visualization & Insights  
- **Matplotlib & Seaborn** for statistical visualization  
- **Plotly** for interactive plots  
- Visuals include:  
  - Count plots of churn vs. features  
  - Boxplots of critic scores across platforms  
  - Heatmaps of sales by platform/genre  
  - Interactive line & bar charts (Plotly)  

---

## 📂 Project Structure  

```bash
pandas-EDA/
│── topic1_pandas_titanic_practice.ipynb         # Practice with Titanic dataset
│── topic1_pandas_data_analysis.ipynb            # Telecom churn dataset analysis
│── topic2_additional_seaborn_matplotlib_plotly.ipynb  # Advanced visualizations
│── README.md                                    # Project documentation

