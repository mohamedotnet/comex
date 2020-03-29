first_key = "\x0e\x3d\x2a\x21\x0b\x2d\x28\x3d\x2a\x0b\x3d\x13\x2a\x3d\x2c\x13\x3d\x21"
second_key = "\x68\x77\x76\x70\x7c\x77\x76\x61\x4c\x60\x67\x76\x75\x72\x7d\x7c\x22\x22\x2b\x4c\x32\x32\x4c\x6e"
key = "VerySuperSeKretKey"

result = []
result_two = []
for i in range(0, 126):
    first_result = ""
    for k in first_key:
        first_result += chr(ord(k) ^ i)
    result.append(first_result)

for i in range(0, 126):
    second_result = ""
    for k in second_key:
        second_result += chr(ord(k) ^ i)
    result_two.append(second_result)

for output in result:
    print(output)
