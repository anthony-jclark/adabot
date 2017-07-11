import xml.etree.ElementTree as et
import random

tree = et.parse("baseXml.dae")
root = tree.getroot()

target = root[4][0][0][0][0]
targetText = target.text
targetSplit = targetText.split()

choicesBoth = [0.01, -0.01]
choicesPos = [0.03, 0.06, 0.09]
choicesNeg = [-0.09, -0.06, -0.003]
choices = choicesBoth
oldPoint = 0

for x in range(0, len(targetSplit) - 1):
    if (x + 1) % 3 == 0:
        newPoint = oldPoint + random.choice(choices)
        targetSplit[x] = str(newPoint)
        oldPoint = newPoint
        if newPoint > 0.5 and (choices == choicesBoth or choices == choicesPos):
            choices = choicesNeg
        if newPoint <= 0 and (choices == choicesBoth or choices == choicesNeg):
            choices = choicesPos
        if newPoint < 0.5 and newPoint > 0:
            choices = choicesBoth

target.text = ' '.join(targetSplit)
print targetSplit[2]
targetText = target.text
print targetText

tree.write('resultXml.dae')

