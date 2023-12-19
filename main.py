from datetime import date
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image
import streamlit as st
import datetime
import os



def your_year():
    #year = int(input("Which year were you born? : "))
    minDate = datetime.date(1900,1,1)
    maxDate = datetime.date(2100,1,1)
    d = st.date_input("When's your birthday", min_value = minDate, max_value = maxDate)

    d = str(d).split(" ")
    d = str(d[0]).split("-")
    year = int(d[0])

    return year



def calculating_current_year():
    current_time = date.today()
    current_time = str(current_time).split(" ")
    current_time = str(current_time[0]).split("-")

    current_year = int(current_time[0])

    return current_year



def calculating_age(year, user_year):
    
    age = year - user_year + 1

    return age

    
   
def image_editing(current_year, user_year, age):

    im = Image.open("template.png")

    Im = ImageDraw.Draw(im)
    #font = ImageFont.load("arial.pil")
    year_font = ImageFont.FreeTypeFont('Pillow/Tests/fonts/FreeMono.ttf', 75)
    user_year_font = ImageFont.FreeTypeFont('Pillow/Tests/fonts/FreeMono.ttf', 150)
    age_font = ImageFont.FreeTypeFont('Pillow/Tests/fonts/FreeMono.ttf', 250)

    size = (im.size)

    Im.text((((size[0] * 2/3) + 50),75), ("In " + str(current_year + 1)), (0,0,255), font=year_font)

    Im.text(((size[0] * 2/3), size[1]/4), str(user_year), (255,0,0), font=user_year_font)
    
    Im.text(((size[0] * 2/3), size[1] * 2/3), str(age), (0,0,0), font=age_font)

    im.save("age.png")
    st.image('age.png', caption='haha you are getting older TT')

    with open("age.png", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="age.png",
            mime="image/png"
            )
        
    os.remove("age.png")
    



def main():

    st.title('YOU WILL BE ___ YEARS OLD')

    current_year = calculating_current_year()
    user_year = your_year()
    age = calculating_age(current_year, user_year)
    image_editing(current_year, user_year, age)

    



if __name__ == "__main__":
    main()

