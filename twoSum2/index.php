<?php

declare(strict_types=1);

class Solution
{

  function twoSum(array $numbers, int $target): array
  {
    $map = array();
    for ($i = 0; $i < count($numbers); $i++) {

      $val = $numbers[$i];
      $pair = $target - $val;

      echo ("$val | $pair");
      echo ('<br>');


      if (isset($map[$pair])) {
        echo ("Found pair [$map[$pair], $i]");
        echo ('<br>');
        echo ('<br>');

        return [$map[$pair], $i + 1];
      } else {
        echo ("Adding $pair");
        echo ('<br>');

        $map[$val] = $i + 1;
        echo (json_encode($map));

        echo ('<br>');
        echo ('<br>');
      }
    }
  }
}


$solution = new Solution();
$solution->twoSum([2, 7, 11, 15], 9);
