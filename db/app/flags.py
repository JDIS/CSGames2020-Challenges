from app.helpers import compare_query_output, execute_query

level_1_data = execute_query("""
SELECT 
    p.ProductName,
    p.UnitPrice,
    c.CategoryName
FROM "Products" p
INNER JOIN Categories c USING(CategoryID)
    WHERE CategoryName = 'Condiments'
""")


level_2_data = execute_query("""
SELECT 
    e.FirstName || ' ' || e.LastName AS FullName,
    sum(od.Quantity) as QuantitySold,
    p.ProductName
FROM "Products" p
INNER JOIN "Order Details" od USING(ProductID)
INNER JOIN "Orders" o USING(OrderID)
INNER JOIN "Employees" e USING(EmployeeID)
    where e.EmployeeID = 3
GROUP BY p.ProductID
ORDER BY p.ProductID, od.OrderID
""")


level_3_data = execute_query("""
SELECT 
    c.CompanyName,
    s.CompanyName as SupplierName,
    CAST(ROUND(SUM(od.UnitPrice * od.quantity * (1 - od.discount))) as INT) || '$' as TotalSpent
FROM Customers c
INNER JOIN "Orders" o USING(CustomerID)
INNER JOIN "Order Details" od USING(OrderID)
INNER JOIN "Products" p USING(ProductID)
INNER JOIN "Suppliers" s USING(SupplierID)
GROUP BY s.SupplierID
ORDER BY c.CompanyName
""")