<?php
/**
 * Created by IntelliJ IDEA.
 * User: chadl
 * Date: 9/17/2016
 * Time: 10:34 AM
 */

namespace App\Robot;


class Robot
{
    private $fr;
    private $br;

    private $fl;
    private $bl;

    public function __construct()
    {
        $this->fr = new Motor(1);
        $this->br = new Motor(2);
        $this->fl = new Motor(3);
        $this->bl = new Motor(4);
    }

    public function test()
    {
        $this->fr->forward();
        $this->br->forward();
        $this->fl->forward();
        $this->bl->forward();
    }
}