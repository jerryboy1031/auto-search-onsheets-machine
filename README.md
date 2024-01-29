# auto-search-onsheets-machine
### an advanced version of [**scape-chrome-data-**](https://github.com/jerryboy1031/scrape-chrome-data-)


[**auto-search-onsheets-machine**](https://github.com/jerryboy1031/auto-search-onsheets-machine) uses python modules `selenium` and `bs4` to help us scrape the data from web. Then, it writes the results it pick on a csv file. The only thing we do is to open the csv and take a look.

It is **authored by** [**陳佳俊**](https://github.com/jerryboy1031). It is **maintained by** [**陳佳俊**](https://github.com/jerryboy1031).


## Contents

1. [Features](#features)
2. [Contributors](#contributors)
3. [Installation](#installation)
4. [Send Us Feedback!](#send-us-feedback)
5. [License](#license)

## Features

- **[main.py file](https://github.com/jerryboy1031/auto-search-onsheets-machine/blob/main/main.py)** 
    - **extract_website(string)**:
        -  start
        - open a google chrome website
        - search a specific title (i.e. 法國自由行)
        - extract data(titles, urls) from the result

    - **saveTOcsv(data)**
        - open a csv file "google_search_results.csv" with writting mode, and encoded with utf-8
        - save the data to a csv file, and add a header row

## Contributors
- [**陳佳俊**](https://github.com/jerryboy1031)

## Installation
required Python modules:
1. selenium
2. bs4
3. time
4. gspread
5. google.oauth2.service_account

install by `pip install ...`

## Send Us Feedback!
Our library is open source for research purposes, and we want to improve it! So let us know (create a new GitHub issue or pull request, email us, etc.) if you...
1. Find/fix any bug (in functionality or speed) or know how to speed up or improve any part of this project.
2. Want to add/show some cool functionality/demo/project made on top of it. We can add your project link to our project.

## License
OpenPose is freely available for free non-commercial use, and may be redistributed under these conditions. Please, see the [license](./LICENSE) for further details.
