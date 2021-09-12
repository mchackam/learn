const http = require('http');

const app = http.createServer((req,res) => {
    res.writeHead(200,{"Content-Type":"application/json"});
    const obj = {
        name:"Mithun",
        age:38
    };
    res.write(JSON.stringify(obj));
    res.end();
});

app.listen(8080);
