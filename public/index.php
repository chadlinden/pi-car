<?php
ini_set("display_errors", "1");
error_reporting(E_ALL);

$input = json_decode(file_get_contents("php://input"), true);

if( ! empty($input) ){
    require __DIR__.'/../vendor/autoload.php';
    require __DIR__.'/../robot/Robot.php';

    $robot = Robot\Robot::handle($input);

    print_r( json_encode($robot) );
    exit();
}

require '/var/www/public/static/index.html';