import re


def parser():
    template_path = "/comex/templates/comex/createNetwork.html"
    names_path = "C:\\Users\\DELL\\PycharmProjects\\comex\\comex\\helper\\names.txt"

    names = []
    with open(template_path, "r") as create_network:
        data = create_network.read()

    input_tags = re.findall("<input ([a-z]*=\".*\")*>", data)[1:]
    select_tags = re.findall("<select ([a-z]*=\".*\")*>", data)

    for tag in input_tags:
        names.append(re.findall("(name=\".*\")", tag)[0])

    for tag in select_tags:
        names.append(re.findall("(name=\".*\")", tag)[0])

    with open(names_path, "w+") as output_file:
        output_file.write('\n'.join(names))


parser()



