#!/home/linguyiq/anaconda3/bin/python3
#Dictionary

def main():
    colors = {'1':'black','2':'red','3':'green','4':'yellow'}
    print_dict(colors)

def print_dict(x):
    for k, v in x.items(): print(f'{k}: {v}') 

if __name__ == '__main__': main()