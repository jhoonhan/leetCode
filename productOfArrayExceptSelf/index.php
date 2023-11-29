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
    $counter = 1;
    // change it to while loop maybe
    for ($i = 0; $i < count($nums); $i++) {
      # code...
      if (isset($nums[$i - 1])) {
        $counter = $counter * $nums[$i - 1];
      }
      array_push($res, $counter);
    }
    $counter = 1;

    print_r($res);
    echo ('<br>');
  }
}


$solution = new Solution();
$solution->productExceptSelf([1, 2, 3, 4]);
