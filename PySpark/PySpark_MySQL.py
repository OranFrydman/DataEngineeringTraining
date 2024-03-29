from pyspark.sql import SparkSession
from pyspark.sql import functions as F
# Create SparkSession with MySQL Connector/J JAR file
spark = SparkSession.builder \
    .appName("Read from MySQL") \
    .config("spark.driver.extraClassPath", "venv/Lib/java-lib/mysql-connector-j-8.3.0.jar") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
# Define connection properties
mysql_url = "jdbc:mysql://localhost:3306/mysql"
mysql_user = "root"
mysql_password = "**"
mysql_table = "stats"

# Read data from MySQL
df = spark.read.format("jdbc") \
    .option("url", mysql_url) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .option("dbtable", mysql_table) \
    .option("user", mysql_user) \
    .option("password", mysql_password) \
    .load()

# Show DataFrame
df.show()
level_counts_df = df.groupBy("level").agg(F.count("*").alias("count"))

# Show the new DataFrame
level_counts_df.show()
mysql_table = "level_group_by"

level_counts_df.write \
    .format("jdbc") \
    .mode("overwrite") \
    .option("url", mysql_url) \
    .option("dbtable", mysql_table) \
    .option("user", mysql_user) \
    .option("password", mysql_password) \
    .option("driver", "com.mysql.cj.jdbc.Driver") \
    .save()
# Write the DataFrame 'level_counts_df' to the MySQL database

# Stop SparkSession
spark.stop()
