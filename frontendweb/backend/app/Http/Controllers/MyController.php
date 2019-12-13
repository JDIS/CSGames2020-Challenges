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
        $query = Incident::class;
        if ($request['ligne']) {
            $incidents = Incident::where('line', 'Ligne ' . $request['ligne'])->paginate($n);
        } else {
            $incidents = Incident::paginate($n);
        }
        return \Response::json($incidents);
    }
}
