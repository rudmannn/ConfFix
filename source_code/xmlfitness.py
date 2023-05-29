from math import sqrt

import xmlfields
import os

fields_with_random = [] # 'mContext.mIdent'
diff_k = 5

def isBooleanOrChar(tag, key_before, value_after):
    if value_after == "true" or value_after == "false" or value_after.__contains__("'"):
        return False
    # return xmlfields.getPartialOrderFields(tag, key_before)

def compareFieldDiff(tag, fields1, fields2):
    diff = {}
    global diff_k
    for key_before in fields1.keys():
        # print(key_before+" aaa "+str(key_before.count(".")))
        if key_before.count(".") > diff_k and diff_k != -1:
            # print("skip key_before::"+key_before)
            continue
        if fields2.__contains__(key_before):
            value_before = fields1[key_before]
            value_after = fields2[key_before]
            if isBooleanOrChar(tag, key_before, value_after) == False:
            # if value_after == "true" or value_after == "false":
                if value_before == value_after:
                    diff[key_before] = 0.0
                else:
                    diff[key_before] = 1.0
            else:
               diff[key_before] = abs(float(value_before) - float(value_after))
               # print("key: "+str(key_before))
               # print("value_before: "+str(value_before))
               # print("value_after: " + str(value_after))
               # print("diff[key]: "+str(diff[key_before]))

    return diff

def compareBoundDiff(tag, fields1, fields2):
    diff = {}
    for key_before in fields1.keys():
        if fields2.__contains__(key_before):
            value_before = fields1[key_before]
            value_after = fields2[key_before]
            if isBooleanOrChar(tag, key_before, value_after) == False:
            # if value_after == "true" or value_after == "false":
                if value_before == value_after:
                    diff[key_before] = 0.0
                else:
                    diff[key_before] = 1.0
            else:
               diff[key_before] = abs(float(value_before) - float(value_after))
               print(key_before)
               print(diff[key_before])

    return diff

def getOriginalFieldFitness(tag, before1, before2):
    fields_before1 = getFields(before1)
    fields_before2 = getFields(before2)
    fitness = 0.0

    diff_before = compareFieldDiff(tag, fields_before1, fields_before2)

    for key_before in diff_before:
        if abs(diff_before[key_before]) > 0.0:
            fitness += 1.0

    return fitness

def getOriginalBoundFitness(before1, before2):
    pass
    # return boundsDiffCal(before1, before2)

def getOriginalFeatureMatchingFitness(before1, before2):
    return sift_score(before1, before2)



def getFitnessByFields(tag, before1, before2, after):
    for i in range(0,5):
        fields_before1 = getFields(before1)
        fields_before2 = getFields(before2)
        fields_after = getFields(after)

        print("compare field diff_before")
        diff_before = compareFieldDiff(tag, fields_before1, fields_before2)
        print("compare field diff_after")
        diff_after = compareFieldDiff(tag, fields_before1, fields_after)
        # print("diff_before: "+str(diff_before))
        # print("diff_after: " + str(diff_after))
        total = 0
        total_diff_vars = 0

        subfitness = 0.0

        for key_before in diff_before:
            if key_before.count(".") > diff_k and diff_k != -1:
                print("skip key_before::"+key_before)
                continue
            if not fields_with_random.__contains__(key_before):
                if diff_after.__contains__(key_before):
                    total += 1
                    diff_before_value = diff_before[key_before]
                    diff_after_value = diff_after[key_before]
                    # print("key: "+str(key_before))
                    # print("diff_before_value:" + str(diff_before_value))
                    # print("diff_after_value:" + str(diff_after_value))
                    if diff_after_value == 0.0 and diff_before_value == 0.0:
                        subfitness += 0.0
                    else:
                        if diff_after_value > diff_before_value:
                            # print("value after > value before")
                            # print(key_before)
                            subfitness += 1.0
                        else:
                            # print("key_before: "+str(key_before))
                            subfitness += abs(diff_after_value/diff_before_value)
                        total_diff_vars += 1

        if total_diff_vars == 0:
            # subfitness = 1.0
            continue
            # return subfitness
        subfitness = subfitness / total_diff_vars
        return subfitness
    return 1.0

def getFields(path):
    fields_dict = {}
    with open(path, 'r') as f:
        for line in f.readlines():
            field = line.split(" = ")[0]
            value = line.split(" = ")[1].strip()
            fields_dict[field] = value
    return fields_dict



def sift_score(filename1, filename2):
    if os.path.exists(filename1) == False or os.path.exists(filename2) == False:
        return 0.0
    return 1.0

# def boundsDiffCal(boundsBasePara, boundsTestPara):
#     return abs(boundsBasePara[0] - boundsTestPara[0]) + abs(boundsBasePara[1] - boundsTestPara[1]) + \
#            abs(boundsBasePara[2] - boundsTestPara[2]) + abs(boundsBasePara[3] - boundsTestPara[3])

def getFitnessByFeatureMatching(before, after):
    return sift_score(before, after)


def getDistanceBetweenPoints(x1,x2,y1,y2):
    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))


def getNeighbors(resId, viewHierarchy, distance):
    ret = []
    lines = []
    with open(viewHierarchy, 'r') as f:
        lines = f.readlines()
    pos = -1
    for i in range(0, len(lines)):
        if lines[i].__contains__("res-name="+resId+', '):
            pos = i
            break
    if pos == -1:
        print('No res-name was found')
        return None

    # inspect parent of fromElement
    lenlen = len(lines[pos].split('+')[1].split('>')[0])
    for i in range(pos-1, -1, -1):
        if lines[i].startswith('+'):
            slash = lines[i].split('+')[1].split('>')[0]
            if len(slash) == lenlen-1:
                ret.append("PARENT:"+lines[i])
                lenlen = lenlen-1
                if lenlen <= len(lines[pos].split('+')[1].split('>')[0])-distance:
                    break

    # inspect children of fromElement
    lenlen = len(lines[pos].split('+')[1].split('>')[0])
    for i in range(pos+1, len(lines)):
        if lines[i].startswith('+'):
            slash = lines[i].split('+')[1].split('>')[0]
            if len(slash) == lenlen + 1:
                ret.append("CHILDREN:"+lines[i])
                lenlen = lenlen + 1
                if lenlen >= len(lines[pos].split('+')[1].split('>')[0]) - distance:
                    break

    # inspect siblings of fromElement
    lenlen = len(lines[pos].split('+')[1].split('>')[0])
    for i in range(pos + 1, len(lines)):
        if lines[i].startswith('+'):
            slash = lines[i].split('+')[1].split('>')[0]
            if len(slash) == lenlen:
                ret.append("SIBLING:"+lines[i])
            elif len(slash) < lenlen:
                break

    for i in range(pos - 1, 0, -1):
        if lines[i].startswith('+'):
            slash = lines[i].split('+')[1].split('>')[0]
            if len(slash) == lenlen:
                ret.append("SIBLING:"+lines[i])
            elif len(slash) < lenlen:
                break

    for r in ret:
        print(r)

    print()

    return ret


def getBoundsByEspresso(resId, viewHierarchy):
    ret = []
    with open(viewHierarchy, 'r') as f:
        for line in f.readlines():
            if line.__contains__('res-name='+str(resId)+','):
                ret.append(float(line.split(' x=')[1].split(', ')[0].replace('}','')))
                ret.append(float(line.split(' y=')[1].split(', ')[0].replace('}','')))
                ret.append(float(line.split(' width=')[1].split(', ')[0].replace('}','')))
                ret.append(float(line.split(' height=')[1].split(', ')[0].replace('}','')))
    return ret


def equalResId(nRes, nTest):
    return getResId(nRes) != None and getResId(nTest) != None and getResId(nRes) == getResId(nTest)


def getResId(nRes):
    if nRes.__contains__(" res-name") == False:
        return None
    return nRes.split(" res-name=")[1].split(',')[0]


def getFitnessByDOM(resId, before, after):
    W1 = 1.0
    W2 = 2.0
    W3 = 0.5

    # get coordinates from reference browser
    rectERef = getBoundsByEspresso(resId, before)
    try:
        eRefx1 = rectERef[0]
        eRefy1 = rectERef[1]
        eRefx2 = rectERef[0] + rectERef[2]
        eRefy2 = rectERef[1] + rectERef[3]
    except IndexError:
        print("cannot find a view in the current view. Terminate!")
        exit(0)

    # get coordinates from test browser
    rectETest = getBoundsByEspresso(resId, after)
    eTestx1 = rectETest[0]
    eTesty1 = rectETest[1]
    eTestx2 = rectETest[0] + rectETest[2]
    eTesty2 = rectETest[1] + rectETest[3]

    # distance between top left and bottom right of current element
    diffLocationTopLeft = getDistanceBetweenPoints(eTestx1, eRefx1, eTesty1, eRefy1)
    diffLocationBottomRight = getDistanceBetweenPoints(eTestx2, eRefx2, eTesty2, eRefy2)
    ePos = (diffLocationTopLeft + diffLocationBottomRight)

    # distance between diagonal of current element
    eSize = abs(rectERef[2] - rectETest[2]) + abs(rectERef[3] - rectETest[3])

    # get DOM neighbours
    neighborsRes = getNeighbors(resId, before, 2)
    neighborsTest = getNeighbors(resId, after, 2)

    # distance between top left and bottom right corners of neighbour in ref and test browsers
    neighborhoodScore = 0.0
    nPos = 0.0
    if len(neighborsTest) > 0:
        for nRes in neighborsRes:
            for nTest in neighborsTest:
                if equalResId(nRes, nTest):
                    nResId = getResId(nRes)
                    nTestId = getResId(nTest)
                    nRefRect = getBoundsByEspresso(nResId, before)
                    nTestRect = getBoundsByEspresso(nTestId, after)

                    nTL = getDistanceBetweenPoints(nRefRect[0], nTestRect[0], nRefRect[1], nTestRect[1])
                    nBR = getDistanceBetweenPoints((nRefRect[0] + nRefRect[2]), (nTestRect[0] + nTestRect[2]),
                                                   (nRefRect[1] + nRefRect[3]), (nTestRect[1] + nTestRect[3]))
                    neighborTLBRDist = (nTL + nBR)
                    neighborhoodScore = neighborhoodScore + neighborTLBRDist
        nPos = neighborhoodScore
    fitnessScore = (W1 * ePos) + (W2 * eSize) + (W3 * nPos)
    print("ePos = " + str(ePos))
    print("eSize = " + str(eSize))
    print("nPos = " + str(nPos))
    print("Local fitness score = " + str(fitnessScore))
    if ePos == 0.0 and eSize == 0.0:
        print("ePos and eSize == 0, hence fitness score set to 0")
        fitnessScore = 0.0

    return fitnessScore


def calculateK(fields1, fields2):
    for key_before in fields1.keys():
        if fields2.__contains__(key_before):
            value_before = fields1[key_before]
            value_after = fields2[key_before]
            if value_before != value_after:
                if str(key_before).endswith('.mGravity'):
                    continue
                global diff_k
                if str(key_before).__contains__("."):
                    diff_k = min(str(key_before).count("."), diff_k)
                    break
                else:
                    diff_k = 0
                    break
    print("diff_k:::"+str(diff_k))
