
def main():

    name1 = input("Enter flavor one: ")
    name2 = input("Enter flavor two: ")
    name3 = input("Enter flavor three: ")
    print()

    if name2 > name1 < name3:
        print(name1)
        if name2 < name3:
            print(name2)
            print(name3)
        else:
            print(name3)
            print(name2)
    elif name1 > name2 < name3:
        print(name2)
        if name1 < name3:
            print(name1)
            print(name3)
        else:
            print(name3)
            print(name1)
    else:
        print(name3)
        if name1 < name2:
            print(name1)
            print(name2)
        else:
            print(name2)
            print(name1)
    
if __name__ == '__main__':
    main()

'''
def main():
    # delete the 'pass' command, then begin coding below:
    pass



if __name__ == '__main__':
    main()
'''
