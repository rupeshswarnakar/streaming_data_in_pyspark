## PySpark Structured Streaming Project

### Overview
This project demonstrates how to use **PySpark Structured Streaming** to process data continuously in near real time. It covers:
- Reading streaming data from a table
- Writing streaming output in batches
- Using `foreachBatch`
- Checkpointing for fault tolerance
- Starting a stream from a specific version or timestamp


### Technologies Used
- Python
- PySpark
- Spark Structured Streaming
- Delta Lake


### Streaming Workflow
1. Create a source table
2. Read the table as a streaming source
3. Process each micro-batch using `foreachBatch`
4. Write output files
5. Use checkpointing to recover progress if the stream stops


### Example: Create a Table
create table emp(id int, name string);

insert into emp values
(1, 'abc'),
(2, 'xyz');

### Real-World Use Cases

- Processing app logs in real time
- Monitoring transactions continuously
- Streaming ETL pipelines
- Updating dashboards with fresh data
- Handling incremental data from Delta tables
