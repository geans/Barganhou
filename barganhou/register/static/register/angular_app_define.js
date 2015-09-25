// Definindo um novo módulo para nossa aplicação
var indexApp = angular.module('register', []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

indexApp.controller('IndexController', ['$scope', function($scope) {
    $scope.local = {
        selected: null,
        tmp: null
    };
    $scope.getLocals = function() {
        locals = [];
        for(l in local.tmp) {
            locals.push({id: l.pk, name: l.name});
        };
        return locals;
    };
}]);




