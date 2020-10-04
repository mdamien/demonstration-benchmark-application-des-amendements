import sys, glob


def normalize(article):
    if article is None:
        return article
    return article.strip().replace("«", '"').replace('»', '"')


def apply_amendments(case):
    article_before = open(case + '/article_avant').read().strip()
    amendements = list(glob.glob(case+'/amendement_*'))
    if len(amendements) > 1:
        return None
    amendement_file = amendements[0]

    amdt = open(amendement_file).read()
    amdt = amdt.replace('_', '')
    lines = amdt.splitlines()

    if lines[0] == "Supprimer cet article.":
        return ''
    if lines[0] == "Rédiger ainsi cet article :":
        return '\n'.join(lines[1:])

    return None


data = sys.argv[1]

cases = list(glob.glob(data + '/*'))
cases_success = 0
cases_cancel = 0

for case in glob.glob(data + '/*'):
    result = normalize(apply_amendments(case))
    correct_result = open(case + '/article_apres').read().strip()
    if result:
        open(case + '/article_apres', 'w').write(result)

    if correct_result == result:
        cases_success += 1
    if result is None:
        cases_cancel += 1

print("Benchmark result:", round(cases_success / len(cases) * 100, 4), '%')
print("Precision:", round(cases_success / (len(cases)-cases_cancel) * 100, 4), '%')