from typing import Dict, List, Optional
from Heap import insert, delete

class Node:
    def __init__(self, freq: int, char: Optional[str]):
        self.freq = freq
        self.char = char
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __lt__(self, other: 'Node') -> bool:
        return self.freq < other.freq

    def __le__(self, other: 'Node') -> bool:
        return self.freq <= other.freq

def hfm(text: str) -> Dict[str, str]:
    if not text:
        return {}

    # Calculate frequency of each character
    freq: Dict[str, int] = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Create a heap of nodes
    heap: List[Node] = []
    for char, frequency in freq.items():
        insert(Node(frequency, char), heap)

    # Build the Huffman tree
    while len(heap) > 1:
        left = delete(heap)
        right = delete(heap)
        new_node = Node(left.freq + right.freq, None)
        new_node.left = left
        new_node.right = right
        insert(new_node, heap)

    # Generate Huffman codes
    code: Dict[str, str] = {}
    def dfs(node: Node, path: str):
        if node.char is not None:
            code[node.char] = path
            return
        if node.left:
            dfs(node.left, path + '0')
        if node.right:
            dfs(node.right, path + '1')

    if heap:
        dfs(heap[0], '')

    return code

def main():
    text = input()
    codes = hfm(text)
    print("Huffman Codes:", codes)

if __name__ == "__main__":
    main()