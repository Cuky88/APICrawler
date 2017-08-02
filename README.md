# From textual to structured Web API Descriptions
### Knowledge Discovery and Data Mining Seminar 2017
by Selcuk Aklanoglu, Jan-Peter Schmidt, Caroline Dieterich, Han Che and Marcel Ruoff

## APICrawler, Text Mining & Clustering
This document is describing the software and tools used for our work “From textual to structured Web API Descriptions” in the course of the seminar “Knowledge Discovery and Data Mining 2017” at KIT. It is also a step-by-step guidance how to setup and use the software.

## Download and Installation
1. To be able to use the software, you need python 2.7. We also highly recommend to setup [virtualenv](https://virtualenv.pypa.io/en/stable/), since many packages need to be installed. 
2. Clone the private repository `git clone git@github.com:Cuky88/APICrawler.git` and activate your virtualenv. 
3. Install all the needed packages with the command `pip install >> requierements.txt` ODER SO ÄHNLICH! <br><br>
**Important:** Tensorflow with GPU version will be installed for the K-Means part. Make sure, that you have a graphics card and CUDA/cudnn is installed!

## Setting up and using the Crawler
The crawler is divided in 3 parts and multi steps, one for [Programmable Web](https://www.programmableweb.com/) (abbr. Progweb), one for crawling Google search results and the last one for crawling the actual API documentation. The crawler files are all located in `APICrawler/api_docs/api_docs/spiders/`. Your working directory should be `APICrawler/api_docs/`.<br><br>
1. [**api_spider.py**](api_docs/api_docs/spiders/api_spider.py) for crawling Progweb:<br>
    **a) Change your working directory to folder `APICrawler/api_docs/`**<br>
    b) start the crawler in the command line with `scrapy crawl apispider`<br>
    The spider will start automatically and crawl Progweb. This can take several hours, since there are lots of APIs. You don't need to change here anything. However, if you want to, you can edit [line 21](api_docs/api_docs/spiders/api_spider.py#L21) and set the ```DOWNLOAD_DELAY``` in seconds to any other number, but 3 seconds are good to go. The results will be saved in `APICrawler/api_docs/apispider_result.json`. <br><br>
    The following data will be collected in the json file:<br>

    | Key  | Description |
    | ------------- | ------------- |
    | api_name  | API name like it is shown on the [overview page](https://www.programmableweb.com/category/all/apis) on Progweb  |
    | progweb_date  | Date on which the API was added to Progweb  |
    | crawled_date  | Date on which the api was crawled  |
    | progweb_url  | URL of API in Progweb  |
    | progweb_cat  | Category tags assigned in Progweb  |
    | api_url  | URL of the host from the API documentation website  |
    | api_url_full  | URL to the documentation website of the API  |
    | progweb_descr  | API description given on Progweb  |
    | progweb_title  | API title given on Progweb when you enter details of API  |
    | page_url  | **Only on Error** containing the Progweb URL if Progweb couldn't be crawled  |
    | HttpError  | **Only on Error** containing the Progweb URL  |
    | DNSLookupError  | **Only on Error** containing the Progweb URL  |
    | TimeoutError  | **Only on Error** containing the Progweb URL  |
    | UnknownError  | **Only on Error** containing the Progweb URL  |

2. [**createID.py**](api_docs/scripts/createID.py):<br>
  Before you proceed, you need to check if there are duplicated entries, due to Progwebs dynamical loading. This will also generate unique IDs for every API. In `APICrawler/api_docs/scripts` there are several scripts, which can be used to do certain tasks. They need to be ajusted to the according input files, usually only the part where the json file is read.<br>
    a) Start the script from command line with `python scripts/createID.py`. You will get a prompt to choose between two datasets. Choose (1) for the Progweb data and hit enter. The processing of the file starts.<br>
    b) You will get a new file named `APICrawler/api_docs/apispider_result_id.json`, which is filtered and has unique IDs.

3. [**testURL.py**](api_docs/scripts/testURL.py):<br>
  After obtaining the data from Progweb, we need to do some some URL checking of the links to the actual API documentations.<br>
    a) Now the URLs have to be checked, if they are reachable. Therefore, start the script from command line with `python scripts/testURL.py`.<br>
    b) After it is finished, you will have a new file in your working directory called `url_test.json`, which has only the keys `progweb_title`, `api_url` and `api_url_full` from the origin input file `apispider_result_id.json`
    The `url_test.json` now contains a new key called `error`, which indicates, if the link is reachable or if it yields an error with ints from 0 to 4: <br>
    
    | Error Code  | Description |
    | ------------- | ------------- |
    | 0  | Nor error on that link  |
    | 1  | HTTPError  |
    | 2  | URLError |
    | 3  | BadStatusLine  |
    | 4  | Unknown error  |

    **Warning:** Running this script takes up to 12 hours!
    
4. [**keyCheck.py**](api_docs/scripts/keyCheck.py):<br>
  With this the `apispider_results_id.json` will be checked if every key is populated. If not, dummy values will be created for the missing keys. Then the results from the link check from step 3 will be included . If a link was not checked, the `error` key will get the value 5. This will also convert all unicode chars to UTF-8.<br>
    a) Start the script from command line with `python scripts/keyCheck.py`.<br>
    b) Results will be saved to `progweb_final_filtered.json` with every key from step 1 and step 3.<br>
    <br>
    If needed, here is an overview of the dummy values for missing keys:<br>
    
    | Key | Dummy |
    | ------------- | ------------- |
    | id  | 000000 |
    | api_name  | NO NAME  |
    | progweb_cat  | NO CATEGORIES |
    | progweb_descr  | NO DESCRIPTION  |
    | progweb_title  | NO TITLE  |
    | progweb_url  | NO PROGWEBURL  |
    | api_url  | NO URL |
    | api_url_full  | NO FULL-URL  |
    | progweb_date  | 01.01.2020  |

**So far, this would be enough to get the working dataset we used for this work. However, if you want to get additional data from Google, you can proceed with the next steps, but be warned, things get complicated!**

### Crawling Google
Google is very effective in blocking the crawler. One solution to overcome this is to set up a proxy. The following steps describe the needed procedure and how to use the crawler [**gsearch.py**](api_docs/api_docs/spiders/gsearch.py) <br><br>
1. Install [scrapoxy](http://scrapoxy.io/) and follow the [documentation](http://docs.scrapoxy.io/en/master/quick_start/index.html) to setup scrapoxy. Best way to go is with an Amazon AWS server. The `conf.json`should be located in the `APICrawler/` main directory. Overwrite the dummy config with yours.<br>

2. If you change anythin on the standard scrapoxy configuration, you must add it into [**gsearch.py**](api_docs/api_docs/spiders/gsearch.py) on lines 45 - 60. **You also have to change [line 50](api_docs/api_docs/spiders/gsearch.py#L50) and add your own scrapoxy password here!** <br>

3. Before you start the crawler, you can modify the search request in [**gsearch.py**](api_docs/api_docs/spiders/gsearch.py) on [line 62](api_docs/api_docs/spiders/gsearch.py#L62) and [line 66](api_docs/api_docs/spiders/gsearch.py#L66). Currently it is set to:<br>
  `Line 62: queries = '+%22api+documentation%22+OR+%22api+reference%22+OR+%22documentation%22'`<br>
  `Line 66: google_base_url_fmt = 'https://www.google.com/search?q=site:{sitename}{query}&lr=lang_en'`<br>
  The `{sitename}`placeholder (line 62) will be replaced with the name of the API from the key `progweb_title`.<br>
  The `{query}`placeholder (line 66) will be replaced with the variable `queries`.<br>
  At the end this will look, for example for the API Paypal like this:<br>
  `https://www.google.com/search?q=site:paypal.com+%22api+documentation%22+OR+%22api+reference%22+OR+%22documentation%22&lr=lang_en` and on the Google page like: `site:paypal.com "api documentation" OR "api reference" OR "documentation"`<br>

4. The gsearch crawler uses the file `progweb_final_filtered.json` to start the crawling process. **Change your working directory back to folder `APICrawler/api_docs/`** and start the crawler from command line with `scrapy crawl gsearch`. The crawler will check the error code, if it is 0, the crawler will do nothing and just write the allready available link as key `link1`. If the error code is anything else then 0, the crawler will start the request to Google and save the first five links.  You can change the number of saved links at [line 65](api_docs/api_docs/spiders/gsearch.py#L65). For every link, an unique key will be generated with the rank of the search result. For example the first result link will be saved in `link1`, the second in `link2` and so on. Results will be saved to `gsearch_result.json` with the following keys:<br>
    <br>
    
    | Key  | Description |
    | ------------- | ------------- |
    | api_url  | URL of the host from the API documentation website  |
    | api_url_full  | URL to the documentation website of the API  |
    | progweb_title  | API title given on Progweb when you enter details of API  |
    | from_g  | 1 = indicating if link was crawled from Google  |
    | error  | The error code from the link checking  |
    | link[#]  | The crawled link from Google and its ranking  |
    | gHttpError  | **Only on Error** containing the Progweb URL  |
    | gDNSLookupError  | **Only on Error** containing the Google URL  |
    | gTimeoutError  | **Only on Error** containing the Google URL  |
    | gUnknownError  | **Only on Error** containing the Google URL  |

5. After the links are extracted, we need to start the actual crawling of the link contents (the API documentation website). Therefore just start the third crawler in command line with `scrapy crawl apidescr`. After it is done, you will get a file called `apidescr_result.json`.

6. [**combGnP.py**](api_docs/scripts/combGnP.py) & [**combDescr.py**](api_docs/scripts/combDescr.py):<br>
  Now further processeing is needed. Due to the way of loading urls, we had to generate one entry in `apidescr_result.json` for every link we had. For example if we had one API with 3 different links from Google, then we have this API three times in `apidescr_result.json` with 3 different single links (`link1`, `link2`, `link3`) with the belonging `descr1`, `descr2` and  `descr3`.<br>
  This can be done with [**combGnP.py**](api_docs/scripts/combGnP.py) and [**combDescr.py**](api_docs/scripts/combDescr.py).<br>
    a) [**combGnP.py**](api_docs/scripts/combGnP.py): This first combines the `gsearch_result.json` from Google with `progweb_final_filtered.json` from Progweb and creates a file called `combGnP.json`. Start the script from the command line with `python scripts/combGnP.py`.<br>
    b) [**combDescr.py**](api_docs/scripts/combDescr.py): Combines now the `combGnP.json` and `apidescr_result.json` to a final dataset called `complete_final.json`. You can run it with `python scripts/combDescr.py`
    
**That's it! Now you should have 3 datasets, the linked Web API, crawled Progweb and the API documentation sites from Google.**



## Final dataset
The final dataset with every information from programmableweb, the link checking, links found from google and the corresponding website contents can be found in this file:<br>
https://drive.google.com/open?id=0B6pePF5DAf_hU0NhN3BpSmN1Tlk
<br><br>
In the api_docs folder is also a file called progweb_final_filtered.json, which only holds the data from programmableweb with the link checking results. This is the final version from programmableweb. You can also download it from GDrive:<br>  https://drive.google.com/open?id=0B6pePF5DAf_hZkhxWVZVcjFPMEU

## Manually Clustered API
The manual clusters can be found here:<br>
https://github.com/Cuky88/APICrawler/tree/master/1_data/4_cluster_single/manuel_cluster/

## Preprocessed Data
Preprocessed data is under:<br>
https://github.com/Cuky88/APICrawler/tree/master/1_data/

## Live Demo
http://webapi.bplaced.net/
