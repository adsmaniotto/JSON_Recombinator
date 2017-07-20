import json, os, sys
os.chdir("C:/users/212615348/desktop/json_recombinator/")

data_in = sys.argv[1]

# if argument is JSON, read in
if data_in[-5:] == ".json":
    with open(data_in, 'r') as data_file:
        json_data = data_file.read()
    d = json.loads(json_data)

d2 = d
if type(d2[0]) == dict:
    # find all unique keys
    all_dicts = {}
    for x in d2:
        all_dicts.update(x)
    all_keys = list(all_dicts.keys())
    
    # replace missing key-value pairs w/ nulls
    for i in range(len(d2)):
        for index in range(len(all_keys)):
            if any(all_keys[index] in k for k in d2[i])==False:
                d2[i].update({all_keys[index] : None})
               
    # now that we have all unique keys, find values for each dict
    lst = []
    output = dict()
    for j in all_keys:
        # initialize key-value pairs for each unique keys
        output[j] = []
        for k in range(len(d2)):
            # append the values for each unique key to a list
            output[j].append(d2[k].get(j))

# solution for a list of lists
if type(d2[0]) == list:
    lst = []
    for x in range(len(d2[0])):
        lst.append([item[x] for item in d2])
    output = {l[0]:l[1:] for l in lst}
    
print("Input: {}".format(json_data))
print("Output: {}".format(output))