<?php
namespace Robot;


class Robot
{
    const PATH = 'sudo python /var/www/scripts/';

    const COMMANDS = [
        'FORWARD' => 'forward',
        'REVERSE' => 'reverse',
        'RIGHT'   => 'right',
        'LEFT'    => 'left',
    ];

    public static function handle($input = [])
    {
        if( empty($input['command']) || ! array_key_exists($input['command'], self::COMMANDS) ){
            return ['results' => 'Error: command not recognized'];
        }

        $command = escapeshellcmd(
            self::PATH .
            'motion.py --command ' . $input['command'] . ' ' .
            '--speed ' . $input['speed'] . ' ' .
            '--moment ' . $input['moment'] . ' ' .
            '--heading ' .$input['heading']
        );

        return [
            'results' => exec($command.' 2>&1 1> /dev/null'),
            'command' => $command,
        ];
    }

}