import logging
import subprocess


def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    logging.info(proc_stdout)


subprocess_cmd('python manage.py dailystar_crawl')
subprocess_cmd('python manage.py dailysun_crawl')
subprocess_cmd('python manage.py express_crawl')
