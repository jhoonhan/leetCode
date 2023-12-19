<?php

declare(strict_types=1);

class Solution
{
  private $arr = [];

  function checkPrev($ratings, $start)
  {
    if (isset($ratings[$start - 1]) && $this->arr[$start] === $this->arr[$start - 1]) {
      if ($ratings[$start - 1] > $ratings[$start]) {
        $this->arr[$start - 1] += 1;
      }
      $this->checkPrev($ratings, $start - 1);
    }
  }

  function candy(array $ratings): int
  {
    $i = 0;
    $this->arr = array_fill(0, count($ratings), 1);

    while ($i < count($ratings)) {
      $changed = false;
      if (isset($ratings[$i - 1]) && $ratings[$i - 1] < $ratings[$i]) {
        $this->arr[$i] = $this->arr[$i - 1] + 1;
        $changed = true;
      }

      if ($changed === false && isset($ratings[$i + 1]) && $ratings[$i] > $ratings[$i + 1]) {
        $this->arr[$i] += 1;
        $this->checkPrev($ratings, $i);
        $changed = true;
      }

      if ($changed === false) {
        $this->arr[$i] = 1;
        $changed = true;
      }

      $i++;
    }

    return array_sum($this->arr);
  }
}

$solution = new Solution();
$solution->candy([29, 51, 87, 87, 72, 12]);
