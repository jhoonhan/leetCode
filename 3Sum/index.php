<?php

declare(strict_types=1);



class Solution
{
  function threeSum(array $nums): array
  {
    sort($nums);
    $res = [];
    echo (json_encode($nums));
    echo ('<br>');
    echo ('<br>');

    for ($i = 0; $i < count($nums); $i++) {
      $l = $i + 1;
      $r = count($nums) - 1;
      echo ("CHECKING: $i :: $nums[$i]");
      echo ('<br>');


      if ($i > 0 && $nums[$i] === $nums[$i - 1]) {
        continue;
      }

      while ($l < $r) {
        $target = $nums[$i] + $nums[$l] + $nums[$r];
        echo ("T: $target");
        echo ('<br>');

        echo ("$nums[$i] | $nums[$l] | $nums[$r]");
        echo ('<br>');
        echo ('<br>');
        // Target is larger
        if ($target > 0) {
          $r--;
        }
        // Target is smaller
        elseif ($target < 0) {
          $l++;
        }
        // Target is equal
        else {
          echo ("Match made $nums[$i], $nums[$l], $nums[$r]");
          echo ('<br>');
          echo ('<br>');
          $res[] = [$nums[$i], $nums[$l], $nums[$r]];
          $l++;
          while ($nums[$l] === $nums[$l - 1] and $l < $r) {
            $l++;
          }
        }
      }
    }

    echo ('<br>');
    echo ('<br>');
    echo (json_encode($res));

    return $res;
  }
}

$solution = new Solution();
$solution->threeSum([-1, 0, 1, 2, -1, -4]);
