<?php

declare(strict_types=1);

class Solution
{
  function isValidSudoku(array $board): bool
  {
    $res = true;
    // check by row
    foreach ($board as $row) {
      $map = array();
      foreach ($row as $value) {
        if (is_numeric($value)) {
          if ($value > 9 || $value < 1) {
            return false;
          }
          if (in_array($value, $map)) {
            echo ("FAILED ON ROW");
            return false;
          } else {
            $map[] = $value;
          }
        }
      }
    }
    // check by column
    for ($i = 0; $i < count($board[0]); $i++) {
      $map = array();
      for ($j = 0; $j < count($board[0]); $j++) {
        if (is_numeric($board[$j][$i])) {
          if (in_array($board[$j][$i], $map)) {
            echo ("FAILED on COL");
            return false;
          } else {
            $map[] = $board[$j][$i];
          }
        }
      }
    }
    // check by 3x3
    $map = array_fill(0, 9, []);
    $rowNumber = 0;
    for ($i = 0; $i < count($board); $i++) {
      $chunks = array_chunk($board[$i], 3);
      for ($j = 0; $j < count($chunks); $j++) {
        $rowNumber = (int)($i / 3);
        $boxNumber = $rowNumber * 3 + $j;
        $map[$boxNumber] = array_merge($map[$boxNumber], $chunks[$j]);
      }
    }
    foreach ($map as $board) {
      $hash = array();
      foreach ($board as $value) {
        if (is_numeric($value)) {
          if (in_array($value, $hash)) {
            echo ("FAILED ON 3X#");
            return false;
          } else {
            $hash[] = $value;
          }
        }
      }
    }

    var_dump($res);
    return $res;
  }
}

$solution = new Solution();
$solution->isValidSudoku([
  ["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]);
