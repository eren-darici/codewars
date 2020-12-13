def find_screen_height(width, ratio): 
    a,b = ratio.split(":")
    x = int(a) / int(b)
    height = (width / int(a))*int(b)
    return str(width) + "x" + str(int(height))    