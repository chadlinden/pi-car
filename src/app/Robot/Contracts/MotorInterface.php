<?php

namespace App\Robot\Contracts;


interface MotorInterface
{
    /**
     * Default direction
     * @return mixed
     */
    public function forward();

    /**
     * Reverse of default direction
     * @return mixed
     */
    public function reverse();

    /**
     * @param int $speed
     * @return mixed
     */
    public function speed($speed = 1);

    /**
     * Increase the motor's velocity
     * units per second
     * @param int $velocity
     * @return mixed
     */
    public function accelerate($velocity = 0);
}