import sys, glob


def apply_amendments(case):
	return ''


data = sys.argv[1]

cases = list(glob.glob(data + '/*'))
cases_success = 0

for case in glob.glob(data + '/*'):
	print("Case", case)
	result = apply_amendments(case)
	correct_result = open(case + '/article_apres').read().strip()
	if correct_result == result:
		cases_success += 1
		print("success")
	else:
		print("fail")

print("Benchmark result:", round(cases_success / len(cases) * 100, 4), '%')