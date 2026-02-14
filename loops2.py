print('loops part 2')

nba_player = ['kyrie', 'lebron', 'steph', 'anthonty edwards']
favorite_nba_player = 'steph'
for nba_player2 in nba_player:
    print(nba_player2)
    if nba_player2 == favorite_nba_player:
        print("this my favorite player")
        break

string1 = "this gone print 8 times and im going to count it"
for string12 in range(8):
    print(string1, str(string12 + 1))

for player in nba_player:
    print(player)

count = 24
while count >= 0:
    print(count)
    count -= 1
print("shoot the ball")

count1 = 0
while count1 <= 30:
    print(count1)
    count1 += 1
print("run the play")

football_player = ['jsn', 'chase', 'jefferson', 'smith', 'brown']
length = len(football_player)
index = 0
while index < length:
    print("i want to play like", football_player[index])
    index += 1

favorite_nfl_player = 'jefferson'
for favorite in football_player:
    print(favorite)
    if favorite == favorite_nfl_player:
        print("this is my favorite player")
        break

favorite_nfl_player2 = 'chase'
for favorite2 in football_player:
    print(favorite2)
    if favorite2 == favorite_nfl_player2:
        print("this is my second favorite player")
        break

nfl_player3 = 'jsn'
for favorite3 in football_player:
    print(favorite3)
    if favorite3 == nfl_player3:
        print("this guy just won offensice player of the year")
        break

MVPs = ['peyton manning', 'tom brady', 'russel wilson', 'matthew stafford', 'lamar jackson', 'josh allen']
mvp2026 = 'matthew stafford'
for favorite4 in MVPs:
    print(favorite4)
    if favorite4 == mvp2026:
        print("this guy just won mvp this year")
        break

mvp_7 = 'tom brady'
for favorite5 in MVPs:
    print(favorite5)
    if favorite5 == mvp_7:
        print("this guy has 7 superbowl mvp's")
        break

leading_rushing_qb = 'lamar jackson'
for favorite6 in MVPs:
    print(favorite6)
    if favorite6 == leading_rushing_qb:
        print("this guy is the leagues leading rushing qb")
        break

rushing = "lamar jackson is the leagues leading rushing qb. i want this to print 8 times"
for rush in range(8):
    print(rushing, str(rush + 1))

point_guards = ["kyrie", "steph", "lebron", "james harden", "lamelo"]
for guard in point_guards:
    print(guard)

count2 = 30
while count2 >= 0:
    print(count2)
    count2 -= 1
print("run the play")

favorite7 = "kyrie"
for ages in point_guards:
    if ages == favorite7:
        continue
    print(ages)

big_numbers_list = [1,2,-1,4,-5,5,2,-9]
for i in big_numbers_list:
    if i <= 0:
        continue
    print(i)

ages = [12,38,34,26,21,19,67,41,17]
for p in ages:
    if p < 21:
        continue
    print(p)

favorite8 = 'james harden'
for s in point_guards:
    if s == favorite8:
        continue
    print(s)

numbers = [12,13,16,17,23,45,34,24,21,67,56,57,58,4,3,5,6,7,8,2]
for g in numbers:
    if g >= 10:
        continue
    print(g)

for t in numbers:
    if t <= 45:
        continue
    print(t)

foods = ["salads", "dressing", "yams", "seafood", "salad", "chicken", "turkey", "mac and cheese", "salad", "ribs", "hotdogs", "hamburgers"]
skip_food = "salads"
for h in foods:
    if h == skip_food:
        continue
    print(h)

security_incident = ['breach', 'rainbow attack', 'watering hole attack', 'phishing attack', 'impersonation attack']
attack = 'watering hole attack'
for attack1 in security_incident:
    if attack1 == attack:
        continue
    print(attack1)

attack2 = 'breach'
for attack3 in security_incident:
    if attack3 == attack2:
        print(attack3)
        break
print("this is my favorite attack to solve")

attack4 = "phishing attack"
for attack5 in security_incident:
    if attack5 == attack4:
        print(attack5)
        break
print("this is my second favorite security incident to solve")

attack6 = "rainbow attack"
for attack7 in security_incident:
    if attack7 == attack6:
        continue
    print(attack7)

print("this gone skip rainbow attack")






