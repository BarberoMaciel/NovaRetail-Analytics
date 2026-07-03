from google.cloud import bigquery

PROJECT_ID = "project-d935bc51-c320-4917-9bd"
DATASET = "novaretail_semantic"

client = bigquery.Client(project=PROJECT_ID)