<?php

declare(strict_types=1);


class Node
{
	public Node|null $prev;
	public Node|null $next;

	function __construct(public int $key, public int $val)
	{
		$this->prev = null;
		$this->next = null;
	}
}

class LRUCache
{
	private int $capacity;
	private array $cache;

	private Node $left;
	private Node $right;

	/**
	 * @param   Integer  $capacity
	 */
	function __construct(int $capacity)
	{
		$this->capacity = $capacity;
		$this->cache    = [];

//		Left = LRU, right = MRU
		$this->left        = new Node(0, 0);
		$this->right       = new Node(0, 0);
		$this->left->next  = $this->right;
		$this->right->prev = $this->left;
	}

	function remove(Node $node): void
	{
		$prev = $node->prev;
		$next = $node->next;

		$prev->next = $next;
		$next->prev = $prev;
	}

	function insert(Node $node): void
	{
		$prev       = $this->right->prev;
		$next       = $this->right;
		$prev->next = $node;
		$next->prev = $node;
		$node->next = $this->right;
		$node->prev = $prev;
	}

	/**
	 * @param   Integer  $key
	 *
	 * @return Integer
	 */
	function get($key)
	{
		if (in_array($key, $this->cache)) {
			$this->remove($this->cache[$key]);
			$this->insert($this->cache[$key]);

			return $this->cache[$key]->val;
		}

		return -1;
	}

	/**
	 * @param   Integer  $key
	 * @param   Integer  $value
	 *
	 * @return NULL
	 */
	function put($key, $value)
	{
		if (in_array($key, $this->cache)) {
			$this->remove($this->cache[$key]);
		}

		$this->cache[$key] = new Node($key, $value);
		$this->insert($this->cache[$key]);

		if (count($this->cache) > $this->capacity) {
//			remove and delete the LRU;
			$lru = $this->left->next;
			$this->remove($lru);
			unset($this->cache[$lru->val]);
		}
	}
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * $obj = LRUCache($capacity);
 * $ret_1 = $obj->get($key);
 * $obj->put($key, $value);
 */