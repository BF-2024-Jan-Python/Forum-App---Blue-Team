CHUNK_SIZE = 1024

routes = [
            {"service_name": "authentication",
             "url": "http://127.0.0.1:6000/authentication/",
             "netloc": "127.0.0.1"
             },
            {"service_name": "user",
             "url": "http://127.0.0.1:6002/user/",
             "netloc": "127.0.0.1"
             },
            {"service_name": "history",
             "url": "http://127.0.0.1:6004/history/",
             "netloc": "127.0.0.1"
             },
            {"service_name": "post_and_reply",
             "url": "http://127.0.0.1:6006/post_and_reply/",
             "netloc": "127.0.0.1"
             },
            {"service_name": "message",
             "url": "http://127.0.0.1:6008/message/",
             "netloc": "127.0.0.1"
             },
            {"service_name": "file",
             "url": "http://127.0.0.1:6010/file/",
             "netloc": "127.0.0.1"
             },
            {"service_name": "email",
             "url": "http://127.0.0.1:6012/email/",
             "netloc": "127.0.0.1"
             },
          ]