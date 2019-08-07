import os
import threading
import time
import uuid
from uuid import getnode as get_mac

import mmh3


def orderid():
    now = int(time.time() * 10000)
    mac = get_mac()
    pid = os.getpid()
    tid = threading.get_ident()
    p_time = int(time.process_time() * 10 ** 9)
    p_time = str(p_time).zfill(8)[-8:]
    uniq_id = mmh3.hash(f"{now}{mac}{pid}{tid}{p_time}", signed=False)
    uniq_id = str(uniq_id).zfill(10)
    order_id = f"{now}{uniq_id}{p_time}"
    return str(order_id)
