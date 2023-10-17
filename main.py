import subprocess

import threading
import time
import schedule


spider_name = ['departures', 'positions', 'routes', 'stops', 'stops_in_trips', 'trips']


def create_index():
    pass


def start_spider(spider_name: str):
    try:
        command = f'scrapy crawl {spider_name}'
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Scrapy spider: {e}")


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every(3).seconds.do(run_threaded, lambda: start_spider('positions'))
schedule.every(3).seconds.do(run_threaded, lambda: start_spider('departures'))
schedule.every(2).hours.do(run_threaded, lambda: start_spider('routes'))
schedule.every(2).hours.do(run_threaded, lambda: start_spider('stops'))
schedule.every(2).hours.do(run_threaded, lambda: start_spider('stops_in_trips'))
schedule.every(2).hours.do(run_threaded, lambda: start_spider('trips'))


while 1:
    schedule.run_pending()
    time.sleep(1)
