var express = require('express'),
    app = express(),
    port = process.env.PORT || 3000;

app.get('/', function(req, res){
  res.send('Hello world This is my updated  website')

})

app.listen(port, function(){
  console.log('Server listening on ', port);
})
