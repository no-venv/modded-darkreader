"""

    script to return a single hex color

"""

def hex_to_rgb(hexa):
    return tuple(int(hexa[i:i+2], 16)  for i in (0, 2, 4))

def main(color,wallpaper):
    
    import pywal

    colors = pywal.colors.get(wallpaper,backend="haishoku")
    
    if color == "all":
        rgbcolors = []

        r = 0
        g = 0 
        b = 0

        for color in colors["colors"].values():

           rgbcolors.append(hex_to_rgb(color[1:]))
        
        for color in rgbcolors:

            r+= color[0]
            g+= color[1]
            b+= color[2]

        color_len = len(rgbcolors)

        r //= color_len
        g //= color_len
        b //= color_len

        return '#{:02x}{:02x}{:02x}'. format(r, g, b)
            

    return colors["colors"]["color"+color]
    