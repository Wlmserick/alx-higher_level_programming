# SQL Queries Overview

## Introduction

This README provides an overview of common SQL queries for managing and manipulating data in a relational database management system (RDBMS).

## Basic SQL Queries

### 1. SELECT Statement

The `SELECT` statement retrieves data from one or more tables.

```sql
SELECT column1, column2 FROM table_name;
```

### 2. INSERT Statement

The `INSERT` statement adds new records to a table.

```sql
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```

### 3. UPDATE Statement

The `UPDATE` statement modifies existing records in a table.

```sql
UPDATE table_name SET column1 = value1 WHERE condition;
```

### 4. DELETE Statement

The `DELETE` statement removes records from a table.

```sql
DELETE FROM table_name WHERE condition;
```

## Advanced SQL Queries

### 1. JOIN Statement

The `JOIN` statement is used to combine rows from two or more tables based on a related column between them.

```sql
SELECT * FROM table1
JOIN table2 ON table1.column_name = table2.column_name;
```

### 2. GROUP BY Statement

The `GROUP BY` statement groups rows that have the same values into summary rows.

```sql
SELECT column1, COUNT(*)
FROM table_name
GROUP BY column1;
```

### 3. ORDER BY Statement

The `ORDER BY` statement sorts the result set in ascending or descending order.

```sql
SELECT * FROM table_name
ORDER BY column1 ASC;
```

### 4. WHERE Clause

The `WHERE` clause filters records based on specified conditions.

```sql
SELECT * FROM table_name
WHERE condition;
```

### 5. DISTINCT Keyword

The `DISTINCT` keyword is used to return unique values in a specified column.

```sql
SELECT DISTINCT column1 FROM table_name;
```

### 6. LIKE Operator

The `LIKE` operator is used in a `WHERE` clause to search for a specified pattern in a column.

```sql
SELECT * FROM table_name
WHERE column1 LIKE 'pattern%';
```

### 7. LIMIT Clause

The `LIMIT` clause is used to limit the number of rows returned in a result set.

```sql
SELECT * FROM table_name
LIMIT 10;
```

## Additional Resources

- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [SQLZoo](https://sqlzoo.net/): Interactive SQL Tutorial
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

