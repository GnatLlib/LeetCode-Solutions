select E1.Name as Employee
from Employee as E1, Employee as E2
where E1.ManagerID = E2.ID and E1.Salary > E2.Salary