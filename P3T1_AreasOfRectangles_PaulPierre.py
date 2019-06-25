# Areas of Rectangles
# 06/25/2019
# CTI-110 P3T1 - Areas of Rectangles
# Pierre Paul
#

# Get the dimensions of the first rectangle.
length1 = float(input('Enter the length of the first rectangle: '))
width1 = float(input('Enter the width of the first rectangle: '))

# Get the dimensions of the second rectangle.
length2 = float(input('Enter the length of the second rectangle: '))
width2 = float(input('Enter the width of the second rectangle: '))

# Calculate the areas of the rectangles.
area1 = length1 * width1
area2 = length2 * width2

# Compare the areas.
if area1 > area2:
    print('The first rectangle has the larger area.')
else:
    if area1 < area2:
        print('The second rectangle has the larger area.')
    else:
        print('Both rectangle have equal area.')
