<?php

class Solution
{

  /**
   * @param Integer[] $citations
   * @return Integer
   */
  function hIndex($citations)
  {
    // 6
    $count = max($citations);
    $h = 0;
    for ($i = $count; $i > 0; $i--) {
      // echo ("Checking with index h: $i");
      // echo ('<br>');
      $elig = 0;
      foreach ($citations as $key) {
        if ($key >= $i) {
          $elig++;
          // echo ("$key eligible.");

          // echo (" Updating Eligible to: $elig");
          // echo ('<br>');
        }
      }
      // echo ("Checking h: $i | $elig");
      // echo ('<br>');
      if ($i <= $elig) {
        $temp = min($i, $elig);
        $h = max($h, $temp);
        // echo ("H updated: $h");
        // echo ('<br>');
      }

      // echo ('<br>');
    }
    // echo ("ended with $h");

    return $h;
  }
}

$solution = new Solution();
$solution->hIndex([1, 3, 1]);
// $solution->hIndex([3, 0, 6, 1, 5]);
