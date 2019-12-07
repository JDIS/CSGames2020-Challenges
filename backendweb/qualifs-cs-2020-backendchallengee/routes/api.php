<?php

use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::get('salut', 'MonController@helloWorld');
Route::get('salut/{word1}/{word2}', 'MonController@salutLes');
Route::get('json', 'MonController@json');
Route::post('brique', 'MonController@brique');
Route::get('brique', 'MonController@getBriques');
