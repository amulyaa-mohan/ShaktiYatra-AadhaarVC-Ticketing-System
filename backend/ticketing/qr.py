import qrcode

def generate_qr(token: str, path: str):
    img = qrcode.make(token)
    img.save(path)
