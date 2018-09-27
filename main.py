import math
import csv

day = 86400
userHeaders = ['uid', 'pid', 'u_score', 'timestamp']
productHeaders = ['pid', 'p_score']
recHeaders = ['uid', 'pid', 'r_score']

def differentTime(latestTime, currentTime):
    if currentTime > latestTime:
        return math.ceil(float(currentTime-latestTime)/day)
    else:
        return 0

def calculate(lastScore, diff_time):
    return round(lastScore * math.pow(0.95,diff_time), 4)

def newStruct(headers, data):
    result = {}
    for i, each in enumerate(data):
        result[headers[i]] = each
    return result

def scoringFunc(user_file, product_file, current):
    print('waiting process')
    with open(user_file, 'rU') as file, open(product_file, 'rU') as file_product:
        readerUsers = csv.DictReader(file, delimiter='\t')
        readerProducts = csv.DictReader(file_product, delimiter='\t')

        users = [r for r in readerUsers]
        products = [r for r in readerProducts]

    newUsers = []
    newRec = []
    for i, user in enumerate(users):
        get_pid_score = int([product['p_score'] for product in products if product['pid'] == user['pid']].pop())
        new_score = calculate(float(user['u_score']), differentTime(int(user['timestamp']), current))
        recommendation = get_pid_score * new_score + get_pid_score
        newUsers.append(newStruct(userHeaders, [user['uid'], user['pid'], new_score, current]))
        newRec.append(newStruct(recHeaders, [user['uid'], user['pid'], recommendation]))

    writeToFiles('output/new_users_preference.txt', newUsers, userHeaders)
    writeToFiles('output/new_recommendation.txt', newRec, recHeaders)

def writeToFiles(filename, data, fieldnames):
    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')

        writer.writeheader()
        for each in data:
            writer.writerow(each)

def recommend(uid):
    with open('output/new_recommendation.txt', 'r') as file:
        reader = csv.DictReader(file, delimiter='\t')
        sorted_pid = sorted([rec for rec in reader if rec['uid'] == uid], key=lambda x: float(x.get('r_score', 0)), reverse=True)[0:5]

        for r in sorted_pid:
            print(r['pid'])