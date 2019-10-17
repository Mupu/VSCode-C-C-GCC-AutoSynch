import sys
import json
import os

with open(".vscode/c_cpp_properties.json", "r") as tasks_json:
    tasks = json.load(tasks_json)
    configs = tasks["configurations"]
    
    # load chosen config
    config = None
    for i in range(len(configs)):
        if configs[i]["name"] == sys.argv[1]:
            config = tasks["configurations"][i]
            break

    if config is None:
        print("Config not found! Please select a existing config. (2. argument in your task that starts build.py)")
        exit(1)

    # load config data
    defines = config.get("defines")
    includes = config.get("includePath")
    cstandard = config.get("cStandard")
    cppstandard = config.get("cppStandard")
    compilerArgs = config.get("compilerArgs")
    compilerPath = config.get("compilerPath")

    if compilerPath is None:
        print("Compiler path not found! Please select a existing compiler in the C/C++ options.")
        exit(1)

    # add compiler to be used
    cmd = compilerPath

    # add compilerArgs
    if compilerArgs is not None:
        for a in compilerArgs:
            cmd += " " + a

    # add defines
    if compilerArgs is not None:
        for d in defines:
            cmd += " -D " + d
 
    # add include paths
    if compilerArgs is not None:
        for i in includes:
            cmd += " -I " + i
    
    # add cStandard/c++Standard
    if cstandard and compilerPath.endswith("gcc.exe"):
        cmd += " -std=" + cstandard
    elif cppstandard and compilerPath.endswith("g++.exe"):
        cmd += " -std=" + cppstandard

    # run command
    print("Running command: " + cmd)

    # create out folder
    if not os.path.exists("out"): os.makedirs("out")

    statusCode = os.system(cmd)
    print("The build process has exited with code " + str(statusCode) + ".")
    exit(statusCode)