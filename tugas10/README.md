# Percobaan Code
## Jalankan runserver.sh yang akan menjalankan async_server.py pada port 9002, 9003, 9004, 9005

![Client](bukti/1.png)

## Jalankan lb.py pada port 44444
![Client](bukti/2.png)

## Buka http://localhost:44444/page.html

![Client](bukti/bukti.png)

# Perbandingan Hasil
## server_async_http.py pada port 45000
![Client](bukti/11.png)

## server_thread_http.py pada port 46000
![Client](bukti/22.png)

## asyncronus server dengan load balance
![Client](bukti/33.png)

## Kesimpulan
Dari ketiga tabel tersebut, dapat kita lihat bahwa asyncronus server yang
menggunakan load balancer dapat memproses hasil yang lebih cepat jika dibandingkan
dengan asyncronus server biasa dan multithread server. Hal ini dapat terjadi karena
adanya load balancer untuk mendistribusikan request ke backend secara bergantian
sehingga dapat mempercepat pemrosesan request.
