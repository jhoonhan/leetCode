<?php

declare(strict_types=1);


class Solution
{
  function spiralOrder(array $matrix): array
  {
    $totalCount = count($matrix[0]) * count($matrix);

    echo ($totalCount);

    $minV = 0;
    $maxV = count($matrix[0]);
    $minH = 0;
    $maxH = $maxV;
    $res = (array)[];

    // while(count($res) !== count())

    return $res;
  }
}

$solution = new Solution();
$solution->spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]);
