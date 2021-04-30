import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import qrcode

df = pd.read_csv("students.csv")
df = df.dropna()

df

records = df.to_dict(orient='record')

def generate_qr(data):
    
    A= data['id']
    B= data['name']
    C= data['class']
    D= data['dob']
    img = qrcode.make("{}raitrait{}raitrait{}raitrait{}".format(A,B,C,D))
    return img


for record in records:
    qr = generate_qr(record)
    qr.save(f"photos/{record['id']}.jpg")

font = ImageFont.truetype("OpenSans-Semibold.ttf", size=25)


def generate_card(data):
    template = Image.open("template.png")
    pic = Image.open(f"photos/{data['id']}.jpg").resize((165, 190), Image.ANTIALIAS)
    template.paste(pic, (25, 75, 190, 265))
    draw = ImageDraw.Draw(template)
    draw.text((315, 80), str(data['id']), font=font, fill='black')
    draw.text((315, 125), data['name'], font=font, fill='black')
    draw.text((315, 170), data['class'], font=font, fill='black')
    draw.text((315, 215), data['dob'], font=font, fill='black')
    return template


for record in records:
    card = generate_card(record)
    card.save(f"cards/{record['id']}.jpg")
