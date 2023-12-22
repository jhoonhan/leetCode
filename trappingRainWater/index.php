<?php

declare(strict_types=1);

class Solution
{
  function trap(array $height): int
  {
    $nums = array_fill(0, count($height), 0);
    $xleft = 0;
    $xright = 0;
    // Going right
    for ($i = 0; $i < count($height); $i++) {
      $xleft = max($xleft, $height[$i]);
      $nums[$i] = $xleft - $height[$i];
    }
    // Going left
    for ($j = count($height) - 1; $j >= 0; $j--) {
      $xright = max($xright, $height[$j]);
      if ($xleft > $xright) {
        $nums[$j] = $nums[$j] - ($xleft - $xright);
      }
    }
    return array_sum($nums);
  }
}

$solution = new Solution();
$solution->trap([0, 3, 1, 0, 2, 0, 4, 0, 1, 3]);
