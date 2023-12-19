<?php

declare(strict_types=1);

class Solution
{
  private $arr = [];

  function checkPrev($ratings, $start)
  {
    echo ("aaang");

    if (isset($ratings[$start - 1]) && $ratings[$start] > $ratings[$start - 1]) {
      $this->arr[$start - 1] += 1;
      echo ("Prev: ");
      echo ($this->arr[$start - 1]);
      $this->checkPrev($ratings, $start - 1);
    }
  }

  function candy(array $ratings): int
  {
    $i = 0;
    $this->arr = array_fill(0, count($ratings), 1);
    // print_r($this->arr);



    while ($i < count($ratings)) {
      // Check left
      if (isset($ratings[$i - 1]) && $ratings[$i - 1] < $ratings[$i]) {
        $this->arr[$i] = $this->arr[$i - 1] + 1;

        echo ("Left: ");
        echo ($this->arr[$i]);
        echo ('<br>');
      } elseif (isset($ratings[$i + 1]) && $ratings[$i] > $ratings[$i + 1]) {
        // Check right
        $this->arr[$i] += 1;
        echo ("Right: ");
        echo ($this->arr[$i]);
        echo ('<br>');
        // Check prev
        $this->checkPrev($ratings, $i);
      } else {
        echo ("None: ");
        echo ($this->arr[$i]);
        echo ('<br>');
        $this->arr[$i] = 1;
      }
      $i++;
    }

    // print_r($this->arr);
    foreach ($this->arr as $key => $value) {
      echo ($value);
      echo (" ");
    }

    return 0;
  }
}

$solution = new Solution();
$solution->candy([0, 1, 2, 1, 7, 3, 0, 1, 2]);
