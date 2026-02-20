-- Create database (run once in SQL Server)
CREATE DATABASE RetailAnalytics;
GO

USE RetailAnalytics;
GO

-- Main retail sales fact table
CREATE TABLE dbo.retail_sales_for_sql (
    Row_ID        INT             NOT NULL,
    Order_ID      NVARCHAR(50)    NOT NULL,
    Order_Date    DATE            NOT NULL,
    Ship_Date     DATE            NOT NULL,
    Ship_Mode     NVARCHAR(50)    NULL,
    Customer_ID   NVARCHAR(50)    NOT NULL,
    Customer_Name NVARCHAR(255)   NULL,
    Segment       NVARCHAR(50)    NULL,
    Country       NVARCHAR(100)   NULL,
    City          NVARCHAR(100)   NULL,
    State         NVARCHAR(100)   NULL,
    Postal_Code   INT             NULL,
    Region        NVARCHAR(50)    NULL,
    Product_ID    NVARCHAR(50)    NOT NULL,
    Category      NVARCHAR(50)    NULL,
    Sub_Category  NVARCHAR(50)    NULL,
    Product_Name  NVARCHAR(255)   NULL,
    Sales         DECIMAL(18,4)   NOT NULL
);