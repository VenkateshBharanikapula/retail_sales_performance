# Retail Sales Performance Analysis

This is a personal end-to-end analytics project built to demonstrate practical skills in **Python**, **SQL**, **Excel**, and **Power BI** using 4 years of retail transaction data.  
The goal is to analyze sales performance, identify trends and seasonality, and deliver an executive-ready KPI dashboard.

---

## 1. Business Objective

The objective of this project is to answer key business questions such as:

- How are **sales evolving over time** (monthly trend, seasonality)?
- Which **categories, sub-categories, and products** generate the most revenue?
- Which **regions and customer segments** are the strongest performers?
- How can we monitor performance using **MoM (Month-over-Month)** and **YoY (Year-over-Year)** growth KPIs?
- How can we deliver these insights in a **reusable, interactive dashboard** for decision-makers?

---

## 2. Dataset Overview

- **Source**: Public “Superstore / Retail Sales”–style dataset (CSV)
- **Rows**: ~9,800
- **Columns**: 18

**Key fields used:**

- **Date & Shipping**
  - `Order Date`, `Ship Date`
- **Customer**
  - `Customer ID`, `Customer Name`, `Segment`
  - `Country`, `City`, `State`, `Region`, `Postal Code`
- **Product**
  - `Category`, `Sub-Category`, `Product Name`, `Product ID`
- **Metrics**
  - `Sales` (main revenue metric)
  - `Row ID`, `Order ID` (identifiers)

---

## 3. Tech Stack

- **Python**
  - `pandas` – data loading, cleaning, aggregations
  - `matplotlib` – trend and distribution visualizations
- **SQL (SQL Server)**
  - `RetailAnalytics` database
  - Table: `dbo.retail_sales_for_sql`
- **Excel**
  - KPI modeling: MoM and YoY growth calculations
- **Power BI**
  - Interactive dashboard with KPIs and drill-downs

---

## 4. Project Structure

```text
retail_sales_performance/
│
├── data/
│   ├── data_raw/                 # original dataset (CSV)
│   └── data_processed/           # cleaned / transformed CSVs
│
├── notebooks/                    # Python scripts for cleaning & EDA
│   ├── 01_data_load_and_quality_check.py
│   ├── 02_prepare_dates.py
│   ├── 03_monthly_sales_trend.py
│   ├── 04_category_region_performance.py
│   ├── 05_customer_segment_performance.py
│   ├── 06_product_performance.py
│   ├── 07_export_kpi_sources.py
│   └── 08_export_for_sql.py
│
├── sql/                          # SQL DDL + analysis queries
│   ├── 01_create_table.sql       # CREATE DATABASE + CREATE TABLE
│   ├── 02_check_table.sql        # basic sanity check
│   └── 03_monthly_sales.sql      # monthly sales aggregation
│
├── excel/
│   └── Retail_KPI_Model.xlsx     # KPI model (MoM / YoY)
│
├── powerbi/
│   └── Retail_Sales_Dashboard.pbix   # interactive report
│
└── docs/
    └── README.md                 # this documentation 
