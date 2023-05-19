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

# Get the slot time and elapsed query time
# slot_time = query_job.total_slot_ms
slots_time = query_job.slot_millis
bytes_processed = query_job.total_bytes_processed


# Print the slot time and elapsed query time
print('Slots time: {} ms'.format(slots_time))
print('Bytes processed: {}'.format(bytes_processed))


# Iterate over the results and print the output
for row in results:
    print(row)
