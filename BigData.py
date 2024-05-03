from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("DepressedPeopleCount") \
    .getOrCreate()

# Read data into DataFrame
input_file_path = "C:/Users/ACER/Desktop/Keele/Data Visualization/StreamlitData.csv"
df = spark.read.option("header", "true").csv(input_file_path)

# Count the number of depressed people
depressed_count = df.filter(df.Depression == "Depressed").count()

# Count the number of depressed people
not_depressed_count = df.filter(df.Depression == "Not Depressed").count()

# Print the count
print("Number of depressed people:", depressed_count)

# Print the count
print("Number of not depressed people:", not_depressed_count)

# Stop SparkSession
spark.stop()
