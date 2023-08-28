-- 1. Retrieve all records from the Employees table.
SELECT * FROM employees;

-- 2. Get the Email address of an employees where FirstName='Robert' and LastName='King'

SELECT EMAIL FROM employees
WHERE FirstName='Robert' AND LastName='King';

-- 3. Get the information of an employees where Firstname='Robert' and LastName='King'
SELECT * FROM employees
WHERE FirstName='Robert' AND LastName='King';

-- 4. Retrieve the FirstName, LastName, BirthDate, Address, City, and State from the Employees table
SELECT FirstName, LastName, BirthDate, Address, City, State
FROM employees;

--5. Find the employee with BirthDate of 1965-03-03 00:00:00
SELECT * FROM employees
WHERE BirthDate='1965-03-03 00:00:00';

--6. Retrieve all the columns from the Tracks table, but only return 20 records
SELECT * FROM tracks LIMIT 20;

--7. What is the runtime in Milliseconds for the 5th track,
--   entitled "Princess of Dawn"
SELECT Milliseconds FROM tracks
WHERE TrackId='5';
-- OR
SELECT Milliseconds FROM tracks
WHERE TrackId='5';

--8. Get data from tracks table, who is the composer with TrackId = 18
SELECT * FROM tracks
WHERE TrackId=18;

--9. Retrieve all data from the artists table, how many artist do you know
SELECT * FROM artists;

--10. Get all data from the invoices table, what is the billing address from customer 31
SELECT * FROM invoices
WHERE CustomerId=31;

--11. Get the playlist id, and name from the playlists table.
SELECT * FROM playlists;
--    How many playlists are there?
SELECT count(*) FROM playlists;

--12. Return the Customer Id, Invoice Date, Billing City from the Invoices tables
SELECT CustomerId, InvoiceDate, BillingCity FROM invoices;
--    What city is associated with Customer ID number 42?
SELECT CustomerId, InvoiceDate, BillingCity FROM invoices
WHERE CustomerId=42;
--    What was the invoice data for the customer in Santiago?
SELECT * FROM invoices
WHERE BillingCity='Santiago';

--13. Return the FirstName, LastName, Email, and Phone from the Customer Table.
SELECT FirstName, LastName, Email, Phone FROM  customers;
--    What is the telephone number for Jennifer Peterson?
SELECT * FROM customers
WHERE FirstName='Jennifer' AND LastName='Peterson';
--OR
SELECT Phone FROM customers
WHERE FirstName='Jennifer' AND LastName='Peterson';

--14. Return the TrackId, GenreId, Composer, UnitPrice from the Tracks table.
SELECT TrackId, GenreId, Composer, UnitPrice FROM tracks;
--    How much do this Tracks cost?
SELECT UnitPrice FROM tracks;
--    Total cost of all tracks
SELECT sum(UnitPrice) FROM tracks;

--15. Select all the columns from the Playlist Track table and Limit the results to 10 records.
SELECT * FROM playlists LIMIT 10;
-- Count number of playlists
SELECT count(*) playlists;

--16. Select all columns from the Media Types table and limit the results to 50 records.
SELECT * FROM media_types;
SELECT * FROM media_types LIMIT 50;
SELECT count(*) FROM media_types;
--    What happened when you ran this query? were you able to get all 50 records?
--    Ans: Only 5 records returned

--17. Select all the columns from the Albums table and limit the results to 5 records.
SELECT * FROM albums;
--    Limit the results to 5
SELECT * FROM albums LIMIT 5;
--    Count total albums
SELECT * FROM albums LIMIT 5;