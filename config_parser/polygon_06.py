import turtle

# потом это - в отдельный файл
import configparser # !!! new
import os           # !!! new

def create_config(path):
    """
    Create, a config file
    """
    config = configparser.ConfigParser()
    config.add_section("mySettings")

    config.add_section("Settings")
    config.set("Settings", "turtle.shape", "turtle")     # turtle.shape('turtle')
    config.set("Settings", "turtle.shapesize", "2,2,1")  # turtle.shapesize(2,2,1)

    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info",
                "You are using %(font)s at %(font_size)s pt")
    
    with open(path, "w") as config_file:
        config.write(config_file)

# =========================================================
path = "s(3)ettings.ini"
font = get_setting(path, 'Settings', 'font')
font_size = get_setting(path, 'Settings', 'font_size')
# =========================================================

turtle.shape('turtle')
turtle.shapesize(2,2,1)
turtle.color('red', 'yellow')
turtle.width(5)


def side(long01, n01):
    turtle.fd(long01)
    turtle.lt(360/n01)


def polygon(long02, n02):
    
    for z in range(n02):
        side(long02, n02)


def poly_fill(long03, n03, color03, col3, fill):

    turtle.color(color03, col3)
    if fill == 0:
       polygon(long03, n03)

    elif fill != 0:
       turtle.begin_fill()
       polygon(long03, n03)
       turtle.end_fill()

while True:
      long04 = int(input("введите длинну стороны _"))            
      n04 = int(input("введите кол-во сторон _"))             
      color1 = input("введите 1-й цвет _")                   
      color2 = input("введите 2-й цвет _")                   
      fill = int(input("закраска не 0, не закраска - 0 _"))  
                                                             
      poly_fill(long04, n04, color1, color2, fill)                
      #input()
      import time
      time.sleep(3)

      turtle.reset()
      turtle.shape('turtle')       
      turtle.shapesize(2,2,1)      
      turtle.color('red', 'yellow')
      turtle.width(5)              
      print('=====================')



