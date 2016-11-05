<?php

namespace App\Http\Controllers;

use App\PyCommand;
use App\Robot\Robot;
use Illuminate\Http\Request;
use Laravel\Lumen\Routing\Controller as BaseController;

class RoboController extends BaseController
{
    public static $commands = [
        'FORWARD' => 'forward',
        'REVERSE' => 'reverse',
        'RIGHT'   => 'right',
        'LEFT'    => 'left',
    ];

    public function commander(Request $request)
    {
        $robot = new Robot();
        $robot->test();
//        if( $request->has('command') && array_key_exists($request->input('command'), SELF::$commands) ){
//            $cmd = self::$commands[$request->input('command')];
//            return PyCommand::run( $cmd );
//        }
//        return ['error' => 'command not found'];
    }
}
