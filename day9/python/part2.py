import sys

def get_empty_spaces(disk, start=0):
    while start < len(disk):
        next_free = disk.index(".", start)
        end_free = next_free
        for idx in range(next_free, len(disk)):
            if disk[idx] == ".":
                end_free = idx
            else:
                break

        yield ((end_free - next_free) + 1 ,next_free, end_free+1)
        start = end_free + 1


def compact(disk, file_info):
    file_len, (fstart, fend) = file_info
    for (free_len, free_start, free_end) in get_empty_spaces(disk):
        if free_start >= fstart:
            continue

        if file_len <= free_len:
            disk[free_start:free_start + file_len] = disk[fstart:fend]
            disk[fstart:fend] = ['.'] * file_len
            break

def checksum(disk):
    total = 0
    for pos, value in enumerate(disk):
        if value != ".":
            total += pos * value
    return total

def main():
    disk_desc = sys.stdin.readline().strip()
    if len(disk_desc) % 2 != 0:
        disk_desc += "0"

    files = {}

    disk = []
    for idx, (count, empty) in enumerate(zip(disk_desc[::2], disk_desc[1::2])):
        count = int(count)
        empty = int(empty)
        files[idx] = (count, (len(disk), len(disk) + count))
        disk += [ idx ] * count
        disk += [ '.' ] * empty
    
    new_disk = list(disk)
    lidx = 0
    ridx = len(new_disk) - 1
    
    file_ids = sorted(list(files.keys()), reverse=True)
    for file_id in file_ids:
        compact(new_disk, files[file_id])

    cs = checksum(new_disk)
    print(cs)

    

        

if __name__ == "__main__":
    main()

