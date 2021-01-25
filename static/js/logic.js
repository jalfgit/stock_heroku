d3.json('http://127.0.0.1:5000/json/').then(function(data) {
    var column_A=data.A;
    var column_B=data.B;
    console.log("Here is the data");
    console.log(data);
    //do something with A and B
})


d3.json('http://127.0.0.1:5000/csv/read').then(function(data) {
    console.log("Here is the Names CSV Contents");
    console.log(data);
    //do something with A and B
})