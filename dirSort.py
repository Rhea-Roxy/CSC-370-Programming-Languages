import collections


def dirsort(dirs):
    result = []
    dict = collections.defaultdict(list)
    for i in range(len(dirs)):
        dict[dirs[i].count('/')].append(dirs[i])

    for key in sorted(dict.keys()):
        dict.get(key).sort()
        for ke in dict.get(key): result.append(ke)
    return result


def q_inputs():
    inputs = [
        ["/", "/usr/", "/usr/local/", "/usr/local/bin/", "/games/", "/games/snake/", "/homework/ ",
         "/temp/downloads/"],
        ["/usr/", "/usr/local/", "/bin/", "/usr/local/bin/", "/usr/bin/", "/bin/local/",
         "/bin/local/"], ["/", "/a/", "/b/", "/c/", "/d/", "/e/", "/f/", "/g/"],
        ["/", "/a/", "/b/", "/c/", "/d/", "/e/", "/f/", "/g/", "/a/a/", "/b/g/c/", "/g/f/"],
        ["/a/b/c/d/e/f/g/h/i/j/k/l/m/n/", "/o/p/q/r/s/t/u/v/w/x/y/z/"],
        ["/a/b/", "/ab/cd/", "/c/d/", "/a/b/c/", "/ab/c/d/", "/a/bc/d/", "/a/b/cd/"]]

    for i in range(len(inputs)):
        print(inputs[i])
        print(dirsort(inputs[i]))
        print()


q_inputs()
