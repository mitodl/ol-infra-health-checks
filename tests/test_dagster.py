import os
import pytest  # type: ignore[import-not-found]
import testinfra  # type: ignore[import-not-found]


from dagster_graphql import DagsterGraphQLClient
from typing import Any, Dict, List, Literal, Tuple


dagster_env: Literal["dev", "qa", "production"] = os.environ.get(  # type: ignore  # noqa: PGH003
    "DAGSTER_ENVIRONMENT", "dev"
)

# define prod and dev dagster urls
dagster_url_map = {
        "dev": ["dagster_webserver", 3000],
        "qa": ["dagster-webserver", 3000],
        "production": ["dagster-webserver", 3000],
}

# GQL Query for code_location status
location_status_query = ("""
query LocationStatusesQuery {
  workspaceOrError {
                ... on Workspace {
      locationEntries {
        ... on WorkspaceLocationEntry {
          id
          loadStatus
          locationOrLoadError {
            __typename
          }
        }
      }
    }
  }
}
""")

def parseLocationEntries(location_entries: List[Dict[str, Any]]) -> Tuple[List[str], List[str]]:
  i=0
  errored=[]
  loaded=[]
  for location in location_entries:
    i+=1
    locationOrError = location["locationOrLoadError"]
    typeName = locationOrError["__typename"]
    loadStatus = location["loadStatus"]
    if typeName == "PythonError" or loadStatus != "LOADED":
      errored.append(location["id"])
    elif typeName == "RepositoryLocation" and loadStatus == "LOADED":
      loaded.append(location["id"])
  return errored, loaded

def get_dagster_client(
    dagster_env: Literal["dev", "qa", "production"]
):
    # get the correct dagster url for the current environment
    dagster_url, port = dagster_url_map[dagster_env]
    dagster_client = DagsterGraphQLClient(hostname=dagster_url, port_number=port)
    return dagster_client

# monitoring Dagster code_location load status
def test_dagster_code_locations():
    dagster_client = get_dagster_client(dagster_env)
    location_status = dagster_client._execute(location_status_query)
    location_entries = dict(location_status["workspaceOrError"])["locationEntries"]
    errored, loaded = parseLocationEntries(location_entries)
    assert errored == []
