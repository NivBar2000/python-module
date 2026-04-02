#ex1: הדפס כל שם יחד עם האינדקס שלו

names = ["Alice", "Bob", "Charlie"]
newnames=list(enumerate(names))
#print(newnames)

# ex2: הדפס כל שרת עם אינדקס שמתחיל מ־1

servers = ["app-01", "app-02", "app-03"]
#print(list(enumerate(servers, start=1) ))

#ex3: הדפס רק שגיאות באינדקס זוגי

errors = ["disk full", "timeout", "connection lost"]
errors_list=enumerate(errors)
even_error=[]
for i in errors_list:
    if i[0] % 2 == 0:
        even_error.append(i)
#print(even_error)

#ex4: הדפס רק פורטים עם אינדקס גדול מ־1

ports = [22, 80, 443, 8080]
port_list=enumerate(ports)

#?for index, port in port_list:    שתי אופציות שונות לגשת לאינדקס בתוך הרשימה
    #? if index > 1:             
    #?    print(index, port)
# for i in port_list:
    #if index[0] > 1:
    #    print(index)
    
#ex5: הדפס: User #index: name

users = ["admin", "dev", "ops"]

users_index = enumerate(users, start=1)
#for index, name in users_index:
#    print (f"User #{index}: {name}")

#ex 6:  הדפס רק את הקובץ האחרון לפי אינדקס

files = ["log1.txt", "log2.txt", "log3.txt"]
files_index = list(enumerate(files))
#? last_index=(len(files_index))           השתמשתי בלאן כדי לספור מה האיבר האחרון, יצירתי אבל קצת מסורבל
#? print(files_index[last_index-1])

#print(files_index[-1])                    פתרון פשוט יותר, להדפיס את האינדקס במקום האחרון מהסוף בעזרת -1

#ex7: הדפס את כל האזורים מלבד הראשון

regions = ["us-east-1", "eu-west-1", "ap-south-1"]
regions_index = enumerate(regions)
# for i in regions_index:        הכנסתי לולאה והכנסתי תנאי כדי להימנע מהדפסה של הערך הראשון, חשוב לשים לב הרבה יותר קל לעשות את זה בסליסינג ולא באניומריט
#     if i[0] > 0:
#         print(i)

#ex8: הדפס כל שירות עם אינדקס שמתחיל מ־1

services = ["nginx", "redis", "postgres"]
#for index, service in enumerate(services, start=1):
    #print(index, service)
    
#ex9:  הדפס רק משימות באינדקס אי-זוגי

tasks = ["backup", "cleanup", "monitoring", "ignore", "app", "study"]
# for i in enumerate(tasks):
#     if i[0] % 2 ==1:
#         print(i)
        
#ex10: עצור את הלולאה כאשר האינדקס מגיע ל־2

containers = ["c1", "c2", "c3", "c4"]
# for container in enumerate(containers):
#     print(container)
#     if container[0]==2:
#         break

#ex11: הדפס כל host יחד עם ה־IP שלו

hosts = ["host1", "host2", "host3"]
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

#print(list(zip(hosts, ips)))

#ex12: הדפס: User <name> has ID <id>

users = ["alice", "bob", "charlie"]
ids = [101, 102, 103]

# for user, id in zip(users, ids):
#     print(f"user {user} has ID {id}")
    
#ex13: הדפס התאמה בין service ל־port

services = ["nginx", "redis", "postgres"]
ports = [80, 6379, 5432]

#? print(list(zip(services, ports)))             אופציה נוספת היא לעשות את זה בלולאה 

# for service, port in zip(services, ports):     הדפסה בלולאה, פלט קצת יותר קריא
#     print(service, port)

#ex14: הדפס region+zone מחוברים יחד

regions = ["us-east-1", "eu-west-1"]
zones = ["a", "b"]

# for region, zone in zip(regions, zones):
#     print(f"{region}+{zone}")

#ex15: הדפס רק containers ש־status שלהם "running"

containers = ["c1", "c2", "c3"]
statuses = ["running", "stopped", "paused"]

# for container, statuse in zip(containers, statuses):
#     if statuse == "running":
#         print(container)

#ex16:  הדפס את כל שלושת הערכים יחד

files = ["file1", "file2"]
sizes = [100, 200]
types = ["txt", "log"]

# print(list(zip(files, sizes, types)))

#ex17: בדוק כמה איברים יודפסו בפועל

names = ["serviceA", "serviceB", "serviceC"]
versions = ["1.0", "2.0"]

new_list=list(zip(names, versions))
#print(len(new_list))

#ex18: הדפס כל שלישייה יחד

dbs = ["mysql", "postgres", "mongo"]
ports = [3306, 5432, 27017]
hosts = ["db1", "db2", "db3"]

# for three in zip(dbs, ports, hosts):
#     print(three)

#ex 19: הדפס רק משימות שנכשלו

tasks = ["build", "test", "deploy", "plug"]
durations = [5, 10, 3, 4]
statuses = ["ok", "ok", "failed", "failed"]

# for task, duration, statuses in zip(tasks,durations,statuses):
#     if statuses == "failed":
#         print(f"the task {task} faild, the next work for {duration} hours canceld")

#ex20: הדפס את כל הערכים יחד בשורה אחת

users = ["admin", "dev"]
roles = ["full-access", "read-only"]
regions = ["us", "eu"]

print(list(zip(users, roles, regions)))