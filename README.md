# file-system-browser
## To Run
- Clone the repository and run `docker-compose up --build` in the cloned directory.
- The results of the contents API can be viewed at http://127.0.0.1:8000/contents/
## API Documentation

### 1. GET /contents/{path}
Returns either the contents of the file or directory at the given path. The path is relative to the root directory of the docker container (see Notes section below).
#### Example for file:
`GET /contents/app/requirements.txt`

```
{
  "contents": "attrs==21.4.0\nautopep8==1.6.0...(etc.)"
}
```
#### Example for directory:
`GET /contents/app`

```
{
  "contents": {
    ".git/": {
      "owner": "root", 
      "permissions": "755", 
      "size": 416
    }, 
    ".gitignore": {
      "owner": "root", 
      "permissions": "644", 
      "size": 336
    }, 
    ".pytest_cache/": {
      "owner": "root", 
      "permissions": "755", 
      "size": 192
    },
    ...
}
```

## Notes

- API code is in `api.py` and test code is in `test.py`. `test.py` includes brief notes on some additional tests and testing infrastructure that would be worth implementing in addition to the very basic tests I wrote already.
- As is, the root directory is hardcoded in `api.py` and it's relative to the root directory of the docker container and not the host machine. I think I see one way to potentially make that work: having the user supply the directory to a shell script which sets an environment variable and runs docker-compose, which then creates a volume based on the supplied directory that the code can then access. But that feels clunky and I was running into opaque permissions bugs which made me suspect there's some better way I'm not seeing.
- I considered having a separate endpoint for files than the one for directories since they seem like such different resources. With a single endpoint, I think a first time user might be surprised that listing a file path shows the full text of the file rather than, say, info about the file similar to what you get if you run `ls` on a file path. But I ended up opting for a single endpoint for both because I think once someone is aware of the behavior, it's actually much easier to use. Having to know or check in advance whether a path leads to a file or directory in order to know which API to call would be a painful experience.
