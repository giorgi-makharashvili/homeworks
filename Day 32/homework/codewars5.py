def better_than_average(class_points, your_points):
    if sum(class_points) / (len(class_points) +1) < your_points:
        return True
    else:
        return False