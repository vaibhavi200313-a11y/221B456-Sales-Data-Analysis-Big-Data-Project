# Sales Data Analysis - Big Data Project

**Student:** Vaibhavi  
**Roll Number:** 1240258482  
**Section:** BCA(DS-AI)-24  
**Submitted To:** Mr. Vikash (IBM)

## Problem Statement
Analyze total sales per product category from a sales dataset using Hadoop MapReduce.

## Dataset Description
CSV file with columns: order_id, product, category, price, quantity, region, 
date, customer_id, payment_mode, discount

## Steps to Run
1. Upload dataset to HDFS:
   hdfs dfs -put dataset.csv /user/cloudera/vaibhavi/sales/
2. Run MapReduce job:
   hadoop jar hadoop-streaming.jar -mapper "python Mapper.py" -reducer "python Reducer.py"
3. View output:
   hdfs dfs -cat /output/part-00000

## Sample Output
Electronics    627000.00
Furniture      175500.00

## Technologies Used
- Hadoop (HDFS, MapReduce)
- Python 3
- Hive
- Cloudera
- Linux
