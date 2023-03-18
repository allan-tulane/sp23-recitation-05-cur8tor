# CMPS 2200 Reciation 5
## Answers

**Name:** Tanner Martz

Place all written answers from `recitation-06.md` here for easier grading.

- **1b.**
I checked out the running times of different sorting algorithms, such as the Quicksort variants and selection sort, on random and already sorted lists. I compared them to their theoretical time complexities.

For random lists, Quicksort with a random pivot was faster than Quicksort with a fixed pivot. The Quicksort methods had O(n log n) behavior, while selection sort was slower with O(n^2) behavior. When I used already sorted lists, the fixed pivot Quicksort got even slower, showing O(n^2) behavior, but the random pivot Quicksort still had that cool O(n log n) behavior.

- **1c.**
I compared the quickest sorting method I found (Quicksort with random pivot) to Python's own sorting function (Timsort), and turns out Timsort is even faster in both cases (random and sorted lists). Timsort is this adaptive sorting algorithm that's pretty smart, as it takes advantage of already ordered parts of the list, making it quicker in real-life situations compared to other O(n log n) sorting algorithms.

Sorting runtime data:
|   n [sorted] |   qsort-fixed-pivot |   qsort-random-pivot |   tim-sort |
|--------------|---------------------|----------------------|------------|
|           25 |               0.170 |                0.082 |      0.001 |
|           50 |               0.333 |                0.155 |      0.001 |
|          100 |               1.076 |                0.332 |      0.001 |
|          200 |               5.085 |                0.866 |      0.003 |
|          500 |              27.164 |                1.970 |      0.005 |
|         1000 |             103.311 |                4.370 |      0.009 |
|         2000 |             407.973 |                8.261 |      0.014 |
|         5000 |            2636.710 |               24.484 |      0.040 |
|        10000 |           10573.152 |               67.091 |      0.080 |
|        20000 |           49223.055 |              108.348 |      0.163 |

|   n [unsorted] |   qsort-fixed-pivot |   qsort-random-pivot |   tim-sort |
|----------------|---------------------|----------------------|------------|
|             25 |               0.142 |                0.085 |      0.002 |
|             50 |               0.139 |                0.176 |      0.003 |
|            100 |               0.275 |                0.347 |      0.007 |
|            200 |               0.598 |                0.664 |      0.014 |
|            500 |               1.715 |                1.946 |      0.041 |
|           1000 |               3.650 |                4.519 |      0.087 |
|           2000 |               8.062 |               10.079 |      0.188 |
|           5000 |              22.088 |               25.179 |      0.517 |
|          10000 |              46.243 |               52.512 |      1.086 |
|          20000 |             103.836 |              108.360 |      2.622 |