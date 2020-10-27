 DROP TABLE  "zillow", "realtor"

CREATE Table Zillow (
	ZipCode	INT  ,
	StateName VARCHAR,
	CountyName VARCHAR,
	CityName 	VARCHAR,
	ForecastedDate DATE,
	ForecastYoYPctChange DECIMAL,
	ID SERIAL PRIMARY KEY

);

CREATE TABLE Realtor(
	ZipCode	INT,
	median_listing_price INT,
	average_listing_price INT,
	total_listing_count INT,
	median_listing_price_per_square_foot DECIMAL,
	ID SERIAL PRIMARY KEY
);


select * from zillow
INNER JOIN realtor
ON zillow.ZipCode = realtor.zipcode

-- JOIN TABLES
SELECT r.ZipCode, r.median_listing_price, r.average_listing_price, r.total_listing_count, r.median_listing_price_per_square_foot, z.ZipCode, z.StateName, z.CountyName, 
	z.CityName, z.ForecastedDate, z.ForecastYoYPctChange
FROM zillow as z
INNER JOIN realtor as r
ON z.ZipCode = r.ZipCode;


