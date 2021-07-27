from threading import Thread as th
import queue
import requests


def proxa():
    global q
    prox = q.get()
    pro = {

        'http':f'socks4://{prox}',
        'https':f'socks4://{prox}'
    }
    try:
        r = requests.get('https://wtfismyip.com/text',proxies=pro,timeout = 7)
        with open('q.txt','a') as f:
            f.write(str(prox)+'\n')
        print(prox)
    except Exception as e:
        print(e)
        proxa()

q = queue.Queue()
proxies = open('prox.txt').read().strip().split('\n')
for i in proxies:
    q.put(i)


print('cart')
for i in range(100):
    th(target=proxa).start()