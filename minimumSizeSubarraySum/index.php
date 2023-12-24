<?php

declare(strict_types=1);

class Solution
{
  function minSubArrayLen(int $target, array $nums): int
  {

    // Guard clause
    if (array_sum($nums) < $target) {
      return 0;
    }
    rsort($nums);
    echo ("SORTED");
    echo ('<br>');
    echo (json_encode($nums));
    echo ('<br>');
    echo ('<br>');



    $l = 0;
    $r = 0;
    $acc = [$nums[$l]];
    $res = 0;


    // Iteration
    // while ($l < count($nums) - 1 && $r < count($nums) - 1) {
    while ($r < count($nums) - 1) {

      // Check self
      // Self is ALWAYS Smaller than target
      if ($nums[$l] > $target) {
        $l++;
        $r = $l;
        $acc = [$nums[$l]];
        continue;
      }

      echo ('<br>');
      echo ('<br>');
      echo ("CHECKING: ");
      echo (json_encode($acc));
      echo (" | $r");

      echo ('<br>');
      echo ("----------------------------------");
      echo ('<br>');


      // Smaller
      if (array_sum($acc) < $target) {
        echo ("ACC is smaller: ");
        echo (json_encode($acc));
        echo ('<br>');
        $sum = array_sum($acc);
        echo ("Sum: $sum");
        echo ('<br>');

        $r++;
        $acc[] = $nums[$r];
        echo ("El added: $nums[$r]");
        echo ('<br>');
        echo (json_encode($acc));
        echo ('<br>');
        $sum = array_sum($acc);
        echo ("Sum: $sum");
        echo ('<br>');
      }
      // Larger
      else {
        // echo ("ACC is larger: ");
        // echo (json_encode($acc));
        // echo ('<br>');
        // $sum = array_sum($acc);
        // echo ("Sum: $sum");
        // echo ('<br>');

        // $r++;
        // $acc[array_key_last($acc)] = $nums[$r];
        // echo ("Last El changed.");
        // echo ('<br>');

        // echo (json_encode($acc));
        return count($acc);
      }
      // Equal
      if (array_sum($acc) >= $target) {
        echo ('<br>');
        echo ("YES");
        echo ('<br>');
        echo (array_sum($acc));
        echo (" | $target");
        echo ('<br>');
        echo ("RESULT: ");
        echo (count($acc));
        return count($acc);
        // $r++;
      }
    }

    echo ('<br>');
    echo ('<br>');
    echo ($res);
    echo ('<br>');

    echo ("FAILED");

    return 0;
  }
}

$solution = new Solution();
// $solution->minSubArrayLen(7, [2, 16, 14, 15]);
$solution->minSubArrayLen(213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]);
