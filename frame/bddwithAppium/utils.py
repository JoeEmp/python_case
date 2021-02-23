def get_size(context):
    width = context.driver.get_window_size()['width']
    height = context.driver.get_window_size()['height']
    return width, height


def swipe(context, direction='up'):
    width, height = get_size(context)
    if 'up' == direction:
        context.driver.swipe(int(width*0.2), int(height*0.75),
                             int(width*0.2), int(height*0.25), duration=300)
    elif 'down' == direction:
        context.driver.swipe(int(width*0.2), int(height*0.75),
                             int(width*0.2), int(height*0.25), duration=300)
