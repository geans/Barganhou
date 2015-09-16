// Definindo um novo módulo para nossa aplicação
var app = angular.module ("shopping_cart", []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});

function ShoppingCartController($scope) {

	$scope.cart = [];

	$scope.addItemCart = function(product) {
		$scope.cart.push(product);
	};

	$scope.removeItemCart = function(index) {
		$scope.cart.splice(index, 1);
	};
}
