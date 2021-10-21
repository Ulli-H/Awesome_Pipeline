"""
All SQL queries and statements to create tables and insert data.
"""

# Drop table queries

drop_immigrations = "DROP TABLE IF EXISTS immigrations;"
drop_temperature = "DROP TABLE IF EXISTS temperatures;"
drop_demographics = "DROP TABLE IF EXISTS demographics;"


# Create table queries

create_immigrations = """
CREATE TABLE IF NOT EXISTS public.immigrations (
    cicid    FLOAT PRIMARY KEY,
    year     FLOAT,
    month    FLOAT,
    cit      FLOAT,
    res      FLOAT,
    iata     VARCHAR(3),
    arrdate  FLOAT,
    mode     FLOAT,
    addr     VARCHAR,
    depdate  FLOAT,
    bir      FLOAT,
    visa     FLOAT,
    count    FLOAT,
    dtadfile VARCHAR,
    entdepa  VARCHAR(1),
    entdepd  VARCHAR(1),
    matflag  VARCHAR(1),
    biryear  FLOAT,
    dtaddto  VARCHAR,
    gender   VARCHAR(1),
    airline  VARCHAR,
    admnum   FLOAT,
    fltno    VARCHAR,
    visatype VARCHAR
);
"""

create_temperature = """
CREATE TABLE IF NOT EXISTS temperatures (
    timestamp                      DATE,
    average_temperature            FLOAT,
    average_temperature_uncertainty FLOAT,
    city                           VARCHAR,
    country                        VARCHAR,
    latitude                       VARCHAR,
    longitude                      VARCHAR
);
"""

create_demographics = """
CREATE TABLE IF NOT EXISTS demographics (
    city                   VARCHAR,
    state                  VARCHAR,
    media_age              FLOAT,
    male_population        INT,
    female_population      INT,
    total_population       INT,
    num_veterans           INT,
    foreign_born           INT,
    average_household_size FLOAT,
    state_code             VARCHAR(2),
    race                   VARCHAR,
    count                  INT
);
"""


# Insert table queries

immigration_insert = ("""
INSERT INTO immigrations (cicid, year, month, cit, res, iata, arrdate, mode, addr, depdate, bir, visa, count, dtadfile, \
entdepa, entdepd, matflag, biryear, dtaddto, gender, airline, admnum, fltno, visatype) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""")

temperature_insert = ("""
INSERT INTO temperatures (timestamp, average_temperature, average_temperature_uncertainty, city, country, \
latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s)""")

demographic_insert = """
INSERT INTO demographics (city, state, media_age, male_population, female_population, total_population, \
num_veterans, foreign_born, average_household_size, state_code, race, count) VALUES (%s, %s, %s, %s, \
%s, %s, %s, %s, %s, %s, %s, %s)"""


# Query lists to use in script
drop_tables_list = [drop_immigrations, drop_temperature, drop_demographics]
create_tables_list = [create_immigrations, create_temperature,  create_demographics]
