<?php
namespace Robot;


class Robot
{
    const PATH = 'sudo python /var/www/scripts/DCmotor/';

    const COMMANDS = [
        'FORWARD' => 'forward',
        'REVERSE' => 'reverse',
        'RIGHT'   => 'right',
        'LEFT'    => 'left',
    ];

    public static function handle($input = [])
    {
        return $input;

//        $command = escapeshellcmd(self::PATH . self::COMMANDS[$input['command']].'.py 100 100 1');
//
//        return [
//            'results' => shell_exec($command.' 2>&1 1> /dev/null'),
//            'command' => $command,
//        ];
    }

}