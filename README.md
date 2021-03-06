# simple scrapper
scrapper code written in python3. It searches most of the domain path for a match and outputs the result in a file.

> just run the code in the generic folder. Alter the options in the `config.json` file as desired.

options are:

* domain -> website url for code to search for data
* path_regex -> the path to search in. Program skips looking for data in url if the path after the `domain` name cannot be found
* keyword_regex -> if match is found in page content, the match will be written to the `output_filename`. Don't add the `(` and `)` so it can actually match exact regex
* use_proxy -> boolean to determine if program needs to use generated proxy
* login -> login credentials of `username`  and  `password`   separates by a colon
* output_filename -> name of the file where match results should be stored.


## Sample config.json

```json
{
    "domain": "https://www.example.com",
    "path_regex": ".*",
    "keyword_regex": ".*?@gmail.com",
    "use_proxy": false,
    "login": "username:password",
    "output_filename": "result.txt"
}
```

> The program may fail after a while due to `maximum recursion depth exceeded` error. If this is the case, just rerun the code and the program will resume execution without overriding the previous  `output_filename` content.

## To be implemented

[] use proxy


## contributing
To contribute, simply fork this repository and create a pull request
