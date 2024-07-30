import qrcode
from PIL import Image
qr = qrcode.QRCode(version= 5, 
                   error_correction= qrcode.constants.ERROR_CORRECT_H, 
                   box_size= 10, border= 4)
qr.add_data("https://www.linkedin.com/in/aryan-modh-385abb288")
qr.make(fit= True)
img = qr.make_image(fill_color = "black", back_color = "lightblue")
img.save("linkedin1.png")