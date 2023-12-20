<?php

declare(strict_types=1);

class Solution
{
  function candy(array $ratings): int
  {
    $nums = array_fill(0, count($ratings), 1);

    for ($i = 1; $i < count($ratings); $i++) {
      if ($ratings[$i] > $ratings[$i - 1]) {
        $nums[$i] = $nums[$i - 1] + 1;
      }
    }
    for ($i = count($ratings) - 2; $i >= 0; $i--) {
      if ($ratings[$i] > $ratings[$i + 1]) {
        $nums[$i] = max($nums[$i], $nums[$i + 1] + 1);
      }
    }

    return array_sum($nums);
  }
}


$solution = new Solution();
$solution->candy([6, 1, 2, 0, 4, 5]);
