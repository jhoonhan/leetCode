<?php

class Solution
{

  /**
   * @param Integer[] $citations
   * @return Integer
   */
  // Works but slow
  // function hIndex($citations)
  // {
  //   $count = max($citations);
  //   $h = 0;
  //   for ($i = $count; $i > 0; $i--) {
  //     $elig = 0;
  //     foreach ($citations as $key) {
  //       if ($key >= $i) {
  //         $elig++;
  //       }
  //     }
  //     if ($i <= $elig) {
  //       $temp = min($i, $elig);
  //       $h = max($h, $temp);
  //     }
  //   }

  //   return $h;
  // }


  ////////
  // Binary search
  function hIndex($citations)
  {
    sort($citations);
    print_r($citations);

    // check for empty array 
    if (count($citations) === 0) return false;
    $low = 0;
    $high = count($citations) - 1;
    $target = 3;

    while ($low <= $high) {

      // compute middle index 
      $mid = floor(($low + $high) / 2);


      // element found at mid 
      if ($citations[$mid] == $target) {
        echo ("aaang");

        return true;
      }

      if ($target < $citations[$mid]) {
        // search the left side of the array 
        $high = $mid - 1;
      } else {
        // search the right side of the array 
        $low = $mid + 1;
      }
    }

    // If we reach here element x doesnt exist 
    return false;
  }
}

$solution = new Solution();
// $solution->hIndex([1, 3, 1]);
$solution->hIndex([3, 0, 6, 1, 5]);
