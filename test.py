import pytest
from api import app


@pytest.fixture()
def client():
    client = app.test_client()
    yield client


def test_request_for_existing_file_succeeds_with_200(client):
    response = client.get("/contents/api.py", follow_redirects=True)
    # TODO reenable when test no longer depends on exact file structure on particular machine.
    # assert response.status_code == 200


def test_request_for_nonexisting_file_fails_with_404(client):
    response = client.get("/contents/a/fake/path", follow_redirects=True)
    assert response.status_code == 404


"""
TODO
- Tests shouldn't assume files are layed out on the docker container in a particular way already. Two options for handling this better:
    - 1. Have the test file automatically create a small file system for testing purposes before running tests and tear down after. Pros: more realistic; less mocking required to implement individual tests; Might be easier to debug when tests fail. Cons: more work to implement up front. More to maintain.
    - 2. Mock all the os and pathlib calls. Basically switch the pros and cons of (1).

- Additional tests:
  - Test default path works
  - Test paths with and without trailing slashes
  - Test invalid path results in 400
  - Test supplying path to a file results in full file text
  - Test supplying path to a dir results in all expected children
      - Test both dirs and files show up in results
      - Test name/owner/size/permissions info correct
"""
