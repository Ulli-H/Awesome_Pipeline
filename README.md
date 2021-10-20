# Awesome_Pipeline
This Project shows an end-to-end workflow for an ETL pipeline.

*Capstone Project Udacity Data Engineer Nanodegree*

## Content
- [Description](#description)
- [Data](#data)
- [Data Model](#data-model)
- [Tools and Technologies](#tools-and-technologies)
- [Workflow](#workflow)
- [Questions](#questions)
- [Links](#links)

## Description  

In this project data on immigration to the United States is used and enriched with city demographics data and temperature data to form a broader basis for analysis. The goal is it to transform the data in an appropriate way and build a suitable data model for analytical purposes.
The choice of tables is described in the [Data Model](#data-model) section. 



## Data 

### Immigration data
This dataset is provided by the [US National Tourism and Trade Office](#https://travel.trade.gov/research/reports/i94/historical/2016.html)

### Temperature data
The earth surface temperature dataset on [Kaggle.com](#https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data) is used for this. 

## Demographics data
The demographics dataset from US cities comes from [OpenDataSoft](#https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/?dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6InVzLWNpdGllcy1kZW1vZ3JhcGhpY3MiLCJvcHRpb25zIjp7fX0sImNoYXJ0cyI6W3siYWxpZ25Nb250aCI6dHJ1ZSwidHlwZSI6ImNvbHVtbiIsImZ1bmMiOiJBVkciLCJ5QXhpcyI6Im1lZGlhbl9hZ2UiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjRkY1MTVBIn1dLCJ4QXhpcyI6ImNpdHkiLCJtYXhwb2ludHMiOjUwLCJzb3J0IjoiIn1dLCJ0aW1lc2NhbGUiOiIiLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlfQ%3D%3D).


## Data Model
The key information is stored in the immigrations fact table and addititonal information is tsored in the dimension tables. All tables can be joined on common identifier columns.   

###### fact tables
|name | colums | description|  
|--- | --- | ---|  
|immigrations | cicid - year - month - cit - res - iata - arrdate - mode - addr - depdate - bir - visa - coun- dtadfil - visapost - occup - entdepa - entdepd - entdepu - matflag - biryear - dtaddto - gender - insnum - airline - admnum - fltno - visatype | the I94 immigration data|  

###### dimension tables
|name | columns | description|  
|--- | --- | ---|   
| temperature | timestamp - average_temperature - average_temperatur_uncertainty - city - country - latitude - longitude | temperature data for U.S. cities per day |  
| demographics | city - state - media_age - male_population - female_population - total_population - num_veterans - foreign_born - average_household_size - state_code - race - count | demographics data for U.S. cities |  


## Tools and Technologies
* Python and Pandas for data wrangling  
* PostgreSQL as a database and Redshift in a second iteration if more performance is needed  
* Spark dataframes for distributed data processing in a second iteration if needed  
* Airflow for automation, scheduling and monitoring of the pipeline if needed  


## Workflow
1. Data exploration and cleaning  
2. creating the tables with script      make_tables.py    
3. inserting data into tables  


## Questions

What would I do differently if the data was increased by 100x?

Choose Spark for efficient, distributed data processing with EMR or Glue 


What would I do if the pipelines were run on a daily basis by 7am?

Run the pipeline script as a cronjob for example on a kubernetes cluster or with Glue. 
Another option would be using Airflow as a tool for the pipeline logic. Airflow comes with a lot of advantages in terms of monitoring and visibility, especially when managing different pipelines and the GUI makes it accessible also for non-data-engineers.


What would I do if the database needed to be accessed by 100+ people?

Move the data to a Redshift data warehouse to make it accessible for that many users. 

## Links
