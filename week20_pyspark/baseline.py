from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg, broadcast, sum

spark = SparkSession.builder.appName("OptimizationExample").master("local[4]").config("spark.driver.memory", "2g").getOrCreate()

geo_df = spark.read.csv("olist_geolocation_dataset.csv", header=True)
customer_df = spark.read.csv("olist_customers_dataset.csv", header=True)
joined_df = geo_df.join(customer_df, geo_df.geolocation_zip_code_prefix == customer_df.customer_zip_code_prefix)
distinct_df = joined_df.distinct()
aggregated = distinct_df.groupBy("customer_city").agg(
    count("customer_id").alias("num_customers"),
    avg("geolocation_lat").alias("avg_lat"),
    avg("geolocation_lng").alias("avg_lng")
)
final_df = aggregated.filter(aggregated.customer_city != "sao paulo")
sorted_df = final_df.sort(col("num_customers").desc())
sorted_df.show()
input("press enter to end spark")
