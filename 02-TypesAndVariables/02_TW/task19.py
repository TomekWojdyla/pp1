a = input("Enter cube edge lenght: ")
#validation shall be made for a>=0 only and stop if condition not met
cube_edge = float(a)
cube_area = 6*cube_edge**2
cube_volume = cube_edge**3
print(f"For a cube with edge length of {cube_edge} cm area of sides equals {cube_area} cm2 and volume equals {cube_volume} cm3")