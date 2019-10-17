# VSCode C/C++ GCC AutoSynch

## Description
This script can be used to pass the general settings of c_cpp_properties.json to a task aka your compiler (e.g. GCC). If you want to contribute to extend the functionality you may do so. Just send a PR.

## Usage
```
# Clone this project.

# Edit your C/C++ Properties to fit your needs (Advanced settings are not supported yet)

# If you change your configuration name or add new ones in c_cpp_properties.json you can select them by passing the name of the configuration to the script. You do this by adding "configName=NAME_HERE" to the tasks arguments.(shown in [Pic 1]) It is important that you add the arguments AFTER .vscode/build.py!

# Edit miDebuggerPath in launcher.json. Here you add the path to your debugger e.g. "C:\\mingw-w64\\mingw32\\bin\\gdb.exe".

# To change your config from Win64_Debug to Win64_Release for example you'd change [Pic 2] to 'Win64_Release' and then the build [Pic 3] to 'Build'.
The first change changes the actual config for the compile (the resulting .exe is effected). The second change is for the Intellisense in the IDE.

# Compile :)
```

## Supported arguments
```
Shown in [Pic 1].

configName=YOUR_CONFIG_NAME - REQUIRED - selects the config that will be loaded from c_cpp_properties.json.

compiler=[clang/gcc/msvc] - OPTIONAL - changes the default commandline lookup table. Can also be used if the detection is wrong.

lang=[C/CPP] - OPTIONAL - if used it will add the chosen langunge level of c/cpp of c_cpp_properties.json to the arguments .

includeCmd=YOUR_OPTION - OPTIONAL - overwrites the default tag for includes (i.e. "-I ")
defineCmd=YOUR_OPTION - OPTIONAL - overwrites the default tag for includes (i.e. "-D ")
langStdCmd=YOUR_OPTION - OPTIONAL - overwrites the default tag for the language standard version (i.e. "-std= ")

```

[Pic 1]
![alt text](https://i.imgur.com/gnoDmBw.png)

[Pic 2]
![alt text](https://i.imgur.com/tjWqrUe.png)

[Pic 3]
![alt text](https://i.imgur.com/jZbP2uh.png)