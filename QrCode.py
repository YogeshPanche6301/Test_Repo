import qrcode

url=input("Enter your Url:")
img=qrcode.make(url)
img.save('qrcode.png')
print("QRCode generated successfully >>")