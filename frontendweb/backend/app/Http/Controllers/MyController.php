<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class MyController extends Controller
{
    public function getData(Request $request) {
        return ['data' => 5];
    }
}
