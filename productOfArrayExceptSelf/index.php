<?php

declare(strict_types=1);

class Solution
{

  /**
   * @param int[] $nums
   * @return int[]
   */
  function productExceptSelf($nums)
  {
    $res = [];
    $res3 = [];
    $counter = 1;
    $counter2 = 1;
    $rNums = array_reverse($nums);
    // change it to while loop maybe

    $i = 0;
    $j = count($nums) - 1;
    while ($i < count($nums) && $j >= 0) {

      if (isset($nums[$i - 1])) {
        $counter = $counter * $nums[$i - 1];
      }
      array_push($res, $counter);

      if (isset($rNums[$j - 1])) {
        $counter2 = $counter2 * $rNums[$j - 1];
      }
      echo ($counter2);
      echo ('<br>');

      // $res[$i] = $res[$i] * $res
      array_push($res3, $res[$i] * $counter2);

      $i++;
      $j--;
    }


    print_r($res);
    echo ('<br>');

    print_r($res3);
    echo ('<br>');
  }
}


$solution = new Solution();
$solution->productExceptSelf([1, 2, 3, 4]);
