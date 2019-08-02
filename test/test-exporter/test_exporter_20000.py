#!/bin/env python3
from prometheus_client import Gauge, start_http_server
import random
import time
test_metric = Gauge('test_metric', '测试serviceMonitor')
jvm_metrics = Gauge('jvm_memory_use', '模拟jvm数据')
http_request_per_second = Gauge('http_request_per_second', '模拟http请求数据')

if __name__ == "__main__":
    start_http_server(20000)
    while True:
        for i in range(0, 10):
            test_metric.set(random.random())
            jvm_metrics.set(i)
            http_request_per_second.set(i * 1000)
            time.sleep(120)
