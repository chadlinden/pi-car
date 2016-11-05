<?php

namespace App\Robot;

use App\Robot\Pin;
use App\Robot\Contracts\MotorInterface;
class Motor implements MotorInterface
{
    private $pins = [];

    const PIN_CONFIG = [
        1 => [
            'pwm' => 8,
            'in2' => 9,
            'in1' => 10,
        ],
        2 => [
            'pwm' => 13,
            'in2' => 12,
            'in1' => 11,
        ],
        3 => [
            'pwm' => 2,
            'in2' => 3,
            'in1' => 4,
        ],
        4 => [
            'pwm' => 7,
            'in2' => 6,
            'in1' => 5,
        ],
    ];

    public function __construct($motor = 0)
    {
        if( $motor == 0 || $motor > 4)
        {
            return false;
        }

        $this->setPins(self::PIN_CONFIG[$motor]);
    }


    private function setPins($pinConfig)
    {
        foreach($pinConfig as $key => $pinNumber)
        {
            $this->pins[$key] = Pin::getPin($pinNumber);
        }
    }

    public function forward($speed = 0, $accel = 0)
    {
        $this->pins['in2']->pinOut()->goHigh();
        $this->pins['in1']->pinOut()->goLow();
        sleep(1);
        $this->pins['in2']->pinOut()->goLow();
        $this->pins['in1']->pinOut()->goLow();
    }

    public function reverse($speed = 0, $accel = 0)
    {
        // TODO: Implement reverse() method.
    }

    /**
     * @param int $speed
     * @return mixed
     */
    public function speed($speed = 1)
    {
        // TODO: Implement speed() method.
    }

    /**
     * Increase the motor's velocity
     * units per second
     * @param int $velocity
     * @return mixed
     */
    public function accelerate($velocity = 0)
    {
        // TODO: Implement accelerate() method.
    }
}