<?php
class Solution
{

  /**
   * @param int[] $nums
   * @return Boolean
   */
  function jump($nums)
  {
    $count = 0;
    $l = $r = 0;
    while ($r < count($nums) - 1) {
      $farthest = 0;
      for ($i = $l; $i <= $r; $i++) {
        $farthest = max($farthest, $i + $nums[$i]);
      }
      $l = $r + 1;
      $r = $farthest;
      $count++;
    }
    echo ($count);
    return $count;
  }
}


$solution = new Solution();
// $solution->jump([2, 3, 1, 1, 4]);
$solution->jump([1, 1, 1, 1]);
