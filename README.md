# file-system-browser
## To Run
- Clone the repository.
- Ensure docker is running.
- In the cloned directory, start the application by running `./run.sh <path/to/root/directory>` (e.g. `./run.sh /Users/dj/notes`). Some paths, like `/`, result in errors that I haven't gotten around to fixing yet. I've had success with everything under my `/Users` directory though.
- The results of the contents API can be viewed at http://127.0.0.1:8000/contents/
## API Documentation

### 1. GET /contents/{path}
Returns either the contents of the file or directory at the given path, relative to the root path supplied to `run.sh` during setup. For files, the contents is the entire text of the file. For directories, it is a list of the immediate children of the directory with details about each child.
#### Example for file:
`GET /contents/file-system-browser/requirements.txt`

```
{
  "contents": "attrs==21.4.0\nautopep8==1.6.0...(etc.)"
}
```
#### Example for directory:
`GET /contents/file-system-browser`

```
{
  "contents": [
    {
      "name": ".git/", 
      "owner": "root", 
      "permissions": "755", 
      "size": 480
    }, 
    {
      "name": ".gitignore", 
      "owner": "root", 
      "permissions": "644", 
      "size": 336
    }, 
    {
      "name": ".pytest_cache/", 
      "owner": "root", 
      "permissions": "755", 
      "size": 192
    }, 
    {
      "name": "Dockerfile", 
      "owner": "root", 
      "permissions": "644", 
      "size": 120
    },
    ...
}
```

## Notes

- API code is in `api.py` and test code is in `test.py`. `test.py` includes brief notes on some additional tests and testing infrastructure that would be worth implementing in addition to the very basic tests I wrote already.
- I considered having a separate API endpoint for files than the one for directories since they seem like such different resources. With a single endpoint, I think a first time user might be surprised that listing a file path shows the full text of the file rather than, say, info about the file similar to what you get if you run `ls` on a file path. But I ended up opting for a single endpoint for both because I think once someone is aware of the behavior, it's actually much easier to use. Having to know or check in advance whether a path leads to a file or directory in order to know which API to call would be a painful experience.
