# mob-framework-radar

**Mob**ile **Framework Radar** is a tool that allows you to easily detect the mobile development framework of the mobile application it takes in input.

## Overview

Discovering the technologies of an application is one of the first steps to perform during the security analysis of a mobile application because once the development framework has been identified, it is possible to focus on the analysis of critical files of the specific framework identified.
For example, in Xamarin apps the logical part of the code is inside the DLL files, in Flutter apps the logical part is inside libapp.so, etc.
Therefore, this tool can be useful during the initial reverse engineering phase of the app to quickly recognize the framework and then proceed with the security analysis based on the identified framework.


## Usage

```
usage: mob-framework-radar.py [-h] -i INPUT [-v]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file (apk or ipa)
  -v, --verbose         Verbose mode
```

![Screenshot of mob-framework-radar](/images/screenshot.png)


## Supported frameworks

Currently mob-framework-radar is able to identify the following frameworks on Android/iOS apps:
- Flutter
- Cordova
- React Native
- Xamarin
- Capacitor
- Expo

