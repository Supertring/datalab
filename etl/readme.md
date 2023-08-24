# What is ETL?

* __E__: Extract
* __T__: Transform
* __L__: Load

A data integration process that combines data from multiple data sources into a single, transforms the data anc finally loads data into data warehouse system.

# __Extract__:

* raw data is copied or exported from source locations to a staging area.
* data extracted from various sources
    * SQL/ NoSQL servers
    * ERP systems
    * flat files
    * Emails
    * web pages
* __Identify Data Sources__:
    * Find the source of data
    * Includes database, spreadsheets, APIs, web services, logs, or other data repositories

* __Define Extraction Methods__: 
    * Decide best approach to extract data from the source
    * __FUll Extraction__: extract all the data in one time
    * __Incremental extraction__: extract data incrementally, in batches
    * __Partial extraction__: extract partial data
    * __Real-time__: extract data in real time when needed in as per the requirenment

* __Access Source Systems__:
    * Access data using methods such as:
    * SQL queries for relational databases
    * API calls from web services
    * CSV, EXCEL, JSON, XML file readings
    * Extract information from log files
    
* __Retrieve Data__:
    * Extract and ensure required fields and records as per your requirenments
  
* __Data Profiling__:
    * Analyze extracted data
    * Understand structure, data types, null values, unique values, patterns, quality issues
    * data profiling helps idenfity issues early in the process
  
* __DAta validation__: 
    * verify extracted data meets expectations and defined rules
    * check missing values, data formats inconsistencies, and any anomalies
    
* __DAta staging__: 
    * __Store the data in Staging area__
    * This area acts as an storage space before the transformation phase
    * Staging allows you to manipulate and validate data without affecting the raw source system/data
  
* __Metadata capture__: 
    * Document metadata related to extracted data, eg: source, time, method, tranformation etcs.
* __Error handling and logging__: 
    * design mechanism to handle errors while data extractions, 
    * create logs about success and faliures, 
    * setup alerts and notifications for issues that occurs during the process
* __Data security and compliance__:
    * Ensure extractions is within security and regulations, 
    * apply encryption, authentication and access controls as required
* __Testing and verifications__: 
    * test if the extraction mechanism extract accuracte and complete data, 
    * compare source and extracted data to verify consistency.
    
Extract phase is a foundation to the next phase of ETL process


# Transform

* In the staging area, raw data undergoes data processing.
* The data is transformed according to use cases.
* Some task are as follows:
    * __Data Cleaning__: remove or correct incorrect data, missing values, incosistencies
    * __Data Enrichment__: Add new data to enhance the information in the dataset. This can be done by merging                            data from different sources, using external data, creating new variables
    * __Data Filtering__: Find a subset of data as per specified criteria
    * __Data Aggregation__: Summarize data by groups/categories, use functions like SUM, AVG, COUNT etc.
    * __Data Transformation__: apply mathematical operations, eg: converting units, scaling, apply logarithms,                               normalization
    * __Data Formatting__: Prepare the data to a specific format that is required for a target system.
    * __Data joining/merging__: combine data from various sources based on common fields
    * __Data duplication__: Removing duplicate records from the data
    * __Data validation__: Check if data meets quality and consistency  as per the defined standards
    * __DAta derivation__: create new data using calculations based on existing data


# Load

* The transformed data is transferred to target data warehouse from stagging storage.

* __Target System Selection__:
    * Setup best target system, as per your data storage and analysis.
    * Can be relational db, NoSQL, data warehouse, data lake, disk or any other storage

* __Desing Schema__:
    * Design right schema to store the transformed data
    * Eg: tables, fields, relationships
   
* __DAta Transformation__:
    * some extra transformation can be done optionally.
    * eg: aggregations, calculations etcs.

* __Data Mapping__:
    * Map the fields between source and target systems
    * Ensure data types in the source match those in the target
 
* __DAta loading Stragegies__:
    * Chose right data loading method, 
    * As per factors such as data volume, frequencey of updates, system capabilites
        * __Full Load__: Load all the transformed data in one run.
        * __Incremental load__: load only new/recently modifined data since the last load
        * __Delta load__: load changes/updates of the data
        * __Append-only load__: load only new data without updating existing ones
        * __Merge load__: Combine multiple data sources into a single target dataset
 
* __Data loading Techniques__:
    * __Bulk loading__: load huge volumes of data efficiently at a time
    * __Inserts__: Insert new data into the target systems
    * __Updates__: Update existing records if needed
    * __Upserts__: Insert new records and update existing records if they exist
    
* __Data quality checks__:
    * ensure data quality while loading data
    * ensure the integrity of data loaded
    * check integrity constraints, referential integrity, and other business rules
    
* __Error handling and logging__:
    * Implement error handling mechanism, eg: data validation faliures/db errors
    * save logs to keep track of load and issues that might come up
   
* __Indexing and optimization__:
    * Design appropriate indexs on the target db to optimize query performance
    * make use of clustering strategies for better data retrieval

* __Metadata updates__:
    * Save and update metadata information on loaded data
    * eg: timestamps, load status, etcs

* __Data validation and verification__:
    * Ensure target loaded data in the target system mathces the transformed data
    * ensure it meets the business rules and standards
    
* __Scheduling and Automation__:
    * Make use of scheduling and automation methods as per the business needs and the eco systems.