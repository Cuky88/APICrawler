var fs = require('fs')

var json = JSON.parse(fs.readFileSync('./../3_tag_clustered/tag-clustered-result.json', 'utf8'));


for (key in json) {
    apis = []
    for (tagKey in json[key]) {
        if (tagKey !== 'total') {
            apis = [...apis, ...json[key][tagKey].apis]
        }
    }
    fs.writeFile(`./singles/${json[key].total}-${key}.json`, JSON.stringify(apis, null, 4), 'utf8');
}