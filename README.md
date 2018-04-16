# simple scrapper
scrapper codes written in python3. It searches most of the domain path for a match and outputs the result in a file.


just run the code in the generic folder.

alter the options in the `config.json` file

options are:

* domain -> website url for code to search for data
* url_regex -> the path to search in. Program skips looking for data in url if the path after the `domain` name cannot be found
* keyword_regex -> if match is found in page content, the match will be written to the `output_filename`
* use_proxy -> boolean to determine if program needs to use generated proxy
* login -> login credentials of `username`  and  `password`   separates by a colon
* method -> request method to use. default is `GET`
* output_filename -> name of the file where match results should be stored.


## Sample config.json

```json
{
    "domain": "https://example.com",
    "url_regex": ".*",
    "keyword_regex": "(.*?@gmail.com)",
    "use_proxy": false,
    "login": "username:password",
    "method": "GET",
    "output_filename": "result.txt"
}
```

> The program may fail after a while due to `maximum recursion depth exceeded` error. If this is the case, just rerun the code and the program will resume execution without overriding the previous  `output_filename` content.

## To be implemented

[] use proxy
[] login

## contributing
To contribute, simply fork this repository and create a pull request
