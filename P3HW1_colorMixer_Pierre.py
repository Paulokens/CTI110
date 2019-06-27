# CTI-110
# P3HW1 - Color Mixer
# Pierre Paul
# 06/26/2019
#

#Pseudocode
#
#input the first color.
#input the second color.
#Determine whether the first and second colors are bleu and red.
#Display the mixing result if the condition is true
#Determine whether the first and second colors are red and yellow if the first condition is false.
#Display the mixing result if the second condition is true.
#Determine whether the first and second color are bleu and yellow.
#Display the mixing result if the third condition is true.
#Displplay an error message if none of the conditions is true.

#Get the primary colors.
color1 = input("Enter the first primary color (red, blue,or yellow).")
color2 = input("Enter the second primary color (red, blue,or yellow).")

#Alternative decision structure.
if (color1 == 'red' and color2 == 'blue') or (color1 == 'blue' and color2 == 'red'):
    print('When you mix red and blue, you get purple.')

elif (color1 == 'red' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'red'):
    print('When you mix red and yellow, you get orange.')


elif (color1 == 'blue' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'blue'):
    print('When you mix blue and yellow, you get green.')


else: print('Error! You must enter two primary colors.')
