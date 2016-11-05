<?php

namespace App\Robot;


class Pin
{
    public $pinNumber;
    public $pinMode;

    public static $path = '/usr/local/bin/gpio -g';

    public static function getPin($pinNumber, $pinMode = 'out')
    {
        $model = new self();
        $model->setConfig($pinNumber, $pinMode);

        return $model;
    }

    public function setConfig($pinNumber = 0, $pinMode = 'out')
    {
        $this->pinNumber = $pinNumber;
        $this->pinMode = $pinMode;
        return $this;
    }

    public function pinOut()
    {
        shell_exec(self::$path.' mode '.$this->pinNumber.' '.$this->pinMode);
        return $this;
    }

    public function goHigh()
    {
        shell_exec(self::$path.' write '.$this->pinNumber.' 1');
        return $this;
    }

    public function goLow()
    {
        shell_exec(self::$path.' write '.$this->pinNumber.' 0');
        return $this;
    }
}