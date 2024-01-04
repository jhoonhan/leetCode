<?php

declare(strict_types=1);

// for ($i = 0; $i <= $maxH; $i++) {
//   # code...
//   echo ($matrix[$minV][$i]);
//   echo ('<br>');
//   $res[] = $matrix[$minV][$i];
// }
// $minV++;

class Solution
{

  public function move($matrix, &$res, $from, $to, &$position, $isHoriz, $isAdd, $isIncrease)
  {
    $indexFrom = $from;
    $indexTo = $to;
    if ($isAdd) {
      $indexTo++;
    } else {
      $indexTo--;
    }
    while ($indexFrom !== $indexTo) {
      if ($isHoriz) {
        echo ($matrix[$position][$indexFrom]);
        $res[] = $matrix[$position][$indexFrom];
      } else {
        echo ($matrix[$indexFrom][$position]);
        $res[] = $matrix[$indexFrom][$position];
      }
      if ($isAdd) {
        $indexFrom++;
      } else {
        $indexFrom--;
      }
      echo ('  ');
      echo ('<br>');
    }
    if ($isIncrease) {
      $position++;
    } else {
      $position--;
    }
    echo (json_encode($res));
    echo ('<br>');
  }

  function spiralOrder(array $matrix): array
  {
    $totalCount = count($matrix[0]) * count($matrix);

    $minV = 0;
    $maxV = count($matrix) - 1;
    $minH = 0;
    $maxH = count($matrix[0]) - 1;
    $res = (array)[];



    $counter = 0;
    while (count($res) !== $totalCount) {
      echo ("minV: $minV | maxV: $maxV | minH: $minH | maxH: $maxH");
      echo ('<br>');

      if ($counter === 0) {
        // 0 :: Horizontal Move
        $this->move($matrix, $res, $minH, $maxH, $minV, true, true, true);
        $counter++;
      } elseif ($counter === 1) {
        // 1 :: Vertical Move
        echo ('<br>');
        $this->move($matrix, $res, $minV, $maxV, $maxH, false, true, false);
        $counter++;
      } elseif ($counter === 2) {
        // 2 :: Horizontal
        echo ('<br>');
        $this->move($matrix, $res, $maxH, $minH, $maxV, true, false, false);
        $counter++;
      } else {
        // 3 :: Vertical
        echo ('<br>');
        $this->move($matrix, $res, $maxV, $minV, $minH, false, false, true);
        $counter = 0;
      }
      echo ('<br>');
    }

    return $res;
  }
}

$solution = new Solution();
// $solution->spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]);
$solution->spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
