<?php

declare(strict_types=1);

class Solution
{
  function minWindow(string $s, string $t): string
  {
    if ($t === "" || strlen($t) > strlen($s)) {
      return "";
    }

    $tChars = str_split($t);
    $sChars = str_split($s);

    // Create hashmap
    $countT = array_fill_keys($tChars, 0);
    foreach ($tChars as $value) {
      $countT[$value]++;
    }

    $have = 0;
    $need = count($countT);
    $res = [-1, -1];
    $resLen = strlen($s) + 1;
    $l = 0;

    for ($r = 0; $r < strlen($s); $r++) {
      $curr = $s[$r];
      if (array_key_exists($curr, $countT)) {
        $window[$curr] = 1 + ($window[$curr] ?? 0);
      }

      if (array_key_exists($curr, $countT) && $window[$curr] === $countT[$curr]) {
        $have++;
      }


      while ($have === $need) {
        if (($r - $l + 1) < $resLen) {
          $res = [$l, $r];
          $resLen = ($r - $l + 1);
        }
        if (array_key_exists($s[$l], $countT)) {
          $window[$s[$l]]--;
        }
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

    if ($res[0] >= 0 && $res[1] >= 0) {
      return implode('', array_slice($sChars, $res[0], $resLen));
    } else {
      return "";
    }
  }
}

$solution = new Solution();
// $solution->minWindow("abc", "b");
$solution->minWindow("a", "b");
