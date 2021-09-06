from typing import List
import re

def get_arguments_from_pattern(self, pattern: str) -> List[str]:
    result = []
    addresses = re.findall(r'\${\w+}', pattern)
    for address in addresses:
        result.append(re.sub('[${}]', '', address))
    return result


def build_message(pattern: str, arguments: List[str]) -> str:
    message = pattern
    for argument in arguments:
        message = re.sub('\${\w+}', argument, message, 1)
    return message


print(build_message("Hi! My name is ${name}! I'm ${age} years old!", ['Mike', '16']))