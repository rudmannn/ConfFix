import os
import sys

util_path = "/Users/huanghuaxun/Documents/GitHub/ConfFix/source_code/ConfFixTestUtil.java" # please locate the path of ConfFixTestUtil.java

cnt = 0


def findStatement(lines, file):
    if file.endswith('.java'):
        for cnt, line in enumerate(lines):
            if ";" in line:
                return cnt + 1
    if file.endswith('.kt'):
        for cnt, line in enumerate(lines):
            if "return" in line or "}" in line:
                return cnt
    return Exception("No statement found")


def findProjectDir(string, project_name):
    os.chdir(string)
    for item in os.listdir(string):
        if os.path.isdir(item) and item.startswith(project_name) and not item.endswith(".zip"):
            return os.path.abspath(item)


def insertFile(string, root_dirs):
    global cnt
    if os.path.isdir(string):
        os.chdir(string)
        for i in os.listdir("."):
            if "main" in os.getcwd() and i == root_dirs[cnt] if len(root_dirs) > cnt else False:
                cnt += 1
                if len(root_dirs) == cnt:
                    print(os.path.abspath(i))
                    os.system("cp " + util_path + " " + os.path.abspath(i))
                    # open the file and insert the code
                    with open(os.path.abspath(i) + "/ConfFixTestUtil.java", "r") as f:
                        lines = f.readlines()

                    with open(os.path.abspath(i) + "/ConfFixTestUtil.java", "w") as f:
                        f.write("package " + ".".join(root_dirs) + ";\n")
                        for line in lines:
                            f.write(line)
                    return
            insertFile(i, root_dirs)
        os.chdir("..")


def findAllFile(string, xmlName, id):
    if os.path.isdir(string):
        os.chdir(string)
        for i in os.listdir("."):
            findAllFile(i, xmlName, id)
        os.chdir("..")

    elif string.endswith(".kt"):
        if xmlName is None: # flag = 1
            parse_file1(string, id)
        else: # flag = 4
            xmlNames = xmlName.split(".xml")[0].split("_")
            xmlName = ''.join(word.lower() for word in xmlNames)
            words = id.split("_")
            id = words[0] + ''.join(word.capitalize() for word in words[1:])
            parse_file4(string, xmlName, id)

    elif string.endswith(".java"):
        if xmlName is None: # flag = 2
            parse_file2(string, id)
        else: # flag = 3
            xmlName = xmlName.split(".xml")[0]
            parse_file3(string, xmlName, id)




def parse_file1(string, id):
    with open(string, "r") as f:
        lines = f.readlines()

    for count, line in enumerate(lines):
        if id in line:
            storage = count
            print(os.path.abspath(string))
            print(line)
            while (lines[storage]):
                if "val" in lines[storage]:
                    print(lines[storage].split("=")[0].strip().split(" ")[-1])
                    with open(string, "w") as f:
                        flag = None
                        for i in range(len(lines)):
                            if i == 0:
                                p = 0
                                while ("package" not in lines[p]):
                                    p += 1
                                    if "class" in lines[p] and "import" not in lines[p]:
                                        break

                            if i == p + 1:  # import package in f
                                if string.endswith(".kt"):
                                    f.write("\nimport " + ".".join(root_dirs) + ".ConfFixTestUtil\n\n")
                                elif string.endswith(".java"):
                                    f.write("\nimport " + ".".join(root_dirs) + ".ConfFixTestUtil;\n\n")

                            if i == count:
                                flag = findStatement(lines[count:], string) + count

                            if flag and i == flag:
                                if string.endswith(".kt"):
                                    f.write("\nConfFixTestUtil.processObject(" +
                                            lines[storage].split("=")[0].strip().split(" ")[-1] + ", this)\n\n")

                            f.write(lines[i])
                    break
                else:
                    storage -= 1


def parse_file2(string, id):
    with open(string, "r") as f:
        lines = f.readlines()

    for count, line in enumerate(lines):
        if id in line and "findViewById(R.id." in line:
            storage = count
            print(os.path.abspath(string))
            print(line)
            while (lines[storage]):
                if "=" in lines[storage]:
                    print(lines[storage].split("=")[0])
                    with open(string, "w") as f:
                        flag = None
                        for i in range(len(lines)):
                            if i == 0:
                                p = 0
                                while ("package" not in lines[p]):
                                    p += 1
                                    if "class" in lines[p] and "import" not in lines[p]:
                                        break

                            if i == p + 1:  # import package in f
                                if string.endswith(".java"):
                                    f.write("\nimport " + ".".join(root_dirs) + ".ConfFixTestUtil;\n\n")

                            if i == count:
                                # flag = findBracket(lines[count:]) + count
                                flag = findStatement(lines[count:], string) + count

                            if flag and i == flag:
                                if string.endswith(".java"):
                                    f.write("\nConfFixTestUtil.processObject(" + lines[storage].split("=")[
                                        0].strip() + ", this);\n\n")

                            f.write(lines[i])
                    break
                else:
                    storage -= 1


def parse_file3(string, xmlName, id):
    with open(string, "r") as f:
        lines = f.readlines()

    for count, line in enumerate(lines):
        if "=" in line and "inflater.inflate(" in line and xmlName in line:
            storage = count
            print(os.path.abspath(string))
            print(line.split("=")[0].strip())
            while (lines[storage]):
                if "=" in lines[storage]:
                    val = lines[storage].split("=")[0].strip()
                    with open(string, "w") as f:
                        flag = None
                        for i in range(len(lines)):
                            if i == 0:
                                p = 0
                                while ("package" not in lines[p]):
                                    p += 1
                                    if "class" in lines[p] and "import" not in lines[p]:
                                        break

                            if i == p + 1:  # import package in f
                                if string.endswith(".java"):
                                    f.write("\nimport " + ".".join(root_dirs) + ".ConfFixTestUtil;\n\n")

                            if i == count:
                                # flag = findBracket(lines[count:]) + count
                                flag = findStatement(lines[count:], string) + count

                            if flag and i == flag:
                                if string.endswith(".java"):
                                    f.write("\nConfFixTestUtil.processObject(" + val + ".findViewById(" + id + "), this);\n\n")

                            f.write(lines[i])
                    break
                else:
                    storage -= 1


def parse_file4(string, xmlName, id):
    with open(string, "r") as f:
        lines = f.readlines()

    for count, line in enumerate(lines):
        if "PlayerFragment" in string and count == 200:
            print()
        if xmlName in line.lower() and "Binding.inflate" in line:
            storage = count
            print(os.path.abspath(string))
            print(line)
            while (lines[storage]):
                if "=" in lines[storage]:
                    print(lines[storage].split("=")[0].strip())
                    with open(string, "w") as f:
                        flag = None
                        for i in range(len(lines)):
                            if i == 0:
                                p = 0
                                while ("package" not in lines[p]):
                                    p += 1
                                    if "class" in lines[p] and "import" not in lines[p]:
                                        break

                            if i == p + 1:  # import package in f
                                if string.endswith(".kt"):
                                    f.write("\nimport " + ".".join(root_dirs) + ".ConfFixTestUtil\n\n")
                                elif string.endswith(".java"):
                                    f.write("\nimport " + ".".join(root_dirs) + ".ConfFixTestUtil;\n\n")

                            if i == count:
                                flag = findStatement(lines[count:], string) + count

                            if flag and i == flag:
                                if string.endswith(".kt"):
                                    f.write("\nConfFixTestUtil.processObject(binding." + id + ", this)\n\n")

                            f.write(lines[i])
                    break
                else:
                    storage -= 1


if __name__ == '__main__':

    xmlName = None

    project_name = "LibreTube"
    id = "conffix_test"
    xmlName = "fragment_player.xml"
    root_dir = "com.github.libretube"


    root_dirs = root_dir.split(".")
    project_dir = findProjectDir("/Users/huanghuaxun/Documents/GitHub", project_name)
    print(project_dir)

    insertFile(project_dir, root_dirs)

    findAllFile(project_dir, xmlName, id)


