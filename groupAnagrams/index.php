<?php declare(strict_types=1);

class Solution {

    public $hashmap = [];


    function groupAnagrams($strs) {
    
    
    }
    // function checkAnagram($str, $target): bool {
    //     if(strlen($str) !== strlen($target)) return false;
    //     $res = true;
    //     for ($i=0; $i < strlen($str); $i++) { 
    //         if(strpos($target, $str[$i]) === false) {
    //             $res = false;
    //         }
    //     }
    //     return $res;
    // }

    // /**
    //  * @param String[] $strs
    //  * @return String[][]
    //  */
    // function groupAnagrams($strs) {
    //     $res = [];
    //     foreach ($strs as $str) {
    //         $splitted = str_split($str);
    //         sort($splitted);
    //         $newStr = implode($splitted);
            
    //         if(!isset($this->hashmap[$newStr])) {
    //             $this->hashmap[$newStr] = count($res);
    //         }
    //         $res[$this->hashmap[$newStr]][] = $str;
            
    //     }
    //     return $res;
    // }
}


$solution = new Solution(); 
$solution->groupAnagrams(["eat","tea","tan","ate","nat","bat"]);
