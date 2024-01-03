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
          // echo ($value);
          // echo ('<br>');
          if ($value > 9 || $value < 1) {
            echo ("Failed on Row");
            echo ('<br>');
            return false;
          }

          $map[$value] = 1 + ($map[$value] ?? 0);
          if ($map[$value] > 1) {
            echo ("Failed on Row");
            echo ('<br>');
            return false;
          }
        }
      }
    }
    // check by column
    for ($i = 0; $i < count($board[0]); $i++) {
      $map = array();
      for ($j = 0; $j < count($board[0]); $j++) {
        if (is_numeric($board[$j][$i])) {
          // $curr = $board[$j][$i];
          // echo ("$i :: $j :: $curr");
          // echo ('<br>');

          $map[$board[$j][$i]] = 1 + ($map[$board[$j][$i]] ?? 0);

          if ($map[$board[$j][$i]] > 1) {
            echo ("Failed on Column");
            echo ('<br>');
            return false;
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
        // echo ("ROW# : $rowNumber");
        // echo ("BOX# : $boxNumber");
        // echo ('<br>');
        $map[$boxNumber] = array_merge($map[$boxNumber], $chunks[$j]);
      }
    }

    foreach ($map as $board) {
      $hash = array();
      foreach ($board as $value) {
        if (is_numeric($value)) {
          $hash[$value] = 1 + ($hash[$value] ?? 0);
          if ($hash[$value] > 1) {
            echo ("Failed on 3X3");
            echo ('<br>');
            return false;
          }
        }
      }

      echo (json_encode($board));
      echo ('<br>');
    }







    var_dump($res);
    return $res;
  }
}

$solution = new Solution();
$solution->isValidSudoku([
  ["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]);
