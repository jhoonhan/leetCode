<?php declare(strict_types=1);

class Solution
{

    /**
     * @param Integer[] $nums
     * @param Integer $val
     * @return Integer
     */
    function removeElement(&$nums, $val)
    {
//        var_dump($nums);
//        echo("<br>");
//        echo("$val<br>");

        $count = count($nums);

        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] == $val) {
                unset($nums[$i]);
                $nums[$i] = "_";
                $count -= 1;
            }
        }
        unset($nums['_']);

        return $count;
    }
}

$solution = new Solution();
$input = [3, 2, 2, 3];
$solution->removeElement($input, 3);