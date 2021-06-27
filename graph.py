graph_dict = {
	"Mumbai" : ["Paris", "Dubai"],
	"Paris" : ["Dubai", "New York"],
	"Dubai" : ["New York"],
	"New York" : ["Toronto"]
}

def get_paths(start, end, path=[]):
    path = path + [start]

    if start == end:
        return [path]

    if start not in graph_dict:
        return []

    paths = []
    for node in graph_dict[start]:
        if node not in path:
            new_paths = get_paths(node, end, path)
            for p in new_paths:
                paths.append(p)

    return paths


print(get_paths("Mumbai", "New York"))
