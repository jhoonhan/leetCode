<?php

declare(strict_types=1);

class Solution
{
  function minSubArrayLen(int $target, array $nums): int
  {
    $l = 0;
    $total = 0;
    $res = count($nums) + 1;

    for ($r = 0; $r < count($nums); $r++) {
      $total += $nums[$r];
      while ($total >= $target) {
        $res = min($r - $l + 1, $res);
        $total -= $nums[$l];
        $l++;
      }
    }

    if ($res === count($nums) + 1) {
      return 0;
    } else {
      return $res;
    }
  }
}

$solution = new Solution();
// $solution->minSubArrayLen(7, [2, 16, 14, 15]);
$solution->minSubArrayLen(213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]);
