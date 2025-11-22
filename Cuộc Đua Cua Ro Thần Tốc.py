def initials(n):
    m = n.split()
    result = ''
    for i in m:
        result += i[0].upper()
    return result

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        name = input().strip()
        country = input().strip()
        time_str = input().strip()
        hour, minute = map(int, time_str.split(":"))
        delta_time = (hour - 6) + (minute / 60)
        v = 120 / delta_time
        position = initials(country) + initials(name)
        print(f"{position} {name} {country} {int(v)} km/h")