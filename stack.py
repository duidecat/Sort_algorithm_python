def loi_stack(ngan_xep):
    print("khong co phan tu trong stack!")

def xoa_stack(ngan_xep):
    if len(ngan_xep) == 0:
        return loi_stack(ngan_xep)
    else:
        ngan_xep.pop()
        print(ngan_xep)

def peek_stack(ngan_xep):
    if len(ngan_xep) == 0:
        return loi_stack(ngan_xep)
    else:
        print(ngan_xep[-1])

def empty_stack(ngan_xep):
    if len(ngan_xep) == 0:
        return loi_stack(ngan_xep)
    else:
        if len(ngan_xep) == 0:
            return True
        elif len(ngan_xep) != 0:
            return False

def size_stack(ngan_xep):
    if len(ngan_xep) == 0:
        return loi_stack(ngan_xep)
    else:
        print(len(ngan_xep))

def display_stack(ngan_xep):
    if len(ngan_xep) == 0:
        return loi_stack(ngan_xep)
    else:
        print(ngan_xep)

if __name__ == "__main__":
    arr = []
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print(peek_stack(arr))
  
    