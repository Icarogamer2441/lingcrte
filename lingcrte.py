variables = {}
functions = {}
ifs = []
repeat = []

tokens = {}

def interpret(code):
    lines = code.split("\n")

    for line in lines:
        if line.startswith("printmsg"):
            printstart = line.split("@> ")[1].split(" $ ")[0].strip("\"\'")
            printmsgstart = line.split(" $ ")[1].split(" , ")[0].strip("\"\'")
            printmsgend = line.split(" , ")[1].split(" @<")[0].strip("\"\'")
            tokens["print"] = [printstart, printmsgstart, printmsgend]
        elif line.startswith("int"):
            intstart = line.split("@> ")[1].split(" $ ")[0].strip("\"\'")
            intequals = line.split(" $ ")[1].split(" @<")[0].strip("\"\'")
            tokens["int"] = [intstart, intequals]
        elif line.startswith("string"):
            stringstart = line.split("@> ")[1].split(" $ ")[0].strip("\"\'")
            stringequals = line.split(" $ ")[1].split(" , ")[0].strip("\"\'")
            stringstartandend = line.split(" , ")[1].split(" @<")[0].strip("\"\'")
            tokens["string"] = [stringstart, stringequals, stringstartandend]
        elif line.startswith("printvar"):
            printstart = line.split("@> ")[1].split(" $ ")[0].strip("\"\'")
            printmsgstart = line.split(" $ ")[1].split(" , ")[0].strip("\"\'")
            printmsgend = line.split(" , ")[1].split(" @<")[0].strip("\"\'")
            tokens["printvar"] = [printstart, printmsgstart, printmsgend]
        elif line.startswith("function"):
            func = line.split("@> ")[1].split(" $ ")[0].strip("\"\'")
            funcstart = line.split(" $ ")[1].split(" , ")[0].strip("\"\'")
            funcend = line.split(" , ")[1].split(" @<")[0].strip("\"\'")
            tokens["function"] = [func, funcstart, funcend]
        elif line.startswith("addcodefunction"):
            funcstart = line.split("@> ")[1].split(" $ ")[0].strip("\"\'")
            funccodestart = line.split(" $ ")[1].split(" , ")[0].strip("\"\'")
            funccodeend = line.split(" , ")[1].split(" @<")[0].strip("\"\'")
            tokens["addfunctioncode"] = [funcstart,funccodestart,funccodeend]
        elif line.startswith("callfunction"):
            funcstart = line.split("@> ")[1].split(" $ ")[0].strip("\"\'")
            funccallstart = line.split(" $ ")[1].split(" , ")[0].strip("\"\'")
            funccallend = line.split(" , ")[1].split(" @<")[0].strip("\"\'")
            tokens["callfunction"] = [funcstart, funccallstart, funccallend]
        elif line.startswith("input"):
            inputstart = line.split("@> ")[1].split(" $ ")[0].strip("\"\'")
            inputmsgstartandend = line.split(" $ ")[1].split(" @<")[0].strip("\"\'")
            tokens["input"] = [inputstart, inputmsgstartandend]
        elif line.startswith("float"):
            floatstart = line.split("@> ")[1].split(" $ ")[0].strip("\"\'")
            floatequals = line.split(" $ ")[1].split(" @<")[0].strip("\"\'")
            tokens["float"] = [floatstart, floatequals]
        elif line.startswith("if"):
            ifname = line.split("@> ")[1].split(" $ ")[0].strip("\"\'")
            ifstart = line.split(" $ ")[1].split(" , ")[0].strip("\"\'")
            ifend = line.split(" , ")[1].split(" @<")[0].strip("\"\'")
            tokens["if"] = [ifname, ifstart, ifend]
        elif line.startswith("repeat"):
            repeatname = line.split("@> ")[1].split(" @<")[0].strip("\"\'")
            tokens["repeat"] = [repeatname]
        elif line.startswith("bool"):
            boolname = line.split("@> ")[1].split(" $ ")[0].strip("\"\'")
            boolequals = line.split(" $ ")[1].split(" @<")[0].strip("\"\'")
            tokens["bool"] = [boolname, boolequals]
        elif line.startswith("addnumber"):
            addnumbername = line.split("@> ")[1].split(" $ ")[0].strip("\"\'")
            addnumberstart = line.split(" $ ")[1].split(" , ")[0].strip("\"\'")
            addnumberend = line.split(" , ")[1].split(" @<")[0].strip("\"\'")
            tokens["addnumber"] = [addnumbername, addnumberstart, addnumberend]
        elif line.startswith("removenumber"):
            removenumbername = line.split("@> ")[1].split(" $ ")[0].strip("\"\'")
            removenumberstart = line.split(" $ ")[1].split(" , ")[0].strip("\"\'")
            removenumberend = line.split(" , ")[1].split(" @<")[0].strip("\"\'")
            tokens["removenumber"] = [removenumbername, removenumberstart, removenumberend]
        elif line.startswith("start"):
            extension = line.split(" ")[1].strip("\"\'")
            def interpretlang(coding):
                liness = coding.split("\n")

                for linee in liness:
                    if linee.startswith(tokens["print"][0]):
                        msg = linee.split(tokens["print"][1])[1].split(tokens["print"][2])[0].strip("\"\'")
                        print(msg)
                    elif linee.startswith(tokens["printvar"][0]):
                        varname = linee.split(tokens["printvar"][1])[1].split(tokens["printvar"][2])[0].strip("\"\'")
                        print(variables[varname])
                    elif linee.startswith(tokens["int"][0]):
                        varname = linee.split(" ")[1].split(" " + tokens["int"][1] + " ")[0].strip("\"\'")
                        value = linee.split(" " + tokens["int"][1] + " ")[1].strip("\"\'")
                        variables[varname] = int(value)
                    elif linee.startswith(tokens["string"][0]):
                        varname = linee.split(" ")[1].split(" " + tokens["string"][1] + " " + tokens["string"][2])[0].strip("\"\'")
                        value = linee.split(" " + tokens["string"][1] + " " + tokens["string"][2])[1].split(tokens["string"][2])[0].strip("\"\'")
                        variables[varname] = value
                    elif linee.startswith(tokens["function"][0]):
                        funcname = linee.split(tokens["function"][1])[1].split(tokens["function"][2])[0].strip("\"\'")
                        functions[funcname] = []
                    elif linee.startswith(tokens["addfunctioncode"][0]):
                        funcname = linee.split(" ")[1].split(" " + tokens["addfunctioncode"][1])[0].strip("\"\'")
                        funccode = linee.split(" " + tokens["addfunctioncode"][1])[1].split(tokens["addfunctioncode"][2])[0].strip("\"\'")
                        functions[funcname].append(funccode)
                    elif linee.startswith(tokens["callfunction"][0]):
                        funcname = linee.split(tokens["callfunction"][1])[1].split(tokens["callfunction"][2])[0].strip("\"\'")
                        interpretlang("\n".join(functions.get(funcname)))
                    elif linee.startswith(tokens["input"][0]):
                        inputvarname = linee.split(" ")[1].split(" " + tokens["input"][1])[0].strip("\"\'")
                        inputmsg = linee.split(" " + tokens["input"][1])[1].split(tokens["input"][1])[0].strip("\"\'")
                        variables[inputvarname] = input(inputmsg)
                    elif linee.startswith(tokens["float"][0]):
                        varname = linee.split(" ")[1].split(" " + tokens["float"][1] + " ")[0].strip("\"\'")
                        value = linee.split(" " + tokens["float"][1] + " ")[1].strip("\"\'")
                        variables[varname] = float(value)
                    elif linee.startswith(tokens["repeat"][0]):
                        times = linee.split(" ")[1].split(" >> ")[0].strip("\"\'")
                        repeatname = linee.split(" >> ")[1].strip("\"\'")
                        repeat = []
                        for linnee in liness:
                            if linnee.startswith(f"{repeatname}"):
                                code = linnee.split("@ ")[1].split(" @codend")[0].strip("\"\'")
                                repeat.append(code)
                            elif linnee.startswith(f"end{repeatname}"):
                                for i in range(int(times)):
                                    interpretlang("\n".join(repeat))
                                break
                    elif linee.startswith(tokens["if"][0]):
                        varname1 = linee.split(tokens["if"][1])[1].split(",")[0].strip("\"\'")
                        varname2 = linee.split(",")[1].split(tokens["if"][2] + " >> ")[0].strip("\"\'")
                        ifname = linee.split(tokens["if"][2] + " >> ")[1].strip("\"\'")
                        ifs = []

                        for linne in liness:
                            if linne.startswith(f"{ifname}"):
                                code = linne.split("$ ")[1].split(" $codend")[0].strip("\"\'")
                                ifs.append(code)
                            elif linne.startswith(f"end{ifname}"):
                                if variables.get(varname1) == variables.get(varname2):
                                    interpretlang("\n".join(ifs))
                                break
                    elif linee.startswith("python"):
                        pycodename = linee.split(" >> ")[1].strip("\"\'")
                        pycode = []

                        for linne in liness:
                            if linne.startswith(f"{pycodename}"):
                                code = linne.split("@ ")[1].split(" @codend")[0].strip("\"\'")
                                pycode.append(code)
                            elif linne.startswith(f"end{pycodename}"):
                                exec("\n".join(pycode))
                                break
                    elif linee.startswith(tokens["bool"][0]):
                        varname = linee.split(" ")[1].split(" " + tokens["bool"][1] + " ")[0].strip("\"\'")
                        value = linee.split(" " + tokens["bool"][1] + " ")[1].strip("\"\'")
                        if value == "true":
                            variables[varname] = True
                        elif value == "false":
                            variables[varname] = False
                    elif linee.startswith(tokens["addnumber"][0]):
                        varname = linee.split(tokens["addnumber"][1])[1].split(",")[0].strip("\"\'")
                        addnumber = linee.split(",")[1].split(tokens["addnumber"][2])[0].strip("\"\'")
                        variables[varname] += int(addnumber)
                    elif linee.startswith(tokens["removenumber"][0]):
                        varname = linee.split(tokens["removenumber"][1])[1].split(",")[0].strip("\"\'")
                        addnumber = linee.split(",")[1].split(tokens["removenumber"][2])[0].strip("\"\'")
                        variables[varname] += int(addnumber)
            filename = input(f"what's your .{extension} file? > ")
            if filename.endswith(f".{extension}"):
                with open(filename, "r") as fi:
                    content = fi.read()
                interpretlang(content)
            else:
                print(f"use .{extension} file extension!")

def execute_file(filename):
    if filename.endswith(".ling"):
        with open(filename, "r") as f:
            interpret(f.read())
    else:
        print("use .ling file extension!")

print("lingcrte v1.1")
filename = input("what's your .ling file? > ")
execute_file(filename)
