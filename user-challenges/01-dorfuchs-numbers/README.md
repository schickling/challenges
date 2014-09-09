## Dorfuchs numbers
Some time ago, the famous artist DorFuchs posted a riddle on his Facebook page:

Find all distinct numbers consisting of exactly five digits, where the five digits have to be five successive digits between 0 and 9.
Numbers with leading zeros should not be included.

Format the output as a sorted list, including numbering.

## Example

1: 10234
2: 10243
3: 10324
...
694: 98675
695: 98756
696: 98765

## Objective
This is a golf challenge - the shortest solution wins.

## Checking

You can pipe your solutions output to a file:

```bash
$ ./base.py > test.txt
```

And then compare it with the correct solution:

```bash
$ diff test.txt solution.txt
```

The number of characters can be checked with `wc`:

```bash
$ wc -c base.py
```

## Solutions

| Filename    | Language | Characters | Bytes (compiled) | Comment                                                                         |
| ----------- | -------- | ---------- | ---------------- | ------------------------------------------------------------------------------- |
| Scala.scala | Scala  | 188 | ?                |                                                                                 |
| base.py     | Python | 478 | 570 | Un-golfed version with comments                                                 |
| golfed-1.py | Python | 174 | 505 | Golfed version of base.py. Only comments and docstrings and spaces were removed |
| golfed-2.py | Python | 148 | 485 | Based on golfed-1.py. Function inlining; Variable renaming     |
| base.hs     | Haskell | 808 | 1364245 | un-golved version with comments |
| golfed-1.hs | Haskell | 340 | 1364116 | Golfed version of base.hs. Only comments and whitespaces were removed |

Note that you can compile Python with `python -m compileall .`.

## Additional
PS: http://youtu.be/tPfnEByx9r0