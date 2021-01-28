d3.json('/json/').then(function(data) {
    var column_A=data.A;
    var column_B=data.B;
    console.log("Here is the data");
    console.log(data);
    //do something with A and B
})


d3.json('/csv/read').then(function(data) {
    console.log("Here is the CSV read API");
    console.log("-----------")
    console.log(data);
    //do something with A and B
})

d3.json('/csv/read2').then(function(data) {
    console.log("Here is the CSV read2 API");
    console.log("-----------")
    console.log(data);
    //do something with A and B
})

