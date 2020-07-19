#1 Реалізувати сортування бульбашкою

def bubble_sorting(lst: list):
    swapper = True
    while swapper:
        swapper = False
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapper = True
    
    return lst

#2 Реалізувати швидке сортування
def partition(nums, low, high):  
    # Обираємо середній елемент опорним 

    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j #виходимо з циклу з індексом j

            # переставляємо елементи, менші за опорний, наліво; більші - направо
            # також на цьому моменті в рекурсії збираємо масив
        nums[i], nums[j] = nums[j], nums[i]

       
def quick_sorting(lst):  
    def _quick_sort(items, low, high):
        if low < high:
            # split_index - це наш j 
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(lst, 0, len(lst) - 1)

    return lst


if __name__ == '__main__' :

    nums_1 = [1, 2, 88, 22, 13, 5, 5, -4, 0]
    print ('Here is \'Bubble Sorting\':', bubble_sorting(nums_1))
    nums_2 = [19, -19, 0, 7, 66, -5, -5, 89, 44, 2]
    print ('Here is \'Quick Sorting\':', quick_sorting(nums_2))