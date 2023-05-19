from google.cloud import bigquery

# Create a BigQuery client
client = bigquery.Client(project='teacher-chat-385416')


# Define the project ID and dataset ID for the public dataset you want to query
project_id = 'bigquery-public-data'
dataset_id = 'samples'

# Define your SQL query
query = """
    SELECT *
    FROM `{}.{}.__TABLES__`
    LIMIT 10
""".format(project_id, dataset_id)

# Submit the query job
query_job = client.query(query)

# Fetch the results
results = query_job.result()

# Iterate over the results and print the output
for row in results:
    print(row)


# Get query statistics
query_stats = query_job.query_statistics

# Get BigQuery slot and elapsed query times
slot_millis = query_stats.slot_millis
elapsed_time = query_stats.end_time - query_stats.start_time

# Print the output
print(f"BigQuery Slot Time: {slot_millis} ms")
print(f"Elapsed Query Time: {elapsed_time.total_seconds()} seconds")
