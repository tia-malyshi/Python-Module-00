def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))

    def count(n):
        if n == x:
            print("Day ", n)
            print("Harvest time!")
            return
        else:
            print("Day ", n)
        count(n + 1)
    count(1)
