# 🧠 Neurogenesis

---

## TODO

- [x] 387. First Unique Character in a String (Easy)
- [x] 242. Valid Anagram (Easy)
- [x] 392. Is Subsequence (Easy)
- [x] 796. Rotate String (Easy)
- [ ] 153. Find Minimum in Rotated Sorted Array (Medium)
- [ ] 33. Search in Rotated Sorted Array (Medium)
- [ ] 567. Permutation in String (Medium)
- [ ] 49. Group Anagrams (Medium)
- [ ] 451. Sort Characters by Frequency (Medium)
- [ ] 438. Find All Anagrams in a String (Medium)
- [ ] 443. String Compression (Medium)
- [ ] 424. Longest Repeating Character Replacement (Medium)
- [ ] 3. Longest Substring Without Repeating Characters (Medium)
- [ ] 79. Word Search (Medium)
- [ ] 139. Word Break (Medium)
- [ ] 208. Implement Trie (Prefix Tree) (Medium)
- [ ] 648. Replace Words (Medium)
- [ ] 720. Longest Word in Dictionary (Medium)
- [ ] 1268. Search Suggestions System (Medium)
- [ ] 76. Minimum Window Substring (Hard)
- [ ] 214. Shortest Palindrome (Hard)
- [ ] 212. Word Search II (Hard)

---

## 1. Input Size & Expected Complexity

| Input Size                       | Typical Constraints         | Target Time Complexity | Common Patterns                       |
| -------------------------------- | --------------------------- | ---------------------- | ------------------------------------- |
| **Very Small** (n ≤ 20)          | exponential/backtracking OK | O(2ⁿ), O(n!)           | Backtracking, brute‑force, recursion  |
| **Small–Medium** (n ≤ 10⁴)       | O(n²) sometimes acceptable  | O(n²), O(n log n)      | Two‑pointers, sorting, sliding window |
| **Medium–Large** (10⁴ ≤ n ≤ 10⁶) | O(n log n) or O(n) required | O(n log n), O(n)       | Hash‑map, two‑pointers, greedy        |
| **Huge** (n > 10⁶)               | near‑linear or better       | O(n), O(log n), O(1)   | Streaming, constant‑space, bit ops    |

> **Tip:** Always check constraints (`n`, memory, recursion depth) to pick the right complexity target.

---

## 2. Core Problem Types & Techniques

### 2.1 Sorted Array / Sequence

- **Binary Search** – O(log n)
- **Two‑Pointers** – O(n)

### 2.2 All Permutations / Subsets / Combinations

- **Backtracking** – exponential in worst case
- **DFS (with path list + choose/not choose)**

### 2.3 Trees

- **DFS** (preorder/inorder/postorder)
- **BFS** (level order)

### 2.4 Graphs

- **DFS** – recursion or stack
- **BFS** – queue

### 2.5 Linked Lists

- **Two‑Pointers** (slow & fast)
- **Dummy head technique** for insertion/deletion

### 2.6 No Recursion Allowed

- **Explicit Stack** – simulate recursion

### 2.7 In‑Place Requirement

- **Value Swapping**
- **Bit‑packing / Tagged pointers** (store extra state)

### 2.8 Maximum / Minimum Subarray or Subsequence

- **Dynamic Programming** – memo table or optimized rolling variables
- **Sliding Window** – O(n)

### 2.9 Top / Kth Smallest / Largest

- **Heap (min/max)** – O(n + k log n)
- **QuickSelect** – average O(n)

### 2.10 Common String Problems

- **Hash‑Map (frequency count)**
- **Trie** – prefix matching, autocomplete

### 2.11 When in Doubt

- **Hash‑Map / Hash‑Set** – O(1) average lookups, O(n) space
- **Sort + Scan** – O(n log n) time, O(1)–O(n) space

---

## 3. Pattern & Constraint Checklist

1. **Check Input Size**

   - If n ≤ 20 → Backtracking, brute‑force
   - If n ~10³–10⁴ → O(n²) algorithms might pass; prefer O(n log n)
   - If n ≥ 10⁵ → aim for O(n) or O(n log n)

2. **Space Constraints**

   - In‑place required → avoid extra arrays/hash maps
   - Extra O(n) space allowed → use maps, sets, auxiliary arrays

3. **Recursion Depth**

   - Mind language recursion limits (e.g., Python ~1 000)
   - Convert to iterative + stack if depth too high

4. **Ordered vs. Unordered**

   - Sorted input → binary search, two‑pointers
   - Unsorted → sort first or use hash maps

5. **Mutability**

   - Read‑only input → can’t sort in place, copy if needed
   - Modifiable → sort or mark visited

6. **Graph Connectivity / Cycles**
   - If detecting cycles → DFS + visited set / union‑find
   - If shortest paths → BFS (unweighted) or Dijkstra (weighted)

---
