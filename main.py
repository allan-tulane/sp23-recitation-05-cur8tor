import random, time, sys
import tabulate

sys.setrecursionlimit(100000)

def qsort(a, pivot_fn):
    if len(a) == 0:
      return a
    else:
      p = pivot_fn(a)
      l = list(filter(lambda e: e < p, a))
      m = list(filter(lambda e: e == p, a))
      h = list(filter(lambda e: e > p, a))
      q1, q2 = qsort(l, pivot_fn), qsort(h, pivot_fn)
      return q1 + m + q2

def time_search(sort_fn, mylist):
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000

def compare_sort(sizes=[25, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]):
    qsort_fixed_pivot = lambda x: qsort(x, lambda y: y[0])
    qsort_random_pivot = lambda x: qsort(x, lambda y: random.choice(y))
    tim_sort = sorted
    result = []
    for size in sizes:
        mylist = list(range(size))
        # shuffle sorted list
        random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(tim_sort, mylist)
        ])
    return result

def print_results(results):
    print(tabulate.tabulate(results,
                            headers=['n [unsorted]', 'qsort-fixed-pivot', 'qsort-random-pivot', 'tim-sort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()