#!/usr/bin/python3
import sys
from time import sleep
import datetime
import secrets

for i in range(10000):
    sleep(secrets.SystemRandom().random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        secrets.SystemRandom().randint(1, 255), secrets.SystemRandom().randint(1, 255), secrets.SystemRandom().randint(1, 255), secrets.SystemRandom().randint(1, 255),
        datetime.datetime.now(),
        secrets.SystemRandom().choice([200, 301, 400, 401, 403, 404, 405, 500]),
        secrets.SystemRandom().randint(1, 1024)
    ))
    sys.stdout.flush()
