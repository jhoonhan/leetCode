<?php

declare(strict_types=1);

class Solution
{

    /**
     * @param Integer[] $nums
     * @param Integer $val
     * @return Integer
     */
    function removeElement(&$nums, $val)
    {
        $k = 0;
        for ($i = 0; $i < count($nums); $i++) {
            if ($nums[$i] !== $val) {
                $nums[$k] = $nums[$i];
                $k++;
            }
        }

        return $k;
    }
}

$solution = new Solution();
$input = [3, 2, 2, 3, 3];
$solution->removeElement($input, 3);
