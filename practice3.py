print('hello world')

food = ['potatoes', 'tomatos', 'burgers', 'hotdogs', 'ribs']
favorite_food = 'burgers'
for temp_food in food:
    print(temp_food)
    if temp_food == favorite_food:
        print("this is my favorite food")
        break

favorite_food2 = 'potatoes'
for temp_food2 in food:
    print(temp_food2)
    if temp_food2 == favorite_food2:
        print("this is my second favorite food")
        break

favorite_food3 = 'hotdogs'
for temp3 in food:
    print(temp3)
    if temp3 == favorite_food3:
        print("this is my 3rd favorite food")
        break

string2 = "this will print 8 times"
for temp4 in range(8):
    print(string2)

count = 25
while count >= 0:
    print(count)
    count -= 1
print("end of count")

count2 = 0
while count2 <= 20:
    print(count2)
    count2 += 1
print("end of count")

basketball_player = ["kyrie", "lebron", "steph", "durant"]
length = len(basketball_player) 
index = 0
while index < length:
    print("i want to play like", basketball_player[index])
    index += 1

football_player = ["jsn", 'chase', 'jefferson']
length2 = len(football_player)
print(length2)
index2 = 0
while index2 < length2:
    print("i want to catch the ball like", football_player[index2])
    index2 += 1

favorite_player = 'chase'
for nfl in football_player:
    print(nfl)
    if nfl == favorite_player:
        print("this is my favorite player")
        break

nba_player = 'kyrie'
for temp5 in basketball_player:
    if temp5 == nba_player:
        continue
    print(temp5)

print("this will not print kyrie")

nba_player2 = 'lebron'
for temp6 in basketball_player:
    if temp6 == nba_player2:
        continue
    print(temp6)

print("this will not print lebron")

nfl_player = 'chase'
for temp7 in football_player:
    if temp7 == nfl_player:
        continue
    print(temp7)

print("this will skip chase")

fruits = ["apple", "banana", "strawberry", "blueberry"]
favorite_fruits = "banana"
for temp8 in fruits:
    if temp8 == favorite_fruits:
        continue
    print(temp8)

print("this will skip banana")

project_teams = [["ava", "samantha", "james"], ["lucille", "zed"], ["edgar", "gabriel"]]
for team in project_teams:
    for student in team:
        print(student)

sales_data = [[12,17,22], [2,10,3], [5,12,13]]
scoops_sold = 0
for location in sales_data:
    print(location)
    for element in location:
        scoops_sold += element

print(scoops_sold)

numbers = [[1,2,3], [3,4,5], [5,6,7], [6,7,8]]
sum_of_numbers = 0
for sum1 in numbers:
    for sum2 in sum1:
        sum_of_numbers -= sum2

print(sum_of_numbers)

foods = [["tyree", "james"], ["milbrun", "trey"], ["klark", "klein"]]
for name in foods:
    for name1 in name:
        print(name1)

numbers2 = [[23,45,67], [45,63,23], [34,12,56], [45,24,13]]
sum_of_numbers2 = 0
for numbers3 in numbers2:
    print(numbers3)
    for numbers4 in numbers3:
        sum_of_numbers2 += numbers4

print(sum_of_numbers2)

new_numbers = [[23,45,23], [54,23,12]]
sum_of_numbers3 = 0
for t in new_numbers:
    for sum_numbers in t:
        sum_of_numbers3 += sum_numbers

print(sum_of_numbers3)


numbers = [2,-1,79,33,-45]
doubled = [num * 2 for num in numbers]
print(doubled)

grades = [90,88,62,76,89,48,57]
scaled_grades = [num2 + 10 for num2 in grades]
print(scaled_grades)

new_list = [30,24,12,25,67,89,56,78,10]
minus_10 = [m10 - 10 for m10 in new_list]
print(minus_10)

new_numbers = [30,24,26,78,46,34,12,68]
times_2 = [new_num ** 3 for new_num in new_numbers]
print(times_2)

list_foods = ["pizza", "seafood", "breakfast", "dinner", "lunch", "cake"]
favorite_list = "seafood"
for t in list_foods:
    print(t)
    if t == favorite_list:
        print("this is my favorite")
        break

for g in list_foods:
    if g == favorite_list:
        continue
    print(g)

another_food = "breakfast"
for h in list_foods:
    if h == another_food:
        continue
    print(h)

print("this shouldnt print breakfast")

length5 = len(list_foods)
index3 = 0
while index3 < length5:
    print("i want to eat", list_foods[index3])
    index3 += 1

sports = [["soccer", "football"], ["tennis", "golf"], ["snowboarding", "skiing"], ["bowling", "baseball"]]
sport1 = ["soccer", "football"]
for r in sports:
    if r == sport1:
        continue
    print(r)

sport = [["football", "tennis"], ["basketball", "baseball"], ["golf", "track"]]
for name_sport in sport:
    for element in name_sport:
        print(element)

print("hello world")







    













