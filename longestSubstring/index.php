<?php declare(strict_types=1);

class Solution
{

    /**
     * @param String $s
     * @return Integer
     */
    function lengthOfLongestSubstring($s)
    {
        $str = "";
        $longestCount = 0;

        for ($i = 0; $i < strlen($s); $i++) {
            if (!str_contains($str, $s[$i])) {
                $str .= $s[$i];
//                echo("$str <br>");
            } else {
                if (strlen($str) > $longestCount) {
                    $longestCount = strlen($str);
                }
                $charIndex = strpos($str, $s[$i]) + 1;
                $str = substr($str, $charIndex) . $s[$i];
            }
        }
        $result = max($longestCount, strlen($str));
        echo $result;
        return $result;
    }
}

$solution = new Solution();
$solution->lengthOfLongestSubstring('aabaab!bb');

$test = "0013456789";
//echo strlen($test);
//echo strpos($test, "1");
//echo "<br>";
//echo substr($test, 1);