<?php
class Solution
{

  /**
   * @param int[] $nums
   * @return Boolean
   */
  function canJump($nums)
  {
    $goal = count($nums);
    $i = 0;

    while ($i < count($nums)) {
      $slicedArray = array_slice($nums, $i + 1, $nums[$i]);
      $goal = count(array_slice($nums, $i + 1));
      if (count($nums) === 1) {
        return true;
      }

      if (count($slicedArray) === 0) {
        echo ('fail');
        return false;
      }
      if ($nums[$i] >= $goal) {
        echo ('pass');
        return true;
      }
      $max = max($slicedArray);
      $indeces = array_keys($nums, $max);
      $maxIndex = end($indeces);
      echo ($maxIndex);





      $i = $maxIndex;
    }
  }
}


$solution = new Solution();
$solution->canJump([1, 1, 1, 1]);
