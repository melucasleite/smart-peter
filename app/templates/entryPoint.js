console.log("Blessed be the name of the LORD From this time forth and forever.")
var AppState = {{ state|tojson }};

$(".client-name").html(AppState.name);