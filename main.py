from conference import crawler

if __name__ == '__main__':
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
    crawler.crawl(config)
