<?php

declare(strict_types=1);
class RandomizedSet
{

  private $set = [];

  function __construct()
  {
  }

  function insert(int $val): bool
  {
    echo ("#### Inserting $val");
    echo ('<br>');

    if (in_array($val, $this->set)) {
      echo ("Exists. Returning false");
      echo ('<br>');
      print_r($this->set);
      echo ('<br>');
      echo ('<br>');

      return false;
    } else {
      array_push($this->set, $val);
      echo ("Doesn't exist. Pushed $val");
      echo ('<br>');
      print_r($this->set);
      echo ('<br>');
      echo ('<br>');
      return true;
    }
  }


  function remove(int $val): bool
  {
    echo ("#### Removing $val");
    echo ('<br>');
    if (in_array($val, $this->set)) {
      echo ("Exists. Removing $val");
      echo ('<br>');
      print_r($this->set);
      echo ('<br>');
      echo ('<br>');
      return true;
    } else {
      echo ("Does not exsits. Returning False");
      echo ('<br>');
      print_r($this->set);
      echo ('<br>');
      echo ('<br>');
      return false;
    }
  }


  function getRandom(): bool
  {
    return true;
  }
}



$obj = new RandomizedSet();
$obj->insert(1);
$obj->insert(1);
$obj->remove(2);
$obj->remove(1);
