var fs = require('fs')

var dbscan = JSON.parse(fs.readFileSync('./db.json', 'utf8'));
var raw = JSON.parse(fs.readFileSync('../../1_data/2_preprocessed/progweb_preprocessed.json', 'utf8'));

result = {
    apis:[]
}
for (var i=0; i<3000; i++){
    api = raw[i]
    api['cluster_id'] = dbscan[i]
    result.apis.push(api)
}

result.apis.sort((a,b)=>{
    return a.cluster_id - b.cluster_id
})

countNoise = 0
for (var i=0; i<result.apis.length; i++){
    if(result.apis[i].cluster_id == -1) countNoise++;
}
console.log(countNoise)

result['noise'] = countNoise;

fs.writeFile(`./dbscan_result.json`, JSON.stringify(result, null, 4), 'utf8');

