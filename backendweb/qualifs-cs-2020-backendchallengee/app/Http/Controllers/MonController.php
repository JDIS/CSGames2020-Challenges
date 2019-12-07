<?php

namespace App\Http\Controllers;

use App\Brique;
use Illuminate\Http\Request;
use Illuminate\Support\Collection;
use Illuminate\Support\Facades\Response;

class MonController extends Controller
{
    /**
     * Lvl0: Route that returns a static string
     * @param $mot1
     * @param $mot2
     * @return string
     */
    function helloWorld() {
        return "Salut la gang";
    }

    /**
     * Lvl1: Route that returns a generated string
     * @param $mot1
     * @param $mot2
     * @return string
     */
    function salutLes($mot1, $mot2) {
        return "Salut " . $mot1 . " " . $mot2;
    }

    /**
     * Lvl2: Route that returns JSON with get parameters
     * @return string
     */
    function json(Request $request) {
        $response = ['Woop' => 'woop'];
        $suite = new Collection();
        for ($i = intval($request['debut']); $i < $request['fin']; $i++) {
            $suite->push($i);
        }
        $response['suite'] = $suite;
        return Response::json($response);
    }

    /**
     * Lvl3: Route that saves a brick to database
     * @return string
     */
    function brique(Request $request) {
        $brique = new Brique(['name' => $request['name'], 'hauteur' => $request['hauteur'], 'largeur' => $request['largeur']]);
        $brique->save();
        return Response::json([], 201);
    }

    /**
     * Lvl3: Route that saves a brick to database
     * @return string
     */
    function getBriques(Request $request) {
        return Brique::all();
    }
}
