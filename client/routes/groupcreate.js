const express = require("express");
const router = express.Router();
const path = require('path'); 


router.get("/groups/create", (req, res) => {
    res.sendFile(path.join(__dirname,'../views/greport.html'))
});
// Export router 
module.exports = router;