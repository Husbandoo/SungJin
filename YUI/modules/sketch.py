from YUI import pgram
from pyrogram import filters


@pgram.on_message(filters.command("sketch") & ~filters.photo)
def sketch(_, message):
    message.reply("Creating Sketch...")
    # Download the image
'''image = message.photo.download("image.jpg")
    
    # Open the image using Pillow
    from PIL import Image, ImageFilter
    im = Image.open(image)
    
    # Apply the BLUR and CONTOUR filters
    im = im.filter(ImageFilter.BLUR).filter(ImageFilter.CONTOUR)
    
    # Save the filtered image
    im.save("sketch.jpg")
    
    # Send the sketch to the user
    pgram.send_photo(message.chat.id, "sketch.jpg")
    message.reply("Sketch Successfully Printed.")
'''
