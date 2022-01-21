from QR_Scanner import qr_code_scanner
import requests
qr_code = qr_code_scanner('/dev/hidraw0')

while 1 :
    if qr_code.read() :
        url = "http://118.175.167.204/post.php?test="+qr_code.get()
        x = requests.post(url)
        # print(qr_code.get())