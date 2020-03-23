import shelve
import uuid

class Person:
    def __init__(self):
        self.data = shelve.open('mydata.dat')
    def upload_data(self,nama=None,size=None, type=None):
        if (nama is None):
            return False
        id=str(uuid.uuid4())
        data = dict(id=id,nama=nama, size=size, type=type)
        self.data[id]=data
        return True
    def download_data(self,nama=None):
        for i in self.data.keys():
            try:
                if (self.data[i]['nama'].lower() ==nama.lower()):
                    return self.data[i]
            except:
                return False
    def list_data(self):
        k = [self.data[i] for i in self.data.keys()]
        return k

if __name__=='__main__':
    p = Person()
    p.upload_data("vanBasten","621234","png")
    p.upload_data("vanPersie","621235","txt")
    p.upload_data("vanNistelroy","621236","pdf")
    print(p.list_data())
