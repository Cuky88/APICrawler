# From textual to structured Web API Descriptions
### Knowledge Discovery and Data Mining Seminar 2017
by Selcuk Aklanoglu, Jan-Peter Schmidt, Caroline Dieterich, Han Che and Marcel Ruoff

## APICrawler, Text Mining & Clustering
This document is describing the software and tools used for our work “From textual to structured Web API Descriptions” in the course of the seminar “Knowledge Discovery and Data Mining 2017” at KIT. It is also a step-by-step guidance how to setup and use the software.

## Download, Installation and Usage
Please refere to the [Wiki](../../wiki/1.Start) and make sure, that you read everything carefully. Every step and every other solutions we tried, are described in there.

## Final dataset
If you don't want to run the crawlers, you can download our crawled data from the following links: (they are too big to be uploaded here!)<br>

| Dataset  | Description |
| ------------- | ------------- |
| [linked_data.json](https://drive.google.com/file/d/0B6pePF5DAf_hU0I0WE9uOEtpQkE/view?usp=sharing)  | Linked Web API dataset converted in JSON format  |
| [progweb_final_filtered.json](https://drive.google.com/open?id=0B6pePF5DAf_hZkhxWVZVcjFPMEU)  | Crawled and filtered data from Progweb  |
| [complete_final.json](https://drive.google.com/open?id=0B6pePF5DAf_hU0NhN3BpSmN1Tlk)  | Crawled, filtered data from Google, merged with Progweb  |

<br>
**Place the files in `APICrawler/api_docs/`.**<br>
If you want to use the linked web api dataset, then you need to edit the code, since in that json, some keys are missing. Since we did not work on that dataset, we didn't put much effort in this.

## Live Demo
You can view the live demo on this [website](http://webapi.bplaced.net).
