var fs = require('fs')

var json = JSON.parse(fs.readFileSync('../api_docs/progweb_final_15838.json', 'utf8'));

// {
//    "api_url": "trumpia.com",
//    "progweb_title": "Trumpia API",
//    "progweb_url": "https://www.programmableweb.com/api/trumpia",
//    "progweb_descr": "Trumpia offers full REST and HTTP APIs, built for reliability and scalability, so you can seamlessly integrate all of our industry-leading messaging and marketing into your system. Access the most complete cross-channel messaging platform with the most promotional features in the market all through the system you use now. Trumpia\u2019s API package features transparent pricing, and boasts exceptionally high throughput rates, allowing up to 200 texts per second.",
//    "api_url_full": "http://trumpia.com/sms-api/index.php",
//    "progweb_date": "06.14.2012",
//    "api_name": "Trumpia",
//    "progweb_cat": "Messaging,Email",
//    "crawled_date": "2017-06-27T10:41:23.676113"
//  }

var result = {}

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
            primeTag[api.progweb_cat].names.push(api.api_name)
        }else{
            primeTag[api.progweb_cat]={
                total: 1,
                ids: [api.id],
                names:[api.api_name]
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
            names:[api.api_name]
        }
    }
})

fs.writeFile('tagcount-result.json', JSON.stringify(result, null, 4), 'utf8');
// console.log(testBlock)

// json.forEach((api)=>{
//     tags = api.progweb_cat.split(',')
// })