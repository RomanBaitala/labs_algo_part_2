def find_lowest_between_two(last_elem, cur_elem, next_elem):
    if cur_elem - last_elem < next_elem - cur_elem:
        return cur_elem - last_elem
    return next_elem - cur_elem


def find_closer_elem_to_value(prev_elem, cur_elem, avg_elem):
    if avg_elem - prev_elem > cur_elem - avg_elem:
        return cur_elem
    return prev_elem


def max_dist_between_angry_cows(free_section, section_num, ang_cows):
    free_section.sort()

    max_section_number, min_section_number = (
        free_section[section_num - 1],
        free_section[0],
    )
    avg_section_num = (max_section_number - min_section_number) / (ang_cows - 1)

    avg_elem_sum = free_section[0]
    last_section_with_cow = free_section[0]
    prev_elem = free_section[0]
    lower_dist = 0

    if ang_cows == 2:
        return max_section_number - min_section_number

    for i in range(1, section_num - 1):
        if (
            last_section_with_cow <= avg_elem_sum + avg_section_num
            and avg_elem_sum + avg_section_num <= free_section[i]
        ):
            avg_elem_sum += avg_section_num
            if avg_elem_sum - free_section[i] < avg_elem_sum - prev_elem:

                lower_dist = find_lowest_between_two(
                    last_section_with_cow,
                    find_closer_elem_to_value(prev_elem, free_section[i], avg_elem_sum),
                    max_section_number,
                )
                last_section_with_cow = free_section[i]
            else:
                lower_dist = find_lowest_between_two(
                    last_section_with_cow,
                    find_closer_elem_to_value(prev_elem, free_section[i], avg_elem_sum),
                    max_section_number,
                )
                last_section_with_cow = prev_elem
        prev_elem = free_section[i]
    return lower_dist
