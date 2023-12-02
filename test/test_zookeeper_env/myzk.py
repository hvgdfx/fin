
from kazoo.client import KazooClient


zk = KazooClient(host="localhost:2181")

zk.start()

children = zk.get_children("/")
print(children)

zk.stop()



