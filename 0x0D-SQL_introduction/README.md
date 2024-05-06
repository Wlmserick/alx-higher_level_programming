# SQL Introduction

## What is SQL?

SQL (Structured Query Language) is a standard programming language used to manage and manipulate relational databases. It allows users to query and manipulate data stored in a relational database management system (RDBMS).

## Why use SQL?

- **Data Retrieval**: SQL allows users to retrieve specific data from a database using queries.
- **Data Manipulation**: It enables users to add, delete, and modify data in the database.
- **Data Definition**: SQL can define the structure and schema of a database, including tables, indexes, and constraints.
- **Data Control**: SQL provides control over user access to the database through permissions and security features.

## Basic SQL Commands:

1. **SELECT**: Retrieves data from one or more tables.
   ```sql
   SELECT column1, column2 FROM table_name;
   ```

2. **INSERT**: Adds new records to a table.
   ```sql
   INSERT INTO table_name (column1, column2) VALUES (value1, value2);
   ```

3. **UPDATE**: Modifies existing records in a table.
   ```sql
   UPDATE table_name SET column1 = value1 WHERE condition;
   ```

4. **DELETE**: Removes records from a table.
   ```sql
   DELETE FROM table_name WHERE condition;
   ```

5. **CREATE TABLE**: Creates a new table in the database.
   ```sql
   CREATE TABLE table_name (
       column1 datatype,
       column2 datatype,
       ...
   );
   ```

6. **ALTER TABLE**: Modifies an existing table structure.
   ```sql
   ALTER TABLE table_name ADD column_name datatype;
   ```

7. **DROP TABLE**: Deletes an existing table from the database.
   ```sql
   DROP TABLE table_name;
   ```

## Getting Started

To start using SQL, you'll need access to a relational database management system (RDBMS) such as MySQL, PostgreSQL, SQLite, or Microsoft SQL Server. Install the RDBMS of your choice and use its command-line interface or a graphical user interface (GUI) tool to interact with the database using SQL queries.

## Resources

- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [SQLZoo](https://sqlzoo.net/): Interactive SQL Tutorial
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

