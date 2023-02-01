
/*

1. Student Advisor


Enter your query below.
Please append a semicolon ";" at the end of the query
*/

SELECT student_information.roll_number, student_information.name
FROM faculty_information
INNER JOIN student_information ON faculty_information.employee_id=student_information.advisor
WHERE (faculty_information.gender = 'F' and faculty_information.salary >20000) 
OR (faculty_information.gender = 'M' and faculty_information.salary >15000)



/*

2.Country Codes


Enter your query below.
Please append a semicolon ";" at the end of the query
*/

SELECT customers.customer_id, customers.name, CONCAT('+',country_codes.country_code, customers.phone_number)
FROM customers
INNER JOIN country_codes on customers.country = country_codes.country
ORDER BY customers.customer_id ASC