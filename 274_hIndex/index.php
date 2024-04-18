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
    rsort($citations);
    $left = 0;
    $right = count($citations) - 1;

    while ($left <= $right) {
      $mid = $left + floor(($right - $left) / 2);
      echo ("$left | $mid | $right");
      echo ('<br>');


      if ($citations[$mid] === $mid + 1) {
        return $mid + 1;
      } elseif ($mid < $citations[$mid]) {
        $left = $mid + 1;
        echo ("Left updated to: $left");
        echo ('<br>');
      } else {
        $right = $mid - 1;
        echo ("Right updated to: $right");
        echo ('<br>');
      }
    }
    echo ("Final left: $left");
    echo ('<br>');

    return $left;
  }
}

$solution = new Solution();
// $solution->hIndex([1, 3, 1]);
$solution->hIndex([100, 100, 100, 100, 4, 0, 0, 0, 0]);
