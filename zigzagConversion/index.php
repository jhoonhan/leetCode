<?php

declare(strict_types=1);

// count = 21 | gap = 8 | row = 5 | col = 3
// 0         8         16
// 1      7  9      15 17
// 2    6   10    14   18
// 3  5     11  13     19
// 4        12         20

// 

// count = 25 | gap = 12 | row = 7 | col = 3
// 0             12           24
// 1          11 13         23
// 2        10   14       22
// 3      9      15     21
// 4    8        16   20
// 5  7          17 19
// 6             18

// Input: s = "012345678", numRows = 4
// Output: "PINALSIGYAHRPI"
// Explanation:




// count = 19 | gap = 6  | row = 4 | col = 3 + 1
// A      G     M     S
// B    F H   L N   R 
// C  E   I K   O Q
// D      J     P

// count = 10 | gap = 4 | row = 3 | col = 2 + 1
// A     E     I
// B  D  F  H  J
// C     G

// count = 3 | gap = 1 | row = 2 | col = 1 + 1
// A  C
// B

class Solution
{
  function convert(string $s, int $numRows): string
  {
    $str = "";
    $chars = str_split($s);
    $count = strlen($s);
    $gap = max(1, 2 * $numRows - 2);
    $numCols = max(1, (int) ($count / $numRows + 1));

    for ($i = 0; $i < $numRows; $i++) {
      for ($j = 0; $j < $numCols; $j++) {
        // before
        if ($i !== 0 and $i !== $numRows - 1 and isset($chars[$i + ($j * $gap) - (2 * $i)])) {
          $str .= $chars[$i + ($j * $gap) - (2 * $i)];
        }
        // og
        if (isset($chars[$i + $j * $gap])) {
          $str .= $chars[$i + $j * $gap];
        }
      }
    }
    return $str;
  }
}



$solution = new Solution();
$solution->convert("ABC", 2);
// $solution->convert("ABCDEFGHIJ", 3);
