
import os
from os import stat
import time
import moment

BASEDIR = r'C:\Users\bundi\Downloads\\'

isoFiles = []
isoDirs = []
imgFormats = {".iso", ".bin"}
arcFormats = {".rar", ".zip", ".7z", ".gz"}


def dateCheck(item):
    itemTime = os.path.getatime(item)

    # itemTime =  * 1000

    # make moments

    itemMoment = moment.unix(itemTime)
    nowMoment = moment.now()

    agedSeven = moment.unix(itemTime).add(days=7)

    if agedSeven > nowMoment:
        itemSafe = True
    else:
        itemSafe = False


    print("item: ", item)
    print("atime: ", itemMoment)
    print("aged: ", agedSeven)
    print("safe: ", itemSafe)
    print("-----------------")


# Clean out old disc image files left over from decompression

# Start at top level of directory
filesOnly = os.scandir(BASEDIR)
for thisFile in filesOnly:
    if os.path.isfile(thisFile):
        if os.path.splitext(thisFile)[1] in imgFormats:
            isoFiles.append(thisFile)
            dateCheck(thisFile)
            break

# Recurse into subdirectories; flag parent for deletion
dirsOnly = os.listdir(BASEDIR)
for searchDir in os.scandir(BASEDIR):
    if os.path.isdir(searchDir):
        for seekFile in os.listdir(searchDir):
            if os.path.splitext(seekFile)[1] in imgFormats:
                dateCheck(searchDir)
                isoDirs.append(searchDir)
                break

# Scour archive files the same way, but we only have to worry about top level
filesOnly = os.scandir(BASEDIR)
for thisFile in filesOnly:
    if os.path.isfile(thisFile):
        if os.path.splitext(thisFile)[1] in arcFormats:
            dateCheck(thisFile)
