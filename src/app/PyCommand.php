<?php

namespace App;


use App\Robot\Process;

class PyCommand
{
    public static $prefix = 'sudo python /var/www/robo/scripts/DCmotor/';

    private static $speed = 255;

    private static $moment = 100;

    private static $direction = 1;

    /**
     * @param array $options
     * @return string
     */
    public static function run($command, $options = [])
    {
        //speed moment direction(+/-)

        self::setOptions($options);

        $command = escapeshellcmd(self::$prefix.$command.'.py '.self::$speed." ".self::$moment." ".self::$direction);

        return [
            'results' => shell_exec($command.' 2>&1 1> /dev/null'),
            'command' => $command,
        ];
    }

    public static function setOptions($options = [])
    {
        self::$speed = empty($options['speed']) ? self::$speed : $options['speed'];
        self::$moment = empty($options['moment']) ? self::$moment : $options['moment'];
        self::$direction = empty($options['direction']) ? self::$direction : $options['direction'];
    }
}