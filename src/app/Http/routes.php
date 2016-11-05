<?php

// The only view route
$app->get('/', function () use ($app) {
    return response(view('index'));
});

//The command route
$app->post('/', 'RoboController@commander');
