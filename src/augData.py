import Augmentor as ag
# the path to the fila that contains the dato to augment
path = "path/to/file"

p = ag.Pipeline(path)

# operations
p.resize(probability=1.0, width=224, height=224)
p.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
p.zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
p.flip_left_right(probability=0.5)
p.flip_top_bottom(probability=0.5)
p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
p.random_brightness(probability=0.3, min_factor=0.3, max_factor=1.2)
p.random_distortion(probability=0.4, grid_width=4, grid_height=4, magnitude=8)
p.skew(probability=0.3)

# here is the amount of resulting data
p.sample(100)

# a file named "output" will be created on the path with the results