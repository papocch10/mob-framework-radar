#!/usr/bin/python3
import zipfile
import argparse
import re

# Command line argument parser 
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input",type=str,required=True,help="""Input file (apk or ipa)""")
parser.add_argument("-v","--verbose",action='store_true',help="""Verbose mode""")
args = parser.parse_args()

# Colors
RED = "\033[0;31m"
END = "\033[0m"

# open apk/ipa file
zip = zipfile.ZipFile(args.input)


# list files present in the installer
list_files = zip.namelist()

# mobile frameworks references
files_ref = {
  "Flutter": ['libflutter.so', 'libapp.so', 'Flutter.framework/Flutter', 'flutter_assets/kernel_blob.bin'], 
  "Cordova": ['www/cordova.js', 'www/index.html', 'www/cordova_plugins.js', 'public/cordova.js'],
  "React Native": ['libreactnativejni.so', 'assets/index.android.bundle', '/main.jsbundle', 'react-native/package.json'],
  "Expo": ['Expo.plist', 'META-INF/expo'], 
  "Xamarin": ['assemblies/Mono.Android.dll', 'mscorlib.dll', 'Mono.Security.dll', 'Xamarin.iOS.dll', 'libxamarin-app.so', 'libmonodroid.so', 'libmonosgen-2.0.so'],
  "Capacitor": ['capacitor.config.json', 'capacitor.plugins.json', 'Capacitor.framework/Capacitor'],
  "Uno Platform": ['libaot-Uno.dll.so', '/Uno.dll', '/Uno.Core.dll'],
  "RootBeer": ['libtoolChecker.so', 'libtool-checker.so'],
  "RASP Talsec": ['libsecurity.so', 'TalsecRuntime.framework/TalsecRuntime', 'freerasp.framework/freerasp']
}

in_code_ref = {
  "IOSSecuritySuite": [b'\x49\x4f\x53\x53\x65\x63\x75\x72\x69\x74\x79\x53\x75\x69\x74\x65'], 
  "RootBeer": [b'\x72\x6f\x6f\x74\x62\x65\x65\x72', b'\x52\x6f\x6f\x74\x42\x65\x65\x72'], 
  "RASP Talsec": [b'\x46\x72\x65\x65\x72\x61\x73\x70\x50\x6c\x75\x67\x69\x6e', b'\x66\x72\x65\x65\x72\x61\x73\x70']
}

# search files related to mobile frameworks and security libraries
flag = False
for key in files_ref:
	hitted_list = [] 
	for file in list_files:
		for elem in files_ref[key]:
			if elem in file:
				hitted_list.append(file)
	if hitted_list:
		print ("\n"+ RED + "[+] " + key + " files found " + END)
		flag = True
		if args.verbose:
			print(hitted_list)
			
# search references in iOS binary file or in Android classes.dex
if args.input.find('.ipa') != -1:
	binary_name = re.search("\/([a-zA-Z0-9 \-_\.]+)\.app\/", list_files[1]).group(1)
	tmp = re.search("(Payloads?\/)", list_files[1]).group(1)
	binary_file = zip.open(tmp+binary_name+'.app/'+binary_name,'r')

if args.input.find('.apk') != -1:
	binary_file = zip.open('classes.dex','r')

binary_file_copy = binary_file.read()

for key in in_code_ref:
	hitted_list = [] 
	for elem in in_code_ref[key]:
		hit = binary_file_copy.find(elem)
		if hit != -1:
			hitted_list.append(elem)
							
	if hitted_list:
		print ("\n"+ RED + "[+] " + key + " references found in code" + END)
		flag = True
		if args.verbose:
			print(hitted_list)
				
# Print message if no references were found
if flag == False:
	print ("\n No references found.")
