from sys import stdin
from heapq import heappush, heappop
from collections import Counter


class BinTree(object):
    """A binary tree node used by Huffman coding."""

    def __init__(self, label=None, left=None, right=None, min_char=None):
        self.label = label
        self.left = left
        self.right = right
        self.min_char = min_char

    def is_leaf(self):
        return self.left is None and self.right is None


def _char_key(ch):
    if ch == " ":
        return (0, "")
    if ch == ",":
        return (1, "")
    if ch == ".":
        return (2, "")
    if ch.isalpha():
        return (3, ch)
    return (4, ch)


def _min_char(a, b):
    return a if _char_key(a) <= _char_key(b) else b


class _HeapItem(object):
    """Wraps a tree with its frequency so it can live in a heap."""

    __slots__ = ("freq", "tree", "min_key", "order")

    def __init__(self, freq, tree, order):
        self.freq = freq
        self.tree = tree
        self.min_key = _char_key(tree.min_char)
        self.order = order

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        if self.min_key != other.min_key:
            return self.min_key < other.min_key
        return self.order < other.order


def _build_huffman_tree(freqs):
    if not freqs:
        return None

    heap = []
    order = 0
    for ch, f in freqs.items():
        heappush(heap, _HeapItem(f, BinTree(label=ch, min_char=ch), order))
        order += 1

    if len(heap) == 1:
        # Single-symbol edge case: create a dummy parent
        only = heappop(heap)
        return BinTree(left=only.tree, right=None, min_char=only.tree.min_char)

    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        if _char_key(a.tree.min_char) <= _char_key(b.tree.min_char):
            left_tree = a.tree
            right_tree = b.tree
        else:
            left_tree = b.tree
            right_tree = a.tree
        parent_min = _min_char(left_tree.min_char, right_tree.min_char)
        parent = BinTree(left=left_tree, right=right_tree, min_char=parent_min)
        heappush(heap, _HeapItem(a.freq + b.freq, parent, order))
        order += 1

    return heappop(heap).tree


def _build_codes(node, prefix="", codes=None):
    if codes is None:
        codes = {}
    if node is None:
        return codes
    if node.is_leaf():
        # Single-symbol case ends here
        codes[node.label] = prefix if prefix else "0"
        return codes
    if node.left is not None:
        _build_codes(node.left, prefix + "0", codes)
    if node.right is not None:
        _build_codes(node.right, prefix + "1", codes)
    return codes


class HuffmanCoder(object):
    """Huffman encoder that can add strings and encode them to binary."""

    def __init__(self):
        self._freqs = Counter()
        self._tree = None
        self._codes = None

    def add_string(self, s):
        """Updates frequencies with a new string and rebuilds codes."""
        self._freqs.update(s)
        self._tree = _build_huffman_tree(self._freqs)
        self._codes = _build_codes(self._tree)

    def encode(self, s):
        """Encodes a string to its Huffman binary representation."""
        if not s:
            return ""
        if self._codes is None:
            # Build from the string itself if no prior data
            self.add_string(s)
        return "".join(self._codes[ch] for ch in s)

    def codes(self):
        return dict(self._codes) if self._codes is not None else {}


def huffman_encode(s):
    coder = HuffmanCoder()
    coder.add_string(s)
    return coder.encode(s), coder.codes()


def main():
    # Reads all input, encodes it, prints binary and code table
    data = stdin.read()
    data = data.rstrip("\n")
    if not data:
        return
    binary, codes = huffman_encode(data)
    print(binary)
    for ch in sorted(codes.keys(), key=_char_key):
        print(f"{repr(ch)}: {codes[ch]}")


if __name__ == "__main__":
    main()
    
