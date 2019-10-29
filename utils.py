def image_to_pixmap(image):
    return QPixmap.fromImage(ImageQt.ImageQt(image))


def deg_to_rad(angle):
    return angle * pi / 180


def angle_part_of_circle(part):
    return 2 * pi / part


def decart_to_image_coords(coords, image_size):
    return (image_size[0] // 2 + coords[0], image_size[1] // 2 - coords[1])


def strings_to_dict(strings, separator):
    return {string.split(separator)[0]: string.split(separator)[1] for string in strings}


def point_on_circle(center_coords, radius, angle):
    return (round(center_coords[0] + radius * sin(angle)),
            round(center_coords[1] + radius * cos(angle)))


def check_coords(coords, new_coords, max_coords):
    return (0 <= coords[0] <= max_coords[0] and
            0 <= coords[1] <= max_coords[1]) or \
        (0 <= new_coords[0] <= max_coords[0] and
         0 <= new_coords[1] <= max_coords[1])
