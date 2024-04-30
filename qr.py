import qrcodes

def generate_qr_code(text, filename='qrcodes.png'):
    qr = qrcodes.QRCode(
        version=1,
        error_correction=qrcodes.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

# Example usage:
text_to_encode = "Hello, I am subh !"
generate_qr_code(text_to_encode)
