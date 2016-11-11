#LeetCode 175. Combine Two Tables
#SQL code

SELECT FirstName, LastName, City, State 
FROM Person p
LEFT JOIN Address a
on p.PersonId = a. PersonId