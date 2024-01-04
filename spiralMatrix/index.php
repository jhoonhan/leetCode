<?php

declare(strict_types=1);


class Solution
{
  public function move($matrix, &$res, $from, $to, &$position, $isHoriz, $isAdd, $isIncrease)
  {
    if ($isAdd) {
      $to++;
    } else {
      $to--;
    }
    while ($from !== $to) {
      if ($isHoriz) {
        $res[] = $matrix[$position][$from];
      } else {
        $res[] = $matrix[$from][$position];
      }
      if ($isAdd) {
        $from++;
      } else {
        $from--;
      }
    }
    if ($isIncrease) {
      $position++;
    } else {
      $position--;
    }
  }

  function spiralOrder(array $matrix): array
  {
    $res = (array)[];

    $minV = 0;
    $maxV = count($matrix) - 1;
    $minH = 0;
    $maxH = count($matrix[0]) - 1;

    $counter = 0;
    while (count($res) !== count($matrix[0]) * count($matrix)) {
      if ($counter === 0) {
        $this->move($matrix, $res, $minH, $maxH, $minV, true, true, true);
        $counter++;
      } elseif ($counter === 1) {
        $this->move($matrix, $res, $minV, $maxV, $maxH, false, true, false);
        $counter++;
      } elseif ($counter === 2) {
        $this->move($matrix, $res, $maxH, $minH, $maxV, true, false, false);
        $counter++;
      } else {
        $this->move($matrix, $res, $maxV, $minV, $minH, false, false, true);
        $counter = 0;
      }
    }
    return $res;
  }
}

$solution = new Solution();
// $solution->spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]);
$solution->spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);
