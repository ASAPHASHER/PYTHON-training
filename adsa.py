# Custom Iterable and Generator
class Countdown:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        val = self.n
        self.n -= 1
        return val

def simple_generator(n):
    while n > 0:
        yield n
        n -= 1


# Heap Example
import heapq
def heap_example(nums):
    heapq.heapify(nums)
    return heapq.heappop(nums)


# Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.end


# Segment Tree (range sum)
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, idx, left, right):
        if left == right:
            self.seg[idx] = arr[left]
            return
        mid = (left + right) // 2
        self.build(arr, idx*2+1, left, mid)
        self.build(arr, idx*2+2, mid+1, right)
        self.seg[idx] = self.seg[idx*2+1] + self.seg[idx*2+2]

    def query(self, idx, left, right, l, r):
        if r < left or l > right:
            return 0
        if l <= left and right <= r:
            return self.seg[idx]
        mid = (left + right) // 2
        return self.query(idx*2+1, left, mid, l, r) + self.query(idx*2+2, mid+1, right, l, r)


# Suffix Array
def suffix_array(s):
    return sorted(range(len(s)), key=lambda i: s[i:])


# Graph Algorithm (Dijkstra)
def dijkstra(graph, start):
    pq = [(0, start)]
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for nxt, w in graph[node]:
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(pq, (nd, nxt))
    return dist


# Dynamic Programming (Longest Increasing Subsequence)
def lis(nums):
    dp = []
    import bisect
    for x in nums:
        i = bisect.bisect_left(dp, x)
        if i == len(dp):
            dp.append(x)
        else:
            dp[i] = x
    return len(dp)


# LRU Cache
class LRU:
    def __init__(self, capacity):
        from collections import OrderedDict
        self.capacity = capacity
        self.cache = OrderedDict()
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# Example usage
if __name__ == "__main__":
    print(list(Countdown(5)))
    print(list(simple_generator(5)))
    print(heap_example([5,1,3,2]))
    t = Trie()
    t.insert("cat")
    print(t.search("cat"))
    st = SegmentTree([1,3,5,7,9])
    print(st.query(0,0,4,1,3))
    print(suffix_array("banana"))
    graph = {'A':[('B',1),('C',4)], 'B':[('C',2),('D',5)], 'C':[('D',1)], 'D':[]}
    print(dijkstra(graph,'A'))
    print(lis([10,9,2,5,3,7,101,18]))
    cache = LRU(2)
    cache.put(1,1)
    cache.put(2,2)
    print(cache.get(1))
    cache.put(3,3)
    print(cache.get(2))
