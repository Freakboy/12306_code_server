import multiprocessing
import os

bind = "0.0.0.0:8000"
workers = os.getenv("WORKERS",1)
worker_class = "gevent"