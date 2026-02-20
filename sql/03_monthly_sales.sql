USE RetailAnalytics;
GO

SELECT
    YEAR(Order_Date) AS [Year],
    MONTH(Order_Date) AS [Month],
    FORMAT(Order_Date, 'yyyy-MM') AS YearMonth,
    SUM(Sales) AS Total_Sales
FROM dbo.retail_sales_for_sql
GROUP BY YEAR(Order_Date), MONTH(Order_Date), FORMAT(Order_Date, 'yyyy-MM')
ORDER BY [Year], [Month];
GO