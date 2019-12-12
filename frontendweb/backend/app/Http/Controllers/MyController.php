<?php

namespace App\Http\Controllers;

use App\Incident;
use Illuminate\Http\Request;

class MyController extends Controller
{
    public function getData(Request $request) {
        $n = 15;
        if($request['n']) {
            $n = $request['n'];
        }
        $incidents = Incident::paginate($n);
        return \Response::json($incidents);
    }
}
