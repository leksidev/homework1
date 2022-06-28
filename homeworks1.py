# Задача 1
import re


def domain_name(url: str) -> str:
    return re.search(r'(?<=[/|.])\w+', url).group()


assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"

# Задача 2

import ipaddress


def int32_to_ip(int32: int) -> str:
    return str(ipaddress.ip_address(int32))


assert int32_to_ip(2154959208) == "128.114.17.104"
assert int32_to_ip(0) == "0.0.0.0"
assert int32_to_ip(2149583361) == "128.32.10.1"


# Задача 3

def zeros(n: int) -> int:
    res = 0
    while n > 0:
        n //= 5
        res += n
    return res


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
assert zeros(100) == 24

# Задача 4

import itertools


def bananas(s: str) -> set:
    result = set()
    string_len = len(s)
    potential_del_coord = itertools.combinations(range(string_len), string_len - 6)
    for coord in potential_del_coord:
        s_in_list = list(s)
        for i in coord:
            s_in_list[i] = '-'

        potential_result = ''.join(s_in_list)

        if potential_result.replace('-', '') == 'banana':
            result.add(potential_result)

    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}


# Задача 5


def count_find_num(primesL: list[int], limit: int) -> list[int]:
    base = eval('*'.join(map(str, primesL)))

    if base > limit:
        return []

    results = [base]

    for prime in primesL:
        for result in results:
            result *= prime
            while result not in results and result <= limit:
                results += [result]
                result *= prime

    return [len(results), max(results)]


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
