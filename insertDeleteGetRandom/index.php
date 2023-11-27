<?php

declare(strict_types=1);
class RandomizedSet
{

  private $map = array();

  private $index = 0;

  function __construct()
  {
  }

  function insert(int $val): bool
  {
    // echo ("#### Inserting $val");
    // echo ('<br>');

    if (isset($this->map[$val])) {
      // echo ("Exists. Returning: FALSE");
      // echo ('<br>');
      // print_r($this->map);
      // echo ('<br>');
      // echo ('<br>');

      return false;
    } else {
      // echo ("Doesn't exist. Adding: $val");
      $this->map[$val] = $this->index;
      // echo ('<br>');
      // print_r($this->map);
      // echo ('<br>');
      // echo ('<br>');
      return true;
    }
  }


  function remove(int $val): bool
  {
    // echo ("#### Removing $val");
    // echo ('<br>');
    if (isset($this->map[$val])) {
      // echo ("Exists. Removing: $val");
      unset($this->map[$val]);
      // echo ('<br>');
      // print_r($this->map);
      // echo ('<br>');
      // echo ('<br>');
      return true;
    } else {
      // echo ("Does not exsits. Returning: FALSE");
      // echo ('<br>');
      // print_r($this->map);
      // echo ('<br>');
      // echo ('<br>');
      return false;
    }
  }


  function getRandom(): int
  {
    return array_rand($this->map);
  }
}



$obj = new RandomizedSet();
$obj->insert(1);
$obj->insert(1);
$obj->remove(2);
$obj->insert(2);
$obj->insert(3);
$obj->remove(3);
$obj->insert(4);
$obj->insert(100);


// $obj->remove(1);
$obj->getRandom();
