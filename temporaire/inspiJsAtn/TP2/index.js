// Import essential libraries 
const express = require('express'); 
const app = express(); 
const path = require('path'); 
const router = express.Router(); 

// Setup essential routes 
router.get('/', function(req, res) { 
    res.sendFile(path.join(__dirname + '/src/index.html')); 
    //__dirname : It will resolve to your project folder. 
}); 

//add the router 
app.use('/', router); 
app.listen(process.env.port || 8080); 
console.log('Running at Port 8080'); 