# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 14:08:54 2023

@author: C_Gab
"""

import sqlite3
import matplotlib.pyplot as plt
import numpy as np
#%% rentabilidad productos
'''
En este ejercicio lo que voy a hacer es calcular de la base 
de datos de Nortwhind calcular la rentabilidad , calculando
las ganancias totales de ventas del mismo
hare una query, y usare la función de pandas para que la lea
'''

conn=sqlite3.connect('northwind.db')
query='''
    SELECT ProductName, SUM(Price*Quantity) ganancia 
    FROM OrderDetails od
    JOIN Products p ON p.ProductID=od.ProductID
    GROUP BY od.ProductID
    ORDER BY ganancia DESC
    LIMIT 10
'''

top_productos=pd.read_sql_query(query,conn)
plt.bar(top_productos['ProductName'],top_productos['ganancia'])
plt.xticks(rotation=90)
plt.xlabel('Nombre producto')
plt.yabel('Ganancia')
#%% rentabilidad empleados
'''
En este ejercicio lo que voy a hacer es calcular de la base 
de datos de Nortwhind calcular la eficiencia de un empleado, calculando
la cantidad de productos que vendio cada uno
hare una query, y usare la función de pandas para que la lea
'''


query2='''
    SELECT FirstName || " "|| LastName as empleado, COUNT(*) as n_ventas
    FROM Orders o
    JOIN Employees e ON e.EmployeeID=o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY n_ventas DESC
    LIMIT 10
'''
top_empleados=pd.read_sql_query(query2,conn)
plt.bar(top_empleados['empleado'],top_empleados['n_ventas'])
plt.xticks(rotation=90)
plt.xlabel('Nombre empleado')
plt.yabel('n_ventas')

#%% total recaudacion por empleado

query3='''
    SELECT FirstName || " "|| LastName as empleado ,sum (price*Quantity )as recaudacion 
    FROM Orders o
    join Employees e on e.EmployeeID=o.EmployeeID
    join OrderDetails od on od.OrderID=o.OrderID 
    join  Products p on p.ProductID=od.ProductID
    Group by o.EmployeeID
    order by recaudacion DESC
    LIMIT 5
'''
recaudacion=pd.read_sql_query(query3,conn)
