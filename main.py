from conference import crawler

if __name__ == '__main__':
    config = {
        "conference": {
            "ICLR",
            "ICML",
            "NeurIPS",
            "COLT"
        },
        "year": {
            2020,
            2021
        },
        "download_paper": True,
        "download_path": "build/conference",
        "clear_download_path": True,
        "thread_pool_size": 5,
        "include": {

            "classif"
        },
        "exclude": {}
    }
    crawler.crawl(config)
