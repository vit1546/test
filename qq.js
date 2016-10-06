is = [{"a":1},{"a":2},{"a":3},{"a":4},{"a":5},{"a":5},{"a":5}];

need = [3,4,5,8,9];

result = [];

is.forEach(function(e){
	if(need.indexOf(e.a) == -1){
		console.log("delete " + e.a);
	}else{
		need.splice(need.indexOf(e.a),1);
	}
});

need.forEach(function(e){
	console.log("add: " + e);
});
