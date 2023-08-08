# Big-Data-Analysis-NCDC-Records-Exploration
This project delves into the realm of big data technology and its practical applications through four distinct components. The provided project data zip file serves as the foundational dataset for each stage of exploration.

## Part 1: Average Wind Direction Calculation
In this section, a Mapper and Reducer application are developed to calculate the average wind direction (in degrees) for each observation month across different years. The dataset, drawn from NCDC records, is leveraged to derive insights. Notably, data quality is indicated by values in the range [0, 1459], while missing data is represented by 999.

## Part 2: Sky Ceiling Height Range Determination
A Python application designed for PySpark is crafted to compute the range (max-min) of sky ceiling height (in meters) for individual USAF weather station IDs. Utilizing the NCDC records dataset, this analysis takes into account data quality, where values within [0, 1459] signify good quality data and 99999 denotes missing data.

## Part 3: USAF Weather Station ID and Visibility Distance Extraction
In this phase, a Mapper and Reducer application extract USAF weather station IDs and visibility distances (in meters) from the NCDC records. The collected data is then consolidated and stored in a dedicated text file. Quality data is indicated by values within [0, 1459], while 999999 denotes missing data.

## Part 4: Pig Analysis of Visibility Distance
The final stage involves utilizing Pig to ingest the text file generated in Part 3. The objective is to determine the range of visibility distances associated with each USAF weather station ID. Through data processing and analysis, the variability in visibility distances is ascertained.

This comprehensive project demonstrates the practical implementation of big data technologies, encompassing data extraction, transformation, and analysis using a variety of tools. By following these four phases, participants gain valuable insights into data manipulation and exploration within a big data context. The project's documentation and codebase are hosted within a Git repository to ensure version control and collaboration capabilities
