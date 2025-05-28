# Критерий Тарьяна

Остовное дерево в неориентированном взвешенном графе минимально тогда и только тогда, когда для любого ребра, не принадлежащего остову, цикл, образуемый этим ребром при добавлении к остову, не содержит рёбер тяжелее этого ребра.

# Лемма о безопасном ребре в частичном MST

Рассмотрим связный неориентированный взвешенный граф G=(V,E) с весовой функцией w:E→ℝ. Пусть G′=(V,E′)\
— подграф некоторого минимального остовного дерева G, ⟨S,T⟩ — разрез G, такой, что ни одно ребро из E′\
не пересекает разрез, а (u,v) — ребро минимального веса среди всех ребер, пересекающих разрез ⟨S,T⟩.\ Тогда ребро e=(u,v) является безопасным для G′.

# Алгоритм Краскала

1) отсортируем все ребра графа в порядке неубывания
2) заицинилизируем ответ - как пустой граф на n вершинах
3) будем итерироваться по ребрам в порядке п.1 и добавлять ребро в ответ, если оно при своем добавление не образует цикл

```
sort(edges)
make_set(n)
for e in edges:
  if leader(e.u) != leader(e.v):
    mst.add(e)
    unite(e.u, e.v)
```

# DSU

1) создадим систему из n одноэлем. подмножества
2) leader(x) - возращает главного представителя подмножества, которое содержит элемент x
3) unite(u, v) - объединяет два подмножества, которое содержит u и которое содержит v

```
make_set(n)
  for i = 0...n-1:
    p[i] = i

leader(x):
  return x == p[x] ? x : p[x] = leader(p[x])

unite(u, v):
  u = leader(u)
  v = leader(v)
  if u != v:
    if (rank[u] > rank[v]) swap(u, v)
    p[u] = v
    if (rank[v] == rank[u])
      rank[v]++
```

# Алгоритм Прима

```
visited[] = [false, false, ...]
d[] = [inf, inf, ...]
d[s] = 0
p[] = [-1, -1, ...]
p[s] = s
while true:
  u = -1
  for i in 0...n-1
    if !visited[u] && (u == -1 || d[v] > d[i]): u = i
  if (u == -1 || d[u] = inf) break
  visited[u] = true
  for (u, v) in E:
    if !visited[v] && d[v] > w(u, v):
      d[v] = w(u, v)
      p[v] = u
```

# Некоторые задачи

## Первое недвудольное ребро

Требуется найти ребро, после добавления которого изначально пустой граф станет недвудольным

```java
public class Solution {
  public static int[] leader(int[] p, int[] l, int u) {
    if (p[u] != u) {
      int[] q = leader(p, l, p[u]);
      p[u] = q[0];
      l[u] += q[1];
    }
    return new int[]{p[u], l[u]};
  }
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();
    int[] p = new int[n];
    int[] l = new int[n];
    for (int i = 0; i < n; i++) {
      p[i] = i
    }

    for (int i = 0; i < m; i++) {
      int x = sc.nextInt() - 1;
      int y = sc.nextInt() - 1;

      int[] a = leader(p, l, x);
      int[] a = leader(p, l, y);
      if (a[0] = b[0]) {
        if (a[1] % 2 == b[1] % 2) {
          System.out.println(i + 1);
          return;
        } else {
          p[a[0]] = b[0];
          l[a[0]] = a[1] % 2 == b[1] % 2 ? 1 : 0;
        }
      }
      System.out.println(-1);
    }
```

## Покраска отрезков

```java
public class Solution {
  public static int leader(int[] p, int u) {
    return p[u] == u ? p[u] : (p[u] = leader(p, p[u]));
  }
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int l = sc.nextInt();
    int n = sc.nextInt();
    int[] p = new int[l + 1];
    for (int i = 0; i <= l; i++) {
      p[i] = i;
    }
    int[] left = new int[n];
    int[] right = new int[n];
    int[] color = new int[n];
    for (int i = 0; i < n; i++) {
      left[i] = sc.nextInt();
      right[i] = sc.nextInt();
      color[i] = sc.nextInt();
    }

    int[] ans = new int[l];

    for (int i = n - 1; i >= 0; i--) {
      int l_i = left[i]
      int r = right[i];
      int c = color[i];
      for (int j = l_i; ;) {
        j = leader(p, j);
        if (j >= r)
          break
        ans[j] = c;
        p[j] = j + 1;
      }
    }
```
