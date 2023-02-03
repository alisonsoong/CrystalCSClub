import qrcode

def main():
    img=qrcode.make('1')
    img.save('testqrcode.png')

main()