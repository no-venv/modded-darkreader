"""

    script to return a single hex color

"""

def main(color,wallpaper):
    
    import pywal

    colors = pywal.colors.get(wallpaper,backend="haishoku")
    
    return colors["colors"]["color"+color]
    