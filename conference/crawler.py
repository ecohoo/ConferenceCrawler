import shutil
import os

from conference.conf_acl import ACL
from conference.conf_naacl import NAACL
from conference.conf_emnlp import EMNLP
from conference.conf_iclr import ICLR
from conference.conf_icml import ICML
from conference.conf_kdd import KDD
from conference.conf_nips import NeurIPS
from conference.conf_sigir import SIGIR
from conference.conf_wsdm import WSDM
from conference.conf_www import WWW
from conference.conf_colt import COLT
from concurrent.futures import ThreadPoolExecutor, wait


def get_conf(conf_name):
    conference = {
        "ACL": ACL,
        "NAACL": NAACL,
        "EMNLP": EMNLP,
        "ICLR": ICLR,
        "ICML": ICML,
        "KDD": KDD,
        "NeurIPS": NeurIPS,
        "SIGIR": SIGIR,
        "WSDM": WSDM,
        "WWW": WWW,
        "COLT": COLT,
    }
    return conference.get(conf_name, None)


def crawl(config):
    conferences = []
    for conf_name in config['conference']:
        conf = get_conf(conf_name)
        if conf is None:
            print("[ERR] ", conf_name, " not exist!")
            continue
        for year in config['year']:
            if conf_name is "NAACL" and year == 2020:
                continue
            conferences.append(
                conf(year,
                     config['download_paper'],
                     config['download_path'],
                     config['include'],
                     config['exclude']))

    if config["clear_download_path"] and os.path.exists(config['download_path']):
        shutil.rmtree(config['download_path'])

    with ThreadPoolExecutor(max_workers=config['thread_pool_size']) as t:
        all_task = [t.submit(conference.crawl) for conference in conferences]
        wait(all_task)
