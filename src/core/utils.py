from easy_thumbnails.files import get_thumbnailer


def responsiveImage(source, sizes=[]):
    def resize(width=0):
        thumbnail = thumbnailer.get_thumbnail({'size': (width, 0)})
        return {
            'src':  thumbnail.url,
            'w': thumbnail.width,
            'h': thumbnail.height
        }

    if not source:
        return None

    
    try:
        thumbnailer = get_thumbnailer(source)
    except:
        raise ValueError('Impossible to get thumbnailer with provided ImageField value.')

    return {
            **resize(2000),
            **{
                'srcset': (resize(width) for width in sizes)
              }
            }
