def find_lowest_dist(last_elem, cur_elem, next_elem):
    if cur_elem - last_elem < next_elem - cur_elem:
        return cur_elem - last_elem
    return next_elem - cur_elem


def find_closer_el(prev_elem, cur_elem, avg_elem):
    if avg_elem - prev_elem > cur_elem - avg_elem:
        return cur_elem
    return prev_elem


def max_dist_between_angry_cows(free_sect, sect_num, ang_cows):
    free_sect.sort()
    avg_sect_num = (free_sect[-1] - free_sect[0]) / (ang_cows - 1)
    avg_elem_sum = free_sect[0]
    last_sect_with_cow = free_sect[0]
    prev_elem = free_sect[0]
    lower_dist = 0

    if ang_cows == 2:
        return avg_sect_num

    for i in range(1, sect_num - 1):
        if (
                last_sect_with_cow <= avg_elem_sum + avg_sect_num <= free_sect[i]
        ):
            avg_elem_sum += avg_sect_num
            lower_dist = find_lowest_dist(
                last_sect_with_cow,
                find_closer_el(prev_elem, free_sect[i], avg_elem_sum),
                free_sect[-1],
            )
            last_sect_with_cow = find_closer_el(prev_elem, free_sect[i], avg_elem_sum)
        prev_elem = free_sect[i]
    return lower_dist
