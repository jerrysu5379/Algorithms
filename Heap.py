def insert(x, heap):
    heap.append(x)
    i = len(heap) - 1
    while i > 0:
        parent = (i - 1) // 2
        if heap[parent] <= x:
            break
        heap[i] = heap[parent]
        i = parent
    heap[i] = x
    return i

def delete(heap):
    if len(heap) == 0:
        raise IndexError("delete from empty heap")
    x = heap[0]
    y = heap.pop()
    if len(heap) == 0:
        return x
    n = len(heap)
    i = 0
    while i * 2 + 1 < n:
        left = i * 2 + 1
        right = i * 2 + 2
        if right < n and heap[right] < heap[left]:
            child = right
        else:
            child = left
        if y <= heap[child]:
            break
        heap[i] = heap[child]
        i = child
    heap[i] = y
    return x

def update(x, heap, pos):
    if x < heap[pos]:
        heap[pos] = x
        while pos > 0:
            parent = (pos - 1) // 2
            if heap[parent] <= x:
                break
            heap[pos] = heap[parent]
            pos = parent
        heap[pos] = x
    else:
        heap[pos] = x
        n = len(heap)
        while pos * 2 + 1 < n:
            left = pos * 2 + 1
            right = pos * 2 + 2
            if right < n and heap[right] < heap[left]:
                child = right
            else:
                child = left
            if x <= heap[child]:
                break
            heap[pos] = heap[child]
            pos = child
        heap[pos] = x