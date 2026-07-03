from api.bigquery_client import client

def execute_query(query):

    rows = client.query(query).result()

    resultado = []

    for row in rows:
        resultado.append(dict(row.items()))

    return resultado