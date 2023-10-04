"""

    script to return a single hex color

"""

def main(wallpaper):
    
    import pywal

    colors = pywal.colors.get(wallpaper)
    
    return colors["colors"]["color2"]
    