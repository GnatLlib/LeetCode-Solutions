LeetCode Problem 176. Second Highest Salary
Write a SQL query to get the second higheset salary from the Employee Table
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+



SELECT MAX( Salary)
  FROM Employee
 WHERE Salary < ( SELECT MAX( Salary) FROM Employee )