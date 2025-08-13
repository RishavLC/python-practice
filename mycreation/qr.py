import qrcode

data = "https://www.python.org"
img = qrcode.make(data)
img.save("python_qr.png")
print("✅ QR Code saved as python_qr.png")
