import sys

def compact(disk, lidx=0, ridx=None):
    ridx = ridx or len(disk) - 1
    if ridx <= lidx or lidx >= len(disk) or ridx < 0:
        raise ValueError("Done")
    
    # Find the next free spot
    next_free = disk.index('.', lidx, ridx)

    # Swap the values
    disk[next_free] = disk[ridx]
    disk[ridx] = '.'

    return (next_free, ridx-1)
    
    #print(''.join([str(x) for x in new_disk]))
    #return compact(new_disk, next_free, ridx-1)

def checksum(disk):
    total = 0
    for pos, value in enumerate((x for x in disk if x != '.')):
        total += pos * value
    return total

def main():
    disk_desc = sys.stdin.readline().strip()
    if len(disk_desc) % 2 != 0:
        disk_desc += "0"

    disk = []
    for idx, (count, empty) in enumerate(zip(disk_desc[::2], disk_desc[1::2])):
        disk += [ idx ] * int(count)
        disk += [ '.' ] * int(empty)
    
    #print(''.join([str(x) for x in disk]))

    new_disk = list(disk)
    lidx = 0
    ridx = len(new_disk) - 1
    
    while True:
        try:
            (lidx, ridx) = compact(new_disk, lidx, ridx)
        except ValueError:
            break
    #print(''.join([str(x) for x in new_disk]))
    cs = checksum(new_disk)
    print(cs)

    

        

if __name__ == "__main__":
    main()

