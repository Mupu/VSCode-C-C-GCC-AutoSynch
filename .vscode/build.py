import sys
import json
import os

defaultCompilerCmds = {
    "gcc" : {
        "includeCmd"    :       "-I ",
        "defineCmd"     :       "-D ",
        "langStdCmd"    :       "-std="
    },
    "clang" : {
        # Not tested!
        "includeCmd"    :       "-I ",
        "defineCmd"     :       "-D ",
        "langStdCmd"    :       "-std="
    },
    "msvc" : {
        # Not tested!
        "includeCmd"    :       "/I",
        "defineCmd"     :       "/D",
        "langStdCmd"    :       "/std:"
    }
}

args = {}
for i in range(len(sys.argv)):
    # skip name of python script
    if i > 0:
        try:
            split = sys.argv[i].split("=", 1)
            args[split[0]] = split[1]
        except IndexError as err:
            print("Error: Illegal argument '" + sys.argv[i] + "' Please check the docs.")
            exit(1)
        
print("Args: " + str(args))

if args.get("configName") is None:
        print("Error: Argument 'configName' missing! Please add it to the tasks arguments.")
        exit(1)

try:
    with open(".vscode/c_cpp_properties.json", "r") as tasks_json:
        tasks = json.load(tasks_json)
        configs = tasks["configurations"]
        
        # load chosen config
        config = None
        for i in range(len(configs)):
            if configs[i]["name"] == args["configName"]:
                config = tasks["configurations"][i]
                break

        if config is None:
            print("Error: Config not found! Please select a existing config. (Task argument: configName=YOUR_CONFIG_NAME)")
            exit(1)

        # load config data
        defines = config.get("defines")
        includes = config.get("includePath")
        cstandard = config.get("cStandard")
        cppstandard = config.get("cppStandard")
        compilerArgs = config.get("compilerArgs")
        compilerPath = config.get("compilerPath")
        intelliSenseMode = config.get("intelliSenseMode") # used for automatic lookup table detection
        compiler = None

        # choose compiler
        if args.get("compiler") is None:
            if intelliSenseMode.startswith("gcc"):
                compiler = "gcc"
            elif intelliSenseMode.startswith("clang"):
                compiler = "clang"
            else: compiler = "msvc"
        else:
            compiler = args["compiler"]
        
        
        # overwrite defaults of chosen compiler
        print("Used defaultCompilerCmds: " + compiler)
        for k,v in args.items():
            defaultCompilerCmds[compiler][k] = v

        if compilerPath is None:
            print("Error: Compiler path not found! Please select a existing compiler in the C/C++ options.")
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
                cmd += " " + defaultCompilerCmds[compiler]["defineCmd"] + d

        # add include paths
        if compilerArgs is not None:
            for i in includes:
                cmd += " " + defaultCompilerCmds[compiler]["includeCmd"] + i
        
        # add cStandard/c++Standard
        if args["lang"].upper() == "C":
            cmd += " " + defaultCompilerCmds[compiler]["langStdCmd"] + cstandard
        elif args["lang"].upper() == "CPP":
            cmd += " " + defaultCompilerCmds[compiler]["langStdCmd"] + cppstandard
        

        # run command
        print("Running command: " + cmd)

        # create out folder
        if not os.path.exists("out"): os.makedirs("out")

        statusCode = os.system(cmd)
        print("The build process has exited with code " + str(statusCode) + ".")
        exit(statusCode)
except IOError as err:
    print("Error: File c_cpp_properties.json not found. Please install the Microsoft C/C++ extension and try again.")
    exit(1)