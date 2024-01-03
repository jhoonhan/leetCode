<?php

declare(strict_types=1);

class Solution
{
  function minWindow(string $s, string $t): string
  {
    if ($t === "") {
      return "";
    }

    $tLength = strlen($t);
    $l = 0;
    $r = $tLength;
    $sChars = str_split($s);
    $tChars = str_split($t);
    $res = [];

    // Create hashmap
    $map = array_fill_keys($tChars, 0);
    foreach ($tChars as $value) {
      $map[$value]++;
    }
    // ksort($map);


    while ($l < $r && $r < strlen($s) + 1) {
      $subStr = array_slice($sChars, $l, $r - $l);
      $window = array_fill_keys($tChars, 0);
      $has = 0;
      foreach ($subStr as $value) {
        if (in_array($value, $tChars)) {
          $window[$value]++;
          if ($window[$value] <= $map[$value]) {
            $has++;
          }
        }
      }
      echo ("$l and $r");
      echo ('<br>');

      echo (":: ");
      echo (implode('', $subStr));
      echo (" | ");

      echo ($has);
      echo ('<br>');


      // If contains
      if ($has === strlen($t)) {
        echo ('good');
        echo ('<br>');
        $l++;
        if (count($subStr) < count($res) || count($res) === 0) {
          $res = $subStr;
        }
      }
      // If not
      else {
        echo ('bad');
        echo ('<br>');
        $r++;
      }
    }

    echo ('<br>');
    echo ('<br>');
    $aang = implode('', $res);
    echo ("RESULT: $aang");



    return implode('', $res);
  }
}

$solution = new Solution();
// $solution->minWindow("abc", "b");
$solution->minWindow("AODBECODEBANC", "ABC");
