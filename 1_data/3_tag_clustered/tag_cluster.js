var fs = require('fs')

var json = JSON.parse(fs.readFileSync('../2_preprocessed/progweb_preprocessed.json', 'utf8'));

var result = {

}

json.forEach((api) => {
    let tags = []
    if (api.progweb_cat) {
        tags = api.progweb_cat.split(',')
    } else {
        console.log(api.id)
    }

    if (result[tags[0]]) {

        let primeTag = result[tags[0]];
        primeTag.total++;
        if(primeTag[api.progweb_cat]){
            primeTag[api.progweb_cat].total++;
            primeTag[api.progweb_cat].ids.push(api.id)
            primeTag[api.progweb_cat].apis.push(api)
        }else{
            primeTag[api.progweb_cat]={
                total: 1,
                ids: [api.id],
                apis:[api]
            }
        }

    } else {
        result[tags[0]] = {
            total: 1
        }
        let newTag = result[tags[0]];
        newTag[api.progweb_cat] = {
            total: 1,
            ids: [api.id],
            apis:[api]
        }
    }
})

fs.writeFile('./tag-clustered-result.json', JSON.stringify(result, null, 4), 'utf8');