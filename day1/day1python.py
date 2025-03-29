import requests

def getInput():
    # The URL of the external API
    url = "https://adventofcode.com/2024/day/1/input"
    # To find cookie: Developer Tools > Application Tab > Cookies > session
    headers = {
        "Cookie": "session=SESSION_COOKIE"
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None
    
    text_content = response.text

    lines = text_content.strip().split("\n")

    list1 = []
    list2 = []

    for line in lines:
        item1, item2 = line.split(' ', 1)

        list1.append(int(item1))
        list2.append(int(item2))
    
    # for i in range(len(list1)):
    #     print(f"{list1[i]} {list2[i]}")
    
    return (list1, list2)

def totalDistance(list1, list2):
    list1.sort()
    list2.sort()
    
    total_diff = 0

    for i in range(len(list1)):
        num1 = list1[i]
        num2 = list2[i]
        total_diff += abs(num1 - num2)
    
    return total_diff

def main():
    list1, list2 = getInput()
    total_diff = totalDistance(list1, list2)
    print(total_diff)
    
if __name__ == "__main__":
    main()