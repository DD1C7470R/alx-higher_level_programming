#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    discovery_list = dir(hidden_4)
    for idx in range(len(discovery_list)):
        if discovery_list[idx].__contains__("__"):
            pass
        else:
            print('{}'.format(discovery_list[idx]))
