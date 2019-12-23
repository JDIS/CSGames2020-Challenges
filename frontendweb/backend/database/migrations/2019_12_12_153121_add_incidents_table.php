<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class AddIncidentsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('incidents', function (Blueprint $table) {
            $table->string('id')->primary();
            $table->string('type');
            $table->string('primaryCause');
            $table->string('secondaryCause');
            $table->string('symptom');
            $table->string('line');
            $table->integer('turnNumber');
            $table->time('incidentTime');
            $table->time('backToNormalTime');
            $table->integer('vehicle');
            $table->integer('doorNumber');
            $table->string('equipmentType');
            $table->string('locationCode');
            $table->boolean('damagedEquipment');
            $table->boolean('kfs');
            $table->boolean('door');
            $table->boolean('emergency');
            $table->boolean('cat');
            $table->string('evacuation');
            $table->year('year');
            $table->date('yearMonth');
            $table->unsignedInteger('monthNumber');
            $table->unsignedInteger('dayNumber');
            $table->unsignedInteger('weekDayNumber');
            $table->date('date');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('incidents');
    }
}
