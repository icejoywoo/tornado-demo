#!/usr/bin/env python2.7
# encoding: utf-8

"""
    @brief: ioloop demo
    @author: icejoywoo
    @date: 15/11/24
"""

from __future__ import print_function

import tornado.gen
import tornado.httpclient
import tornado.ioloop


@tornado.gen.coroutine
def fetch_coroutine(url):
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = yield http_client.fetch(url)
    raise tornado.gen.Return(response.body)


@tornado.gen.coroutine
def print_response(url):
    response = yield fetch_coroutine(url)
    print(response)


def synchronous_fetch(url):
    http_client = tornado.httpclient.HTTPClient()
    response = http_client.fetch(url)
    return response.body


def asynchronous_fetch(url, callback):
    http_client = tornado.httpclient.AsyncHTTPClient()
    def handle_response(response):
        callback(response.body)
    http_client.fetch(url, callback=handle_response)


if __name__ == '__main__':
    ioloop = tornado.ioloop.IOLoop.current()
    print(synchronous_fetch('http://www.baidu.com/'))
    #  if the `.IOLoop` is not yet running, you can start the IOLoop, run the coroutine,
    # and then stop the IOLoop with the IOLoop.run_sync method.
    ioloop.run_sync(lambda: asynchronous_fetch('http://www.baidu.com', lambda x: print(x)))
    # call asynchronous func
    ioloop.spawn_callback(asynchronous_fetch, 'http://www.baidu.com', lambda x: print(x))
    ioloop.spawn_callback(print_response, 'http://www.baidu.com')
    ioloop.start()
