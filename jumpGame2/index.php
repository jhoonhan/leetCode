<?php
class Solution
{

  /**
   * @param int[] $nums
   * @return Boolean
   */
  function jump($nums)
  {
    $goal = count($nums) - 1;
    $count = 0;
    $i = count($nums) - 1;
    $potential = 0;

    while ($i > 1) {
      for ($j = $i; $j > 0; $j--) {
        if ($nums[$j] + $j >= $i) {
          $potential = $j;
          echo ("Updated Poten: $potential | $nums[$potential]<br>");
        }
        $i = $potential;
        echo ("Updated i: $i<br>");
      }
      $count++;
    }
    echo ("Count: $count");






    // if ($goal === 0) {
    //   return true;
    // } else {
    //   return false;
    // }
    return $count;
  }
}


$solution = new Solution();
$solution->jump([2, 3, 1, 1, 4]);
// $solution->jump([1, 1, 1, 1]);
