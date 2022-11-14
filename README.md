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

### 1. Create an emulator
1. download Android SDK Command line tools [link](https://dl.google.com/android/repository/commandlinetools-linux-7302050_latest.zip)

Rename cmdline-tools to be tools and put it under an SDK root folder (e.g., /ssddata/yourname/SDK/android_sdk_linux). So now the tools path will be /ssddata/yourname/SDK/android_sdk_linux/tools

2. Rename cmdline-tools to be tools and put it under an SDK root folder (e.g., /ssddata/yourname/SDK/android_sdk_linux). So now the tools path will be /ssddata/yourname/SDK/android_sdk_linux/tools

3. Navigate to the SDK root and type in the following commands to install necessary files for the SDK
```
(1) tools/bin/sdkmanager --sdk_root=/ssddata/yourname/SDK/android_sdk_linux --install "system-images;android-33;google_apis;x86_64"
(2) tools/bin/sdkmanager --sdk_root=/ssddata/yourname/SDK/android_sdk_linux --install "platforms;android-33"
(3) tools/bin/sdkmanager --sdk_root=/ssddata/yourname/SDK/android_sdk_linux --install "platform-tools"
(4) tools/bin/sdkmanager --sdk_root=/ssddata/yourname/SDK/android_sdk_linux --install "emulator"
```
4. Add something into PATH

```
export ANDROID_HOME=/ssddata/yourname/SDK/android_sdk_linux
export PATH=$PATH:$ANDROID_HOME:$ANDROID_HOME/emulator:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools
export ANDROID_SDK_ROOT=$ANDROID_HOME
export ANDROID_AVD_HOME=~/.android/avd
export PATH=$PATH:$ANDROID_AVD_HOME
```

5. Create an folder under the SDK root named avds and create an Android emulator: avdmanager create avd -n emulator0 -k "system-images;android-23;google_apis;x86_64" -p avds/emulator0

6. modify the emulator configuration to change the screen size of your emulator:
In our evaluation, we set an emulator with 2GB RAM, 1GB SdCard, 1GB internal storage and 256MB heap size (the file for modification usually is: ~/.android/avd/emulator.avd/config.ini)

7. Launch the emulator: ```emulator -avd emulator0 -no-window -no-audio -wipe-data -port 5554```


### 2. Install UIAutomator2

Install uiautomator2, which is used for executing test scripts
```
pip3 install --upgrade --pre uiautomator2
```

### 3. Run ConfFix

To reproduce the experiment result, we have prepared a ```.sh``` file for each issue to run.


****
Here are links.
