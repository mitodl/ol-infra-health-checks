
import DagsterGraphQLPythonClient

def test_dagster_loaded_modules():
    dagster_client = DagsterGraphQLPythonClient.Client("http://localhost:3000/graphql")
    result = dagster_client.execute("query { __schema { types { name } } }")
    assert result["data"]["__schema"]["types"] is not None

