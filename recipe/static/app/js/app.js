var mainCtrl = function($scope, $filter, recipesService) {
    var slugify = $filter("slugify");

    $scope.recipes = recipesService.recipes();

    $scope.recipeHref = function(name) {
        return "/recipe/" + slugify(name) + "/";
    };

    $scope.onLinkClick = function(name) {
        location.href = $scope.recipeHref(name);
    };
};

mainCtrl.$inject = ["$scope", "$filter", "recipesService"];

var recipesService = function($resource) {
    var recipesResource = $resource("/recipe/api/v1/recipes");

    return {
        recipes: function() {
            return recipesResource.query();
        }
    };
};

recipesService.$inject = ["$resource"];

var slugify = function() {
    return function(value) {
        if (angular.isString(value)) {
            return value.toLowerCase().replace(/\s+/g, "-").replace(/[^-a-z0-9]/gi, "-").replace(/\-+/g, "-");
        }
        else {
            return value;
        }
    };
};

var title = function() {
    return function(value) {
        if (angular.isString(value)) {
            return value.toLowerCase().replace(/\w+/g, "");
        }
        else {
            return value;
        }
    };
};

angular.module("mainApp", ["ngResource"])
    .controller("mainCtrl", mainCtrl)
    .factory("recipesService", recipesService)
    .filter("slugify", slugify)
    .filter("title", title);