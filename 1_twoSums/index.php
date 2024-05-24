<?php declare(strict_types = 1);


class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
//    Time Complexity = O(n^2)
//    function twoSum(array $nums, int $target): array {
//        for ($i = 0; $i < count($nums); $i++) {
//            for ($j = $i + 1; $j < count($nums); $j++){
//                if($nums[$i] + $nums[$j] === $target) {
//                    echo($nums[$i] + $nums[$j]);
//                    return [$i,$j];
//                }
//            }
//        }
////        Will never reach here
//        return [];
//    }
    function twoSum(array $nums, int $target): array
    {
        $map = array();
        for($i = 0; $i<count($nums); $i++){
            $val = $nums[$i];
            $pair = $target - $val;
            if(isset($map[$pair])) {
                return [$map[$pair], $i];
            }
            $map[$val] = $i;

        }

//        will never reach here
        return [];
    }

}

$solution = new Solution();
$result1 = $solution->twoSum([2,7,11,15], 9);
$result2 = $solution->twoSum([3,2,4], 6);
$result3 = $solution->twoSum([3,3], 6);

echo("$result1[0] | $result1[1]<br>");
echo("$result2[0] | $result2[1]<br>");
echo("$result3[0] | $result3[1]");

?>