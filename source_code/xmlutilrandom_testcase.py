import subprocess

from lxml import etree
import uiautomator2 as u2
import datetime
import random
import xmlfitness
import sys
import xmlattr
import os

import xmltestcasedriver

randomNum = str(random.randint(100, 8000))
xmlBase = './xml_base.xml'
imageBase = './image_base.png'
appProjectPath = "./tmps/app-debug"+randomNum+"/"
xmlPath = appProjectPath+"res/layout/activity_main.xml"
signedApkPath = "./tmps/signed"+randomNum+".apk"
before1 = "./tmps/"+randomNum+"before1.txt"
before1_1 = "./tmps/"+randomNum+"before1_1.txt"
before2 = "./tmps/"+randomNum+"before2.txt"
after = "./tmps/"+randomNum+"after.txt"
apkPath = ""
apkRootPath = ""
baseDeviceId = 'emulator-5558'
appId = 'com.example.myapplication'
activityName = 'com.example.myapplication.MainActivity'
resId = 'messageText'
appProjectRootPath = appProjectPath
appProjectName = "app-debug"
lineNum = 2
currentBoundFitness = 9999999
bboundsBase = None
bboundsTest = None
optimalAttrValue = {}
optimalFitness = {}
optimalAttrImprovement = {}

optimalCombinationFitness = 999999
optimalCombinationFitnessAttributes = {}
xmlElemTag = ""
issueInducingAttribute = ""
testApkPath = ""
dataformat = ""
testMethod = ""
testApkPackage = ""
originalXmlElem = None

def xmlElementByLineNum(xmlRoot, lineNum):
    for element in xmlRoot.iter():
        if element.sourceline == lineNum:
            return element
    return None

def xmlElementById(xmlRoot, id):
    for element in xmlRoot.iter():
        attribDic = element.attrib
        for key in attribDic.keys():
            if str(key).endswith('}id'):
                attribValue = str(attribDic[key])
                if attribValue.__contains__("@id") and attribValue.endswith("/"+str(id)):
                    return element
    # in case when id does not exists
    return None

def boundsDiffCal(boundsBasePara, boundsTestPara):
    return abs(boundsBasePara[0] - boundsTestPara[0]) + abs(boundsBasePara[1] - boundsTestPara[1]) + \
           abs(boundsBasePara[2] - boundsTestPara[2]) + abs(boundsBasePara[3] - boundsTestPara[3])

def evaluateCandidateFix(xmlElem, attribute, param, filePath, appProjectRootPath,appProjectName, deviceId):
    xmlElem.set(attribute, param)
    xmlRoot.write(filePath)
    buildSignedApk(appProjectRootPath,appProjectName)
    # run the signed apk file
    pass

def removeAttribute(xmlElem, attributes, filePath, appProjectRootPath, appProjectName, deviceId):
    for attribute in attributes:
        xmlElem.attrib.pop(attribute)
    xmlRoot.write(filePath)
    buildSignedApk(appProjectRootPath, appProjectName)
    pass

def producingCandidateFix(mode, xmlRoot, xmlElem, attribute, filePath, appProjectRootPath,appProjectName, deviceId):
    print("produce candidate fix for "+attribute)
    if xmlElem.attrib.keys().__contains__(attribute):
        print("the attribute has been used in the XML element, skip it.")
        return

    currentValue = 0
    maxStep = 0
    step = 1
    positiveDirection = True
    suboptimalFitness = 9999999
    suboptimalAttributeValue = 0

    if mode == "dimension":
        # use dimen attr values
        if len(dimenAttrValues) > 0:
            print("dimenAttrValues > 0")
            for dimenAttrValue in dimenAttrValues:
                if str(dimenAttrValue).endswith("sp") == False and str(dimenAttrValue).endswith("dp") == False and str(dimenAttrValue).endswith("dip") == False:
                    print("dimen: "+str(dimenAttrValue)+" not valid, continue.")
                    continue
                originalXmlElem = xmlElem
                evaluateCandidateFix(xmlElem, attribute, str(dimenAttrValue), filePath, appProjectRootPath,
                                     appProjectName,
                                     deviceId)
                test_case(deviceId, signedApkPath, "after")
                try:
                    fitness = xmlfitness.getFitnessByFields(xmlElemTag, before1, before2, after)
                except FileNotFoundError:
                    continue
                print("currentValue:: " + str(dimenAttrValue))
                print("fitness:: " + str(1-fitness))
                if fitness < suboptimalFitness:
                    suboptimalFitness = fitness
                    suboptimalAttributeValue = dimenAttrValue
                    print("suboptimalFitness:: " + str(1-suboptimalFitness))
                    print("suboptimalAttribute:: " + str(attribute))
                    print("suboptimalAttributeValue:: " + str(suboptimalAttributeValue))
                    if suboptimalFitness < 0.1:
                        print("find a good fix already and the process terminates")
                        endtime = datetime.datetime.now()
                        print("running time: " + str((endtime - starttime).seconds))
                        # clean()
                        exit(0)
                xmlElem = originalXmlElem
                xmlRoot.write(filePath)

        if suboptimalFitness >= 0.0:
            suboptimalFitness = 9999999
            suboptimalAttributeValue = 0
            for i in range(0, 20):
                print("round :: "+str(i))
                print("maxStep :: "+str(maxStep))
                if maxStep >= 5:
                    break
                elif maxStep == 2 and suboptimalFitness == 1.0:
                    break
                if positiveDirection:
                    beforeValue = currentValue
                    currentValue = currentValue + random.randint(1, step)
                    # currentValue = 20
                    evaluateCandidateFix(xmlElem, attribute, str(currentValue) + "sp", filePath, appProjectRootPath, appProjectName, deviceId)
                    test_case(deviceId, signedApkPath, "after")
                    try:
                        fitness = xmlfitness.getFitnessByFields(xmlElemTag, before1, before2, after)
                    except FileNotFoundError:
                        continue
                    print("currentValue:: " + str(currentValue))
                    print("fitness:: " + str(1-fitness))
                    if fitness < suboptimalFitness:
                        suboptimalFitness = fitness
                        suboptimalAttributeValue = currentValue
                        print("positive")
                        print("suboptimalFitness:: " + str(1-suboptimalFitness))
                        print("suboptimalAttributeValue:: " + str(suboptimalAttributeValue))
                        print("attribute:: "+str(attribute))
                        if suboptimalFitness < 0.1:
                            print("find a good fix already and the process terminates")
                            endtime = datetime.datetime.now()
                            print("running time: " + str((endtime - starttime).seconds))
                            # clean()
                            exit(0)
                        step = step * 2
                        maxStep = 0
                    else:
                        positiveDirection = False
                        #TODO added
                        currentValue = beforeValue
                        step = 1
                        maxStep = maxStep +1
                else:
                    beforeValue = currentValue
                    currentValue = currentValue + random.randint(-1 - step, -1)
                    evaluateCandidateFix(xmlElem, attribute, str(currentValue) + "sp", filePath, appProjectRootPath, appProjectName,
                                         deviceId)
                    test_case(deviceId, signedApkPath, "after")
                    fitness = xmlfitness.getFitnessByFields(xmlElemTag, before1, before2, after)
                    print("currentValue:: " + str(currentValue))
                    print("fitness:: " + str(1-fitness))

                    if fitness < suboptimalFitness:
                        suboptimalFitness = fitness
                        suboptimalAttributeValue = currentValue
                        print("suboptimalFitness:: " + str(1-suboptimalFitness))
                        print("suboptimalAttributeValue:: " + str(suboptimalAttributeValue))
                        print("attribute:: "+str(attribute))
                        if suboptimalFitness < 0.1:
                            print("find a good fix already and the process terminates")
                            endtime = datetime.datetime.now()
                            print("running time: " + str((endtime - starttime).seconds))
                            # clean()
                            exit(0)
                        step = step * 2
                        maxStep = 0
                    else:
                        positiveDirection = True
                        # TODO added
                        currentValue = beforeValue
                        step = 1
                        maxStep = maxStep + 1
        print("fitness: " + str(fitness))
    elif mode == "int":
        # use dimen attr values
        if len(intAttrValues) > 0:
            print("intAttrValues > 0")
            for intAttrValue in intAttrValues:
                evaluateCandidateFix(xmlElem, attribute, str(intAttrValue), filePath, appProjectRootPath,
                                     appProjectName,
                                     deviceId)
                test_case(deviceId, signedApkPath, "after")
                fitness = xmlfitness.getFitnessByFields(xmlElemTag, before1, before2, after)
                print("currentValue:: " + str(intAttrValue))
                print("fitness:: " + str(1-fitness))
                if fitness < suboptimalFitness:
                    suboptimalFitness = fitness
                    suboptimalAttributeValue = intAttrValue
                    print("suboptimalFitness:: " + str(1-suboptimalFitness))
                    print("suboptimalAttribute:: " + str(attribute))
                    print("suboptimalAttributeValue:: " + str(suboptimalAttributeValue))
                    if suboptimalFitness < 0.1:
                        print("find a good fix already and the process terminates")
                        endtime = datetime.datetime.now()
                        print("running time: " + str((endtime - starttime).seconds))
                        # clean()
                        exit(0)

        # avm
        for i in range(0, 16):
            print("round :: "+str(i))
            print("maxStep :: "+str(maxStep))
            if maxStep >= 5:
                break
            if positiveDirection:
                beforeValue = currentValue
                currentValue = currentValue + random.randint(1, 1 + step)
                evaluateCandidateFix(xmlElem, attribute, str(currentValue), filePath, appProjectRootPath, appProjectName, deviceId)
                test_case(deviceId, signedApkPath, "after")
                fitness = xmlfitness.getFitnessByFields(xmlElemTag, before1, before2, after)
                print("currentValue:: " + str(currentValue))
                print("fitness " + str(fitness))
                if fitness < suboptimalFitness:
                    suboptimalFitness = fitness
                    suboptimalAttributeValue = currentValue
                    print("positive")
                    print("suboptimalFitness:: " + str(1-suboptimalFitness))
                    print("suboptimalAttributeValue:: " + str(suboptimalAttributeValue))
                    print("attribute:: "+str(attribute))
                    if suboptimalFitness < 0.1:
                        print("find a good fix already and the process terminates")
                        endtime = datetime.datetime.now()
                        print("running time: " + str((endtime - starttime).seconds))
                        # clean()
                        exit(0)
                    step = step * 2
                    maxStep = 0
                else:
                    positiveDirection = False
                    #TODO added
                    currentValue = beforeValue
                    step = 1
                    maxStep = maxStep +1
            else:
                beforeValue = currentValue
                currentValue = currentValue + random.randint(-1 - step, -1)
                evaluateCandidateFix(xmlElem, attribute, str(currentValue), filePath, appProjectRootPath, appProjectName,
                                     deviceId)
                test_case(deviceId, signedApkPath, "after")
                fitness = xmlfitness.getFitnessByFields(xmlElemTag, before1, before2, after)
                print("currentValue:: " + str(currentValue))
                print("fitness:: " + str(1-fitness))

                if fitness < suboptimalFitness:
                    suboptimalFitness = fitness
                    suboptimalAttributeValue = currentValue
                    print("suboptimalFitness:: " + str(1-suboptimalFitness))
                    print("suboptimalAttributeValue:: " + str(suboptimalAttributeValue))
                    print("attribute:: "+str(attribute))
                    if suboptimalFitness < 0.1:
                        print("find a good fix already and the process terminates")
                        endtime = datetime.datetime.now()
                        print("running time: " + str((endtime - starttime).seconds))
                        # clean()
                        exit(0)
                    step = step * 2
                    maxStep = 0
                else:
                    positiveDirection = True
                    # TODO added
                    currentValue = beforeValue
                    step = 1
                    maxStep = maxStep + 1
        print("fitness: " + str(fitness))

    elif mode == "color":
        # obtain all color data format attribute values in the current XML file.
        if len(colorAttrValues) > 0:
            for drawableAttrValue in colorAttrValues:
                originalXmlElem = xmlElem
                evaluateCandidateFix(xmlElem, attribute, str(drawableAttrValue), filePath, appProjectRootPath,
                                     appProjectName,
                                     deviceId)
                test_case(deviceId, signedApkPath, "after")
                fitness = xmlfitness.getFitnessByFields(xmlElemTag, before1, before2, after)
                print("currentValue:: " + str(drawableAttrValue))
                print("fitness:: " + str(1-fitness))
                if fitness < suboptimalFitness:
                    suboptimalFitness = fitness
                    suboptimalAttributeValue = drawableAttrValue
                    print("suboptimalFitness:: " + str(1-suboptimalFitness))
                    print("suboptimalAttribute:: " + str(attribute))
                    print("suboptimalAttributeValue:: " + str(suboptimalAttributeValue))
                    if suboptimalFitness < 0.1:
                        print("find a good fix already and the process terminates")
                        endtime = datetime.datetime.now()
                        print("running time: " + str((endtime - starttime).seconds))
                        # clean()
                        exit(0)
                xmlElem = originalXmlElem
                xmlRoot.write(filePath)

    elif mode == "drawable":
        # obtain all color data format attribute values in the current XML file.
        if len(drawableAttrValues) > 0:
            for drawableAttrValue in drawableAttrValues:
                evaluateCandidateFix(xmlElem, attribute, str(drawableAttrValue), filePath, appProjectRootPath,
                                     appProjectName,
                                     deviceId)
                test_case(deviceId, signedApkPath, "after")
                fitness = xmlfitness.getFitnessByFields(xmlElemTag, before1, before2, after)
                print("currentValue:: " + str(drawableAttrValue))
                print("fitness:: " + str(1-fitness))
                if fitness < suboptimalFitness:
                    suboptimalFitness = fitness
                    suboptimalAttributeValue = drawableAttrValue
                    print("suboptimalFitness:: " + str(1-suboptimalFitness))
                    print("suboptimalAttribute:: " + str(attribute))
                    print("suboptimalAttributeValue:: " + str(suboptimalAttributeValue))
                    if suboptimalFitness < 0.1:
                        print("find a good fix already and the process terminates")
                        endtime = datetime.datetime.now()
                        print("running time: " + str((endtime - starttime).seconds))
                        # clean()
                        exit(0)
    elif mode == "enum":
        evaluateCandidateFix(xmlElem, attribute, str(globAttrValue), filePath, appProjectRootPath,
                             appProjectName,
                             deviceId)
        test_case(deviceId, signedApkPath, "after")
        fitness = xmlfitness.getFitnessByFields(xmlElemTag, before1, before2, after)
        print("currentValue:: " + str(globAttrValue))
        print("fitness:: " + str(1 - fitness))
        if fitness < suboptimalFitness:
            suboptimalFitness = fitness
            suboptimalAttributeValue = globAttrValue
            print("suboptimalFitness:: " + str(1 - suboptimalFitness))
            print("suboptimalAttribute:: " + str(attribute))
            print("suboptimalAttributeValue:: " + str(suboptimalAttributeValue))
            if suboptimalFitness < 0.1:
                print("find a good fix already and the process terminates")
                endtime = datetime.datetime.now()
                print("running time: " + str((endtime - starttime).seconds))
                # clean()
                exit(0)

    #TODO fitness function
    if xmlElem.attrib.keys().__contains__(attribute):
        if mode == "dimension":
            optimalAttrValue[attribute] = str(suboptimalAttributeValue)+"sp"
        else:
            optimalAttrValue[attribute] = suboptimalAttributeValue
        optimalFitness[attribute] = suboptimalFitness
        xmlElem.attrib.pop(attribute)
    pass


def producingCandidateFixes(xmlRoot, xmlElem, attributeName, filePath, appProjectRootPath,appProjectName, deviceId):
    # dimension attribute
    if dataformat == "dimension":
        attributes = xmlattr.getDimensionalAttributes(xmlElemTag)
        # random.shuffle(attributes)
        for attribute in attributes:
            print("attribute: "+attribute)
            producingCandidateFix("dimension", xmlRoot, xmlElem, attribute, filePath, appProjectRootPath,appProjectName, deviceId)
    elif dataformat == "enum":
        attributes = [str(str(attributeName[0]).replace('res/android', 'res-auto'))]
        for attribute in attributes:
            print("attribute: "+attribute)
            producingCandidateFix("enum", xmlRoot, xmlElem, attribute, filePath, appProjectRootPath,appProjectName, deviceId)
    # integer attributes
    elif dataformat == "int":
        attributes = xmlattr.getIntAttributes(xmlElemTag)
        if attributes is None or len(attributes) == 0:
            print('no issue-fixing attributes, terminates!')
            endtime = datetime.datetime.now()
            print("running time: " + str((endtime - starttime).seconds))
            exit(0)
        for attribute in attributes:
            print("attribute: " + attribute)
            producingCandidateFix("int", xmlRoot, xmlElem, attribute, filePath, appProjectRootPath, appProjectName,
                                  deviceId)

    # # float attributes
    elif dataformat == "float":
        attributes = xmlattr.getFloatAttributes(xmlElemTag)
        for attribute in attributes:
            print("attribute: " + attribute)
            producingCandidateFix("float", xmlRoot, xmlElem, attribute, filePath, appProjectRootPath, appProjectName,
                                  deviceId)

    # # boolean attributes
    elif dataformat == "boolean":
        attributes = xmlattr.getBooleanAttributes(xmlElemTag)
        for attribute in attributes:
            print("attribute: " + attribute)
            producingCandidateFix("boolean", xmlRoot, xmlElem, attribute, filePath, appProjectRootPath, appProjectName,
                                  deviceId)

    # color attributes
    elif dataformat == "color":
        attributes = xmlattr.getColorAttributes(xmlElemTag)
        for attribute in attributes:
            print("attribute: " + attribute)
            producingCandidateFix("color", xmlRoot, xmlElem, attribute, filePath, appProjectRootPath, appProjectName, deviceId)

    # drawable attributes
    elif dataformat == "drawable":
        attributes = xmlattr.getDrawableAttributes(xmlElemTag)
        print("tag: "+xmlElemTag)
        for attribute in attributes:
            print("attribute: " + attribute)
            producingCandidateFix("drawable", xmlRoot, xmlElem, attribute, filePath, appProjectRootPath, appProjectName, deviceId)

def install_test_apk(deviceId):
    print("begin installing test apk")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_install(testApkPath)
    d.sleep(1)
    print("test apk has been installed")

def uninstall_test_apk(deviceId):
    print("begin installing test apk")
    d = u2.connect(deviceId)
    d.screen_on()
    d.app_uninstall(testApkPath)
    print("test apk has been uninstalled")

def producingBaselines(xmlRoot, xmlElem, attributeNames, filePath, appProjectRootPath, appProjectName, deviceId):
    install_test_apk(deviceId)
    # removing randomness
    print("building fields_with_random")
    test_case(deviceId, signedApkPath, "before1")
    test_case(deviceId, signedApkPath, "before1_1")
    fields_before1 = xmlfitness.getFields(before1)
    fields_before1_1 = xmlfitness.getFields(before1_1)
    b11diff = xmlfitness.compareFieldDiff(xmlElemTag, fields_before1, fields_before1_1)
    for k in b11diff.keys():
        if b11diff[k] != 0.0:
            xmlfitness.fields_with_random.append(k)
    print("fields_with_random: "+str(xmlfitness.fields_with_random))

    # removing attribute
    removeAttribute(xmlElem, attributeNames, filePath, appProjectRootPath, appProjectName, deviceId)
    test_case(deviceId, signedApkPath, "before2")
    fields_before1 = xmlfitness.getFields(before1)
    fields_before2 = xmlfitness.getFields(before2)
    xmlfitness.calculateK(fields_before1, fields_before2)
    b12diff = xmlfitness.compareFieldDiff(xmlElemTag, fields_before1, fields_before2)
    nodiff = True
    for k in b12diff.keys():
        if b12diff[k] != 0.0:
            if xmlfitness.fields_with_random.__contains__(k):
                continue
            print("key:: "+k)
            nodiff = False
    if nodiff:
        print("find a fix by removing the issue-inducing attribute. Terminates!!")
        endtime = datetime.datetime.now()
        print("running time: " + str((endtime - starttime).seconds))
        exit(0)

def generateCombinationByImprovement(xmlRoot, xmlElem, attributeName, filePath, appProjectRootPath, appProjectName,
                                     deviceId):
    optimalCombinationFitness = 999999
    optimalCombinationFitnessAttributes = []
    # get attributes with maximum improvement
    maxImprovement = -1
    for key in optimalAttrImprovement.keys():
        if optimalAttrImprovement[key] > maxImprovement:
            maxImprovement = optimalAttrImprovement[key]
    # generate combinations of attributes
    for i in range(0,10):
        combinationAttributes = []
        for key in optimalAttrImprovement.keys():
            p = optimalAttrImprovement[key] / maxImprovement
            if p > 1.0:
                p = 1.0
            if p < 0.0:
                p = 0.0
            print("key: "+str(key))
            print("p: "+str(p))
            ran = random.random()
            if ran <= p:
                combinationAttributes.append(key)

        for attribute in combinationAttributes:
            xmlElem.set(attribute, optimalAttrValue[attribute])
        xmlRoot.write(filePath)
        buildSignedApk(appProjectRootPath, appProjectName)
        test_case(deviceId, signedApkPath, "after")
        print("checking attribute combination: "+str(combinationAttributes))
        fitness = xmlfitness.getFitnessByFields(xmlElemTag, before1, before2, after)
        if fitness < optimalCombinationFitness:
            optimalCombinationFitness = fitness
            optimalCombinationFitnessAttributes.clear()
            optimalCombinationFitnessAttributes.extend(combinationAttributes)
            print("suboptimal fitness score:: "+str(1-optimalCombinationFitness))
            print("suboptimal attribute combination: " + str(combinationAttributes))
        for attribute in combinationAttributes:
            xmlElem.attrib.pop(attribute)
        xmlRoot.write(filePath)

    print("optimalCombinationFitness")
    print(optimalCombinationFitness)
    print("optimalCombinationFitnessAttributes")
    print(optimalCombinationFitnessAttributes)
    pass


def producingCandidateFixesCombinations(xmlRoot, xmlElem, attributeName, filePath, appProjectRootPath, appProjectName,
                                        deviceId):
    print("optimalAttrValue")
    print(optimalAttrValue)
    print("optimalFitness")
    print(optimalFitness)
    if len(optimalFitness.keys()) == 1:
        print("terminate because only one attributes in the combination")
        endtime = datetime.datetime.now()
        print("running time: " + str((endtime - starttime).seconds))
        exit(0)

    # original fitness score
    originalFitnessScore = xmlfitness.getOriginalFieldFitness(xmlElemTag, before1, before2)

    # for each attribute, calculate the improvement
    for attrKey in optimalFitness.keys():
        optimalAttrImprovement[attrKey] = 1 - (optimalFitness[attrKey] / originalFitnessScore)
        if optimalAttrImprovement[attrKey] < 0.0:
            optimalAttrImprovement[attrKey] = 0.0
        elif optimalAttrImprovement[attrKey] > 1.0:
            optimalAttrImprovement[attrKey] = 1.0

    print("optimalAttrImprovement: "+str(optimalAttrImprovement))
    generateCombinationByImprovement(xmlRoot, xmlElem, attributeName, filePath, appProjectRootPath, appProjectName,
                                        deviceId)
    pass


def processBackwardCompatXmlElement(xmlRoot, xmlElem, attributeNames, filePath, appProjectRootPath,appProjectName, deviceId):
    producingBaselines(xmlRoot, xmlElem, attributeNames, filePath, appProjectRootPath,appProjectName, deviceId)
    producingCandidateFixes(xmlRoot, xmlElem, attributeNames, filePath, appProjectRootPath,appProjectName, deviceId)
    producingCandidateFixesCombinations(xmlRoot, xmlElem, attributeNames, filePath, appProjectRootPath,appProjectName, deviceId)

def processXmlElement(xmlRoot, xmlElem, attributeNames, filePath, appProjectRootPath,appProjectName, deviceId):
    processBackwardCompatXmlElement(xmlRoot, xmlElem, attributeNames, filePath, appProjectRootPath,appProjectName, deviceId)

def test_case(deviceId, apkPath, mode):
    install_test_apk(deviceId)
    print("begin executing test case")
    d = u2.connect(deviceId)
    d.screen_on()
    print("apkPath: "+str(apkPath))
    try:
        testcase_starttime = datetime.datetime.now()
        d.app_install(apkPath)

        # temporary close the uiautomator service
        d.uiautomator.stop()
        print("uiautomator service is temporarily closed to avoid crash")
        d.sleep(1)

        try:
            cmd = "$ANDROID_HOME/platform-tools/adb -s "+deviceId+" shell am instrument -w -m -e debug false -e class '"+testMethod+"' "+testApkPackage+"/androidx.test.runner.AndroidJUnitRunner"
            print("cmd:::"+cmd)
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            stdoutdata, stderrdata = p.communicate()
            # print("return_code: "+str(stdoutdata))
            # print("return_code: "+str(return_code))
        except subprocess.TimeoutExpired:
            print("timeout???")
            pass

        d.sleep(1)
        print("the test apk has finished running.")

        d.uiautomator.start()
        print("uiautomator service starts again")

        # use the command line to obtain the field information
        if mode == "before1":
            cmd = "$ANDROID_HOME/platform-tools/adb -s "+deviceId+" shell \"run-as "+appId+" cat /data/user/0/"+appId+"/files/fitness_out.txt\" > "+before1
            print("cmd: "+cmd)
        if mode == "before1_1":
            cmd = "$ANDROID_HOME/platform-tools/adb -s " + deviceId + " shell \"run-as " + appId + " cat /data/user/0/" + appId + "/files/fitness_out.txt\" > " + before1_1
            print("cmd: " + cmd)
        elif mode == "before2":
            cmd = "$ANDROID_HOME/platform-tools/adb -s "+deviceId+" shell \"run-as "+appId+" cat /data/user/0/"+appId+"/files/fitness_out.txt\" > "+before2
            print("cmd: " + cmd)
        elif mode == "after":
            cmd = "$ANDROID_HOME/platform-tools/adb -s "+deviceId+" shell \"run-as "+appId+" cat /data/user/0/"+appId+"/files/fitness_out.txt\" > "+after
            print("cmd: " + cmd)

        p = subprocess.Popen(cmd, shell=True)
        return_code = p.wait()
        print("return_code: "+str(return_code))
        print("the field information has been extracted.")
        d.app_uninstall(appId)
        testcase_endtime = datetime.datetime.now()
        print("test case execution time:: "+str((testcase_endtime - testcase_starttime).seconds))
    except RuntimeError as e:
        if mode == "before1" or mode == "before2":
            print('terminate due to a runtime error for building before1.txt or before2.txt')
            print(e)
            exit(0)
        else:
            print('skip installing due to a runtime error by APK file'+str(e))

def buildSignedTestApk(apk_path):
    generated_aligned_apk_path = str(apk_path).replace('.apk','_aligned.apk')
    generated_aligned_signed_path = str(apk_path).replace('.apk', '_signed.apk')
    cmd = "$BUILD_TOOL_ROOT/zipalign -f -v 4 " + apk_path + " " + generated_aligned_apk_path + " & " +\
          "$BUILD_TOOL_ROOT/apksigner sign --ks ./debug.keystore --ks-key-alias key1 --ks-pass pass:android "+\
          "--out " + generated_aligned_signed_path + " \""+\
          generated_aligned_apk_path + "\""
    print("sign test apk cmd::::"+cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    return_code = p.wait()
    print("return_code: " + str(return_code))

def buildSignedApk(appProjectRootPath, appProjectName):
    build_signed_apk_start_time = datetime.datetime.now()
    appProjectPath = appProjectRootPath
    cmd = "cd "+appProjectPath+" & cd .. & java -jar ./apktool.jar b --use-aapt2 " + appProjectPath + " -o "+appProjectPath+"/dist/app-debug.apk && cd .."
    print("cmd: " + str(cmd))
    p = subprocess.Popen(cmd, shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))
    # sign the generated apk file
    testApkPath = signedApkPath
    generated_apk_path = appProjectPath+"dist/"+appProjectName+".apk"
    generated_aligned_apk_path = appProjectPath + "dist/" + appProjectName + "_aligned.apk"

    p = subprocess.Popen("$BUILD_TOOL_ROOT/zipalign -f -v 4 "+generated_apk_path+" "+generated_aligned_apk_path+" & "
                         "$BUILD_TOOL_ROOT/apksigner sign --ks ./debug.keystore --ks-key-alias key1 --ks-pass pass:android "
                         "--out " + testApkPath + " \""
                         + generated_aligned_apk_path + "\"", shell=True, stdout=subprocess.PIPE)

    return_code = p.wait()
    print("return_code: " + str(return_code))
    build_signed_apk_end_time = datetime.datetime.now()
    print("apk repackaging time:: "+str((build_signed_apk_end_time-build_signed_apk_start_time).seconds))

def clean():
    print("perform file cleaning")
    cmd = "rm -r ./tmps/*"
    p = subprocess.Popen(cmd, shell=True)
    return_code = p.wait()
    print("return_code: " + str(return_code))


def xmlElementByAttributes(xmlRoot, issueInducingAttribute):
    for element in xmlRoot.iter():
        attribDic = element.attrib
        for key in attribDic.keys():
            keystr = str(key).split('}')[1]
            if issueInducingAttribute.__contains__(keystr):
                return element
    return None


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    baseDeviceId = sys.argv[1]
    testDeviceId = sys.argv[2]
    apkPath = sys.argv[3]
    xmlPath = appProjectPath+sys.argv[4]
    xmlElemTag = sys.argv[5]
    issueInducingAttribute = sys.argv[6]
    dataformat = sys.argv[7]
    testApkPath = sys.argv[8]
    testMethod = sys.argv[9]
    testApkPackage = sys.argv[10]
    appId = sys.argv[11]
    resId = sys.argv[12]

    buildSignedTestApk(testApkPath)
    testApkPath = str(testApkPath).replace('.apk','_signed.apk')
    cmd = "cd "+apkRootPath+" & java -jar ./apktool.jar d -s -f "+apkPath+" -o " \
          ""+appProjectPath
    print("cmd: " + str(cmd))
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return_code = p.wait()
    print("return_code: "+str(return_code))
    xmlRoot = etree.parse(xmlPath)
    xmlRoot.write(xmlPath)
    # try:
    buildSignedApk(appProjectRootPath,appProjectName)
    endtime = datetime.datetime.now()
    # # by line num
    # print("lineNum: "+str(lineNum))

    intAttrValues = []
    dimenAttrValues = []
    colorAttrValues = []
    drawableAttrValues = []

    xmlRoot = etree.parse(xmlPath)
    xmlElem = xmlElementById(xmlRoot, resId)
    if xmlElem == None:
        xmlElem = xmlElementByAttributes(xmlRoot, issueInducingAttribute)
    print("xmlElem: " + str(xmlElem))
    if xmlElem == None:
        print("Cannot locate the XML element, terminate!!")
        exit(0)
    attrValue = None
    global globAttrValue
    globAttrValue = ""
    for attr in xmlElem.attrib:
        if str(attr).endswith(issueInducingAttribute):
            attrValue = xmlElem.attrib[attr]
            globAttrValue = str(attrValue)
            intAttrValues.append(str(attrValue))
            dimenAttrValues.append(attrValue)
            colorAttrValues.append(attrValue)
            drawableAttrValues.append(attrValue)
        else:
            if str.isdigit(str(attrValue)):
                intAttrValues.append(str(attrValue))
            if str(attrValue).startswith("@dimen") or str(attrValue).endswith("sp"):
                if not dimenAttrValues.__contains__(attrValue):
                    dimenAttrValues.append(attrValue)
            if str(attrValue).startswith("@color") or str(attrValue).startswith("#"):
                if not colorAttrValues.__contains__(attrValue):
                    colorAttrValues.append(attrValue)
            if str(attrValue).startswith("@drawable"):
                drawableAttrValues.append(attrValue)

    print("colorAttrValue: " + str(colorAttrValues))
    # get int attribute values
    # for element in xmlRoot.iter():
    #     for attr in element.attrib:
    #         attrValue = element.attrib[attr]
    #         if str.isdigit(str(attrValue)):
    #             intAttrValues.append(attrValue)
    # print(intAttrValues)
    #
    # # get dimension attribute values
    # for element in xmlRoot.iter():
    #     for attr in element.attrib:
    #         attrValue = element.attrib[attr]
    #         if attr == issueInducingAttribute:
    #             if not dimenAttrValues.__contains__(attrValue):
    #                 dimenAttrValues.append(attrValue)
    #         if str(attrValue).startswith("@dimen") or str(attrValue).endswith("sp"):
    #             if not dimenAttrValues.__contains__(attrValue):
    #                 dimenAttrValues.append(attrValue)
    # print(dimenAttrValues)
    #
    # # get color attribute values
    # for element in xmlRoot.iter():
    #     for attr in element.attrib:
    #         attrValue = element.attrib[attr]
    #         if str(attr).endswith(issueInducingAttribute):
    #             if not colorAttrValues.__contains__(attrValue):
    #                 colorAttrValues.append(attrValue)
    #         elif str(attrValue).startswith("@color") or str(attrValue).startswith("#"):
    #             if not colorAttrValues.__contains__(attrValue):
    #                 colorAttrValues.append(attrValue)
    # print("colorAttrValue: " + str(colorAttrValues))
    #
    # # get color attribute values
    # for element in xmlRoot.iter():
    #     for attr in element.attrib:
    #         attrValue = element.attrib[attr]
    #         if attr == issueInducingAttribute:
    #             drawableAttrValues.append(attrValue)
    #         elif str(attrValue).startswith("@drawable"):
    #             drawableAttrValues.append(attrValue)
    # print(drawableAttrValues)

    # in case multiple issue-inducing attributes, divided by "0"
    attributeNames = []
    if issueInducingAttribute.__contains__("0") == False:
        attributeNames = ["{http://schemas.android.com/apk/res/android}"+issueInducingAttribute]
    else:
        attrs = issueInducingAttribute.split("0")
        for a in attrs:
            attributeNames.append("{http://schemas.android.com/apk/res/android}"+str(a))
    processXmlElement(xmlRoot, xmlElem, attributeNames, xmlPath, appProjectRootPath,appProjectName, baseDeviceId)

    endtime = datetime.datetime.now()
    print("running time: " + str((endtime - starttime).seconds))
    # clean()

