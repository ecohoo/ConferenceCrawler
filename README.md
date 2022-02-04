# ConferenceCrawler
Crawl and analyse NLP conference papers.

Required library: selenium, requests, python-slugify.

```
config = {
        "conference": {
            "ACL",
            "NAACL",
            "EMNLP",
            "ICLR",
            "ICML",
            "KDD",
            "NeurIPS",
            "SIGIR",
            "WSDM",
            "WWW"
        },
        "year": {
            2020,
            2021
        },
        "download_paper": True,
        "download_path": "build/conference",
        "clear_download_path": False,
        "thread_pool_size": 5,
        "include": {
            "text",
            "classification",
            "few"
        },
        "exclude": {}
    }
```

"conference": the conferences to be crawled.  
"year": which year we need to crawl.  
"download_paper": if you want to download crawled paper, set it True.  
"download_path": the path to download paper.  
"clear_download_path": if you want to clear history downloaded paper before crawl, set it True.  
"thread_pool_size": the thread pool size for concurrent operation.  
"include": the keywords for search papers.  
"exclude": do not include these keywords when search papers.
