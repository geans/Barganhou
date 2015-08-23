// Definindo um novo módulo para nossa aplicação
var app = angular.module ("register", []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});




