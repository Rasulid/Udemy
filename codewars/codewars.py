# import string

# quote = string.capwords


# def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     return numbers[0] + numbers[1]


def better_than_average(class_points, your_points):
    lcp =len(class_points)
    scp =sum(class_points)
    sac =lcp / scp
    
    if sac < your_points:
        return True
    else :
        return False


s=better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69)
print(s)