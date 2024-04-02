from PIL import Image, ImageDraw, ImageFont

#open images
img = Image.open('./src/imgs/template_01.png')
placeholder = Image.open('./src/imgs/template_01_placeholder.png')


#Text vars:
text_curso = "Curso de Python"


#set colors for the project
main_color = '#B66C6C'
text1_color = '#825858'
text2_color = '#B66C6C'

#load fonts
font_maitree = ImageFont.truetype("./src/fonts/Maitree/Maitree-Bold.ttf", 50)
draw = ImageDraw.Draw(img)


#set padding for the border
border_w = img.size[0] * 0.1 / 2
border_h = img.size[1] * 0.13 / 2

#draw border
img.paste(placeholder, (0,0))
draw.rectangle([
    (border_w,border_h),
    (img.size[0]-border_w, img.size[1]-border_h)], 
    fill=None, 
    outline=main_color, 
    width=25
    )

#draw text
draw.text((
    img.size[0]/2, 
    img.size[1]* 0.345), 
    text_curso, 
    font=font_maitree,
    fill=text1_color, 
    anchor='mm')



img.show()