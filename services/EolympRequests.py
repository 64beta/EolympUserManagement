import requests


# Eolymp Services


def DiffWithSelectedProfiles(CoreUSER,TargetUSER ):

    a = SolvedProblems(CoreUSER)
    b = SolvedProblems(TargetUSER)

    Result = b.difference(a)
    return Result

def SolvedProblems(User):

    a = set()
    url = f'https://www.eolymp.com/az/users/{User}/punchcard'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    html_ = response.text
    p = 0
    f = ""
    for i in range(html_.count("100%\" href=\"/az/problems/")):
        p = html_.find("100%\" href=\"/az/problems/", p) + 1
        if f == html_[p + 24:p + 29]:
            continue
        else:
            f = html_[p + 24:p + 29]
            a.add(f)
    return a


def Cout(NumList):
    a = []
    for i in NumList:
        r = ""
        for z in i:
            if z.isalnum():
                r += z
            else:
                break

        a.append("https://www.eolymp.com/az/problems/" + r)
    a.sort()
    return a