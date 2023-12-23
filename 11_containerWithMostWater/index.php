<?php

declare(strict_types=1);
class Solution
{
  function maxArea(array $height)
  {
    $maxLeft = 0;
    $leftIndex = 0;
    $maxVal = [0, 0];
    $max = 0;
    for ($i = 0; $i < count($height); $i++) {
      echo ($height[$i]);
      echo ('<br>');
      echo ("Left: $leftIndex | $maxLeft");

      echo ('<br>');
      echo ("Comparing $maxLeft | $height[$i]");
      echo ('<br>');

      $potential = min($height[$i], $maxLeft) * ($i - $leftIndex);
      echo ("Potential = $potential");
      echo ('<br>');

      // Potent 2 checker
      if (isset($height[$i - 1])) {
        $aang = $height[$i];
        echo ("Comparing $aang | $height[$i]");
        echo ('<br>');
        $potential2 = min($height[$i - 1], $height[$i]) * 1;

        echo ("Potential 2 = $potential2");
        echo ('<br>');
        if ($potential2 > $potential) {
          $maxLeft = $height[$i - 1];
          $leftIndex = $i;
          $potential = $potential2;
        }
      }

      // max logger
      if ($potential > $max) {
        $max = $potential;
        $maxVal = [$maxLeft, $height[$i]];
      }
      echo (json_encode($maxVal));
      echo ('<br>');


      echo ('<br>');
    }
  }
}

$solution = new Solution();
$solution->maxArea([3, 5, 1, 3, 4, 5, 4, 1]);
