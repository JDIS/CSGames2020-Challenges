<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Brique extends Model
{

    protected $table = 'brique';
    protected $fillable = [
        'name', 'largeur', 'hauteur',
    ];
}
