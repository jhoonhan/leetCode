<?php

declare(strict_types=1);

class Solution
{
  function findSubstring(string $s, array $words): array
  {
    // $wordLegnth = strlen($words[0]);
    // $success = [];
    // for ($i = 0; $i <= strlen($s) - ($wordLegnth * count($words)); $i++) {
    //   $substr = substr($s, $i, $wordLegnth);
    //   $brute = $words;
    //   if (in_array($substr, $brute)) {
    //     for ($j = $i; $j <= ($wordLegnth * count($words)) + $i; $j += $wordLegnth) {
    //       $nextWord = substr($s, $j, $wordLegnth);
    //       $key = array_search($nextWord, $brute);
    //       if (in_array($nextWord, $brute)) {
    //         unset($brute[$key]);
    //         if (count($brute) === 0) {
    //           $success[] = $i;
    //           break;
    //         }
    //       } else {
    //         break;
    //       }
    //     }
    //   }
    // }
    // echo (json_encode($success));
    // return $success;

    $result = [];
    if (count($words) < 1) return $result;
    $strLength  = strlen($s);
    $wordLength = strlen($words[0]);
    $subLength  = $wordLength * count($words);

    sort($words);

    for ($i = 0; $i <= ($strLength - $subLength); $i++) {
      $strToArr = str_split(substr($s, $i, $subLength), $wordLength);
      sort($strToArr);
      echo (json_encode($strToArr));
      echo ('<br>');

      if (
        count($words) === count($strToArr)
        && empty(array_diff_assoc($strToArr, $words))
      ) {
        $result[] = $i;
      }
    }
    return $result;
  }
}

$solution = new Solution();
// $solution->findSubstring("barfoothefoobarman", ["foo", "bar"]);
$solution->findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]);
