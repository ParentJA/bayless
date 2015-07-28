(function () {
  "use strict";

  function MainController($scope) {}

  angular.module("app")
    .controller("MainController", ["$scope", MainController]);

})();