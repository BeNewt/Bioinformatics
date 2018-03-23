hello = """BCABCCGACDCCDADDCBAABADCAABBDACDBDBADBACCBADDDDBBB
BAACABBACABDABACDDBCACABDBDACDBCADBDBADBADBADBBABDACBADCAACC
DABBBCCBDBCDCACCBBBACBBCDCADDDADCBDCBBCDBACACDCDCBDBBCADCCBA
ADBBBBCBDDCDCADACBBACBCDDBBCDBCADACCACCGBBABCDDDBBBABBBADBBB
ADDAAABADCBCCCBCDAADBABDCADBDDDDDDDDDDADCCAAACAADDDDDCBCCDCD
CBACCBABBDBBCABBBCDDBDADACADBAACBADBCDBBCDABADCCDDCAADCCBAAA
DCCBABBCDCADBCCCABCAABADDDDCABABDAABADBBCCBDDDBBCCDBAADBCCAD
ABBDCCCACADDBACACBABBBADBDCBDDDBDBDDBBDDBDCBCACBDCBBCBBDDDDC
ABDAAADCDBABCCBBBBAACACBDBACDBDDAADACBBBDAAACDDCCCBDCADDCACB
ACBCDCDDBBDABAAAADDCCDCDACDBAAAAAAACCABDBCAABBCDAACDADDCACDA
BCACACCAABCABCBACBACDCCBDBABBAAACDDDAAADDCACDDCCDADDBADADBAC
BADCBCCCADBDDABACCDBBDAADADCDABBBADBBACAADABABBAACABBBDDDBAD
DBDDADBCDBDBCADBCBAACCCBCBDBCACDDBADAADBBDDABCDBAAADBDAABDDA
ACACBCCCADCCBBDCCBCAACCCDCABDABADAAAADABABCDAADDDABAAADCADBB
ADDDDADDABCAADACBBBCBBDBDBCAAAACBCBBABCBBBDACCDCDABACBBCBDDA
BCDDDABADCBACBDDADABABDBBACDDADABBADACDCCCDAADABBBBBBACADBBB
CACBBBCCBBDBADABBD"""

hello = hello.replace('\r', '').replace('\n', '')



tally_a = 0.0
tally_b = 0.0
tally_c = 0.0
tally_d = 0.0
count = 0.0

for letter in hello:
    if letter == 'C':
        tally_c +=1
    if letter == 'D':
        tally_d +=1
    if letter == 'A':
        tally_a +=1
    if letter == 'B':
        tally_b +=1
    count +=1

def percentage(tally, count):
  return str((tally / count) * 100) + "%"

print("total: " + str(count)) 
print("A: " + str(tally_a) + " B: " + str(tally_b) + " C: " + str(tally_c) + " D: " + str(tally_d))
print("A: " + percentage(tally_a, count) + " B: " + percentage(tally_b, count) + " C: " + percentage(tally_c, count) + " D: "  + percentage(tally_d, count))
