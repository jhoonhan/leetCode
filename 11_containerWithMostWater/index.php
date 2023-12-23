<?php

declare(strict_types=1);
class Solution
{
  function maxArea(array $height)
  {
    $left = 0;
    $right = count($height) - 1;
    $max = 0;

    while ($left < $right) {
      $max = max($max, min($height[$left], $height[$right]) * ($right - $left));
      if ($height[$left] > $height[$right]) {
        $right--;
      } else {
        $left++;
      }
    }
    return $max;
  }
}

$solution = new Solution();
$solution->maxArea([2, 3, 4, 5, 18, 17, 6]);
