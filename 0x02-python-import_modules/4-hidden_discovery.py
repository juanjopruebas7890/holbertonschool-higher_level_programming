#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import hidden_4
    for p in dir(hidden_4):
        if p[:2] != "__":
            print(p)
