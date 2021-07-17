total = 0
for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    total = total + angle
print('The drunk pirate’s heading is', total % 360, 'degree.')
