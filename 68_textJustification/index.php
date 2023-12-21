<?php

declare(strict_types=1);

use function PHPSTORM_META\type;

class Solution
{

  private function aaang(array $wordRow, int $maxWidth): string
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
    for ($i = 0; $i <= $gaps; $i++) {
      # code...
      if ($i < $gaps) {
        $str .= $wordRow[$i] . str_repeat('_', $dist);
        if ($remainder > 0) {
          $str .= "_";
          $remainder--;
        }
      } else {
        $str .= $wordRow[$i];
      }
    }
    for ($j = 0; $j < $remainder; $j++) {
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
      echo ("Count: $count");
      echo ('<br>');
      if ($count <= $maxWidth) {
        echo ("Success: $count");
        echo ('<br>');
        // Update the accumulator so that it can be compared with maxwidth during next iteration
        $acc = $count;
        // Add words to result
        $res[$row][] = $words[$i];
        print_r($res[$row]);
      } else {
        echo ("Failed: $count");
        echo ('<br>');
        // If failed, move doen a row
        $row++;
        // Start fresh:
        // Accumulator is not the length of itself
        $acc = strlen($words[$i]);
        // Add self to res
        $res[$row][] = $words[$i];
        print_r($res[$row]);
      }
      echo ('<br>');
      echo ('<br>');
    }


    $real = [];
    foreach ($res as $key => $row) {
      $real[] = $this->aaang($row, $maxWidth);
    }
    echo ('<br>');

    foreach ($real as $key => $strRow) {
      # code...
      echo ($strRow);
      echo ('<br>');
    }


    return [];
  }
}

$solution = new Solution();
$solution->fullJustify(["this", "is", "an", "example", "of", "text", "justification"], 16);
