import logging
import os
import threading
import requests
from queue import Queue

def download_gambar(url):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        namafile = namafile.split(".",1)[0]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

list_gambar =["https://cdn.idntimes.com/content-images/post/20191220/73017677-2248225938749972-2951715633794400605-n-1-9a82bb25cb27a28a5ba980bed5b11493_600x400.jpg",
              "https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg"]

que = Queue()
def c_url():
    while True:
        url = que.get()
        download_gambar(url)
        que.task_done()

for url in list_gambar:
    que.put(url)

for scan in range(1,3):
    t = threading.Thread(target=c_url)
    t.daemon=True
    t.start()
que.join()

