"""

    script to return a single hex color

"""

def hex_to_rgb(hexa):
    return tuple(int(hexa[i:i+2], 16)  for i in (0, 2, 4))

def main(color,wallpaper):
    
    from haishoku.haishoku import Haishoku

    colors = Haishoku.getPalette(wallpaper)
    
    color_length = colors.__len__()

    if color == "all":

        r = 0
        g = 0 
        b = 0

        for color in colors:

            r+= color[1][0]
            g+= color[1][1]
            b+= color[1][2]

        r //= color_length
        g //= color_length
        b //= color_length

        return '#{:02x}{:02x}{:02x}'. format(r, g, b)


    selected_color = colors[ int(color) > color_length and color_length-1 or int(color) ]

    r = selected_color[1][0]
    g = selected_color[1][1]
    b = selected_color[1][2]

    return '#{:02x}{:02x}{:02x}'. format(r, g, b)
    
