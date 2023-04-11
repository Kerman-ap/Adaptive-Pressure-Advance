#!python
import sys
import re
import os

tuningspeed = 160
pa = 0.01

sourceFile=sys.argv[1]

# Read the ENTIRE g-code file into memory
with open(sourceFile, "r") as f:
    lines = f.readlines()

#Handling file change
if (sourceFile.endswith('.gcode')):
    destFile = re.sub('\.gcode$','',sourceFile)
    try:
        os.rename(sourceFile, destFile+".sqv.bak")
    except FileExistsError:
        os.remove(destFile+".sqv.bak")
        os.rename(sourceFile, destFile+".sqv.bak")
    destFile = re.sub('\.gcode$','',sourceFile)
    destFile = destFile + '.gcode'
else:
    destFile = sourceFile
    os.remove(sourceFile)


with open(destFile, "w") as of:
    for lIndex in range(len(lines)):
        oline = lines[lIndex]
        #Skip Comments
        if ';' in oline:
            oline = oline.split(';')[0]
        # Parse gcode line
        if oline.startswith('G1') and 'F' in oline:
            speed = float(oline.split('F')[1].split(' ')[0])/60
            newpa = round(pa * (tuningspeed/speed)*100000)/100000
            of.write(oline)
            of.write(f'SET_PRESSURE_ADVANCE ADVANCE={newpa}\n')
        elif oline.startswith('SET_PRESSURE_ADVANCE'):
            of.write(oline)
            pa = float(oline.split('=')[1])
        else: #Add original line if feedrate change isn't found
            of.write(oline)


of.close()
f.close()
