<?php
class Solution
{

  /**
   * @param int[] $nums
   * @return Boolean
   */
  function canJump($nums)
  {
    $goal = count($nums) - 1;

    for ($i = count($nums) - 1; $i >= 0; $i--) {
      echo ("Index: $i | Num: $nums[$i] | Total: $i + $nums[$i] | Goal: $goal <br>");
      if ($i + $nums[$i] >= $goal) {
        $goal = $i;
      }
    }
    echo ("Final goal: $goal");

    if ($goal === 0) {
      return true;
    } else {
      return false;
    }
  }
}


$solution = new Solution();
$solution->canJump([3, 1, 0, 1, 4]);
