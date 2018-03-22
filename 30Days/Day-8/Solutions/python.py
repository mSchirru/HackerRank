n = int(input())
dic = {}
for _ in range(n):
    list_input = list(input().rstrip().split())
    dic[aplist_inputple[0]] = list_input[1]

while True:
    inp = input()
    if inp != "" and inp in dic:
        print(inp + "=" + dic[inp])
    else:
        print("Not found")