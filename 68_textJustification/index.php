<?php

declare(strict_types=1);

use function PHPSTORM_META\type;

class Solution
{

  private function aaang(array $wordRow, int $maxWidth, bool $istLast): string
  {
    $diff = $maxWidth - strlen(join("", $wordRow));
    $gaps = count($wordRow) - 1;
    $dist = 0;
    $remainder = 0;
    if ($gaps > 0) {
      $dist = (int)floor($diff / $gaps);
      $remainder = $diff % $gaps;
    }

    $str = "";
    if (!$istLast) {
      for ($i = 0; $i <= $gaps; $i++) {
        if ($i < $gaps) {
          $str .= $wordRow[$i] . str_repeat(' ', $dist);
          if ($remainder > 0) {
            $str .= ' ';
            $remainder--;
          }
        } elseif ($maxWidth - strlen($str) > 0) {
          $str .= $wordRow[$i];
          $str .= str_repeat(' ', $maxWidth - strlen($str));
        }
      }
    } else {
      $str = join(' ', $wordRow);
      $str .= str_repeat(' ', $maxWidth - strlen($str));
    }


    return $str;
  }

  function fullJustify(array $words, int $maxWidth): array
  {
    $acc = -1;
    $res = [];
    $row = 0;

    for ($i = 0; $i < count($words); $i++) {
      $count = $acc + strlen($words[$i]) + 1;
      if ($count <= $maxWidth) {
        // Update the accumulator so that it can be compared with maxwidth during next iteration
        $acc = $count;
        // Add words to result
        $res[$row][] = $words[$i];
      } else {
        // If failed, move doen a row
        $row++;
        // Start fresh:
        // Accumulator is not the length of itself
        $acc = strlen($words[$i]);
        // Add self to res
        $res[$row][] = $words[$i];
      }
    }

    // Returns
    $resStr = [];
    foreach ($res as $key => $row) {
      if ($key < count($res) - 1) {
        $resStr[] = $this->aaang($row, $maxWidth, false);
      } else {
        $resStr[] = $this->aaang($row, $maxWidth, true);
      }
    }

    // foreach ($resStr as $key => $strRow) {
    //   echo ($strRow);
    //   echo ('<br>');
    // }


    return $resStr;
  }
}

$solution = new Solution();
$solution->fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16);
