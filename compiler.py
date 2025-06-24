import re
def compileLine(line):
    if re.match(r"(\d+)\s*?(\+|-|\*|\/|%)\s*(\d+)(\s*?(\+|-|\*|\/|%)\s*(\d+))*",line):
        return str(eval(line))
    else:
        return line
def compile(code):
    codeDict = {}
    python = ""
    lines = code.split("\n")
    for line in lines:
        id, statement, goto = line.split("|")
        id, statement, goto = [item.strip() for item in [id, statement, goto]]
        if id == "":
            raise ValueError("Line id must not be blank")
        if id in codeDict.keys():
            raise ValueError(f"Line id {id}")
        codeDict.update(
            {
                id:{
                    "code":statement,
                    "goto":goto
                }
            }
        )
    if "init" in codeDict.keys():
        currentLine = codeDict["init"]
    else:
        raise ValueError('The line with id "init" could not be found.')
    
    while True:
        python+=compileLine(currentLine["code"])
        if currentLine["code"]:
            python+="\n"
        if currentLine["goto"]=="":
            break
        if currentLine["goto"] in codeDict.keys():
            currentLine = codeDict[currentLine["goto"]]
        else:
            raise ValueError(f'The line with id "{currentLine["goto"]}" could not be found.')
    return python
