def bubble_sort(exam_list):
    print('버블 정렬')
    for _ in range(len(exam_list)-1):
        for i in range(len(exam_list)):
            if not i == 4:
                if exam_list[i] > exam_list[i+1]:
                    temp = exam_list[i]
                    exam_list[i] = exam_list[i+1]
                    exam_list[i+1] = temp
    return exam_list


def selection_sort(exam_list):
    print('선택 정렬')
    length = len(exam_list)
    for i in range(length):
        for j in range(i, length):
            if exam_list[j] == min(exam_list[i:length]):
                temp = exam_list[0 + i]
                exam_list[0 + i] = exam_list[j]
                exam_list[j] = temp
    return exam_list


def injection_sort(exam_list):
    print('삽입 정렬')
    length = len(exam_list)
    while (exam_list[length-1] != max(exam_list) or
           exam_list[0] != min(exam_list)):
        for i in range(length-1):
            while exam_list[i+1] < exam_list[i]:
                temp = exam_list[i + 1]
                del exam_list[i+1]
                exam_list.insert(i, temp)
    return exam_list


def merge_sort(exam_list):
    print('병합 정렬')
    if len(exam_list) <= 1:
        return exam_list

    half = len(exam_list) // 2
    part1 = exam_list[:half]
    part2 = exam_list[half:]
    part1 = merge_sort(part1)
    part2 = merge_sort(part2)
    print(part1)
    print(part2)
    return merge(part1, part2)


def merge(part1, part2):
    result = []
    part1_idx, part2_idx = 0, 0

    while part1_idx < len(part1) and part2_idx < len(part2):
        if part1[part1_idx] < part2[part2_idx]:
            result.append(part1[part1_idx])
            part1_idx += 1
        else:
            result.append(part2[part2_idx])
            part2_idx += 1

    result.extend(part1[part1_idx:])
    result.extend(part2[part2_idx:])

    return result

