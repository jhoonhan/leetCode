<?php

declare(strict_types=1);

class Solution
{
  function minWindow(string $s, string $t): string
  {
    if ($t === "") {
      return "";
    }

    $tChars = str_split($t);
    $sChars = str_split($s);

    // Create hashmap
    $window = array_fill_keys($tChars, 0);
    $countT = array_fill_keys($tChars, 0);
    foreach ($tChars as $value) {
      $countT[$value]++;
    }

    $have = 0;
    $need = count($countT);
    $res = [-1, -1];
    $resLen = INF;
    $l = 0;

    for ($r = 0; $r < strlen($s) - 1; $r++) {
      $c = $s[$r];
      $window[$c] = 1 + ($window[$c] ?? 0);

      if (array_key_exists($c, $countT) && $window[$c] === $countT[$c]) {
        $have++;
      }

      while ($have === $need) {
        if (($r - $l + 1) < $resLen) {
          $res = [$l, $r];
          $resLen = ($r - $l + 1);
        }
        $window[$s[$l]]--;

        if (array_key_exists($s[$l], $countT) && $window[$s[$l]] < $countT[$s[$l]]) {
          $have--;
        }
        $l++;
      }
    };



    // while ($l < $r && $r < strlen($s) + 1) {
    //   $subStr = array_slice($sChars, $l, $r - $l);
    //   $window = array_fill_keys($tChars, 0);
    //   $has = 0;
    //   foreach ($subStr as $value) {
    //     if (in_array($value, $tChars)) {
    //       $window[$value]++;
    //       if ($window[$value] <= $map[$value]) {
    //         $has++;
    //       }
    //     }
    //   }
    //   echo ("$l and $r");
    //   echo ('<br>');

    //   echo (":: ");
    //   echo (implode('', $subStr));
    //   echo (" | ");

    //   echo ($has);
    //   echo ('<br>');


    //   // If contains
    //   if ($has === strlen($t)) {
    //     echo ('good');
    //     echo ('<br>');
    //     $l++;
    //     if (count($subStr) < count($res) || count($res) === 0) {
    //       $res = $subStr;
    //     }
    //   }
    //   // If not
    //   else {
    //     echo ('bad');
    //     echo ('<br>');
    //     $r++;
    //   }
    // }





    echo (implode('', array_slice($sChars, $l, $r - $l)));

    return implode('', array_slice($sChars, $l, $r - $l));
  }
}

$solution = new Solution();
// $solution->minWindow("abc", "b");
$solution->minWindow("AODBECODEBANC", "ABC");
