import os
import shutil

# Start range stored as key
# End range stored as value
rangedict = {
    130 : 149,
    152 : 198,
    319 : 405,
    590 : 621,
    631 : 651,
    744 : 769,
    943 : 953,
    1414 : 1462,
    1981 : 1987,
    2233 : 2265,
    2292 : 2322,
    2488 : 2517,
    2542 : 2706,
    2827 : 2840,
    2880 : 2927,
    3008 : 3068,
    3080 : 3178,
    3183 : 3315,
    3392 : 3399,
    3518 : 3540,
    3643 : 3684,
    3763 : 3767,
    3799 : 3828,
    3925 : 3954,
    3979 : 4029,
    4051 : 4065,
    4417 : 4430,
    4609 : 4663,
    4701 : 4765,
    4785 : 4801,
    4849 : 4857,
    4869 : 4882,
    4906 : 4913,
    4927 : 4959,
    5049 : 5124,
    5222 : 5259,
    5329 : 5368,
    5415 : 5439,
    5565 : 5586,
    5604 : 5626,
    5632 : 5726
}

#User Directory Name
user = 'User'

#Screenshot Folders, Add/Remove as needed
folders = [
    'BobsAngels NE 01\\', 'BobsAngles South01\\',
    'BobsAngles zero-zero\\', 'Westward Expansion 1\\',
    ]

path = (r'C:\Users\\' + user + '\AppData\Roaming\Factorio' +
        '\script-output\CTLM\Positions\position\\')

for folder in folders:
    srcpath = path + folder
    destpath = path + 'Missing' + folder
    for folderName, subfolders, filenames in os.walk(srcpath):
        for minrange in rangedict:
            maxrange = rangedict.get(minrange)
            for fhand in filenames:
                if int(fhand[:-4]) in range(minrange, maxrange):
                    try : shutil.copyfile(srcpath + fhand, destpath + fhand)
                    except FileNotFoundError: os.mkdir(destpath)
