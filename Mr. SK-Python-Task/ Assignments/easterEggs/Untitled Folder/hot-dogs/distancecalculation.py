

initial_velocity = int(input(print("Enter initial velocoty: ")))

time_span = int(input(print("Enter time span: ")))

acceleration = int(input(print("Enter acceleration: ")))


time_square = time_span * time_span
acceleration_time_span = 0.5 * acceleration * time_square
distance = initial_velocity * time_span + acceleration_time_span;

print(distance, "\n")


