# ConfFix

This repository contains the ConfFix tool, the evaluation detail and the benchmark of real-world configuration compatibility issues, which are available in three separate folders: tool and source code, evaluation, and DataSet.

# How ConfFix works
We give the video clip on how ConfFix repairs configuration compatibility issues provided in our motivating example.

# ConfFix benchmark

The benchmark now contains 81 reproducible CC issues.
For each issue, we provide:

* The issue report

* An executable APK that can reproduce the issue

* A bug-reproducing script and the reproduction steps

* The app source code with respect to each issue

# Build and Use ConfFix from Scratch

## Prerequisite

* UIAutomator2
* Python 3
* Android emulators at target API levels (e.g., API level 33)

## Steps

1. create an Android emulator by using [avdmanager](https://developer.android.com/studio/command-line/avdmanager) (see [this link](https://stackoverflow.com/questions/43275238/how-to-set-system-images-path-when-creating-an-android-avd)).

2. (optional) modify the emulator configuration to ensure optimal testing performance of testing tools:
In our evaluation, we set an emulator with 2GB RAM, 1GB SdCard, 1GB internal storage and 256MB heap size (the file for modification usually is: ~/.android/avd/Android7.1.avd/config.ini)

3. install uiautomator2, which is used for executing test scripts

```
pip3 install --upgrade --pre uiautomator2
```

****
Here are links.
