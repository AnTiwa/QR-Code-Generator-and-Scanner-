import qrcode
he ="hello"
def generate_qr(A, B, C, D):
    img = qrcode.make("{}raitrait{}raitrait{}raitrait{}".format(A,B,C,D))
    return img
    #img.save("1.jpg")



