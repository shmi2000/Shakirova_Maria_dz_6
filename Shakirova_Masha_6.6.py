from sys import argv

with open("baker.csv", "a", encoding="utf-8") as donut_a:
    with open("baker.csv", "r", encoding="utf-8") as donut_r:
        if len(argv) > 1 and [a for a in argv[1:] if a.replace(".", "").isdigit()]:
            if len(argv) == 3:
                print(*donut_r.read().split()[int(argv[2])], sep="\n")
            if "," in argv[1] or "." in argv[1]:
                print(argv[1], file=donut_a)
            else:
                print(*donut_r.readlines()[int(argv[1]) - 1:], sep="\n")
        else:
            print(donut_r.read())
