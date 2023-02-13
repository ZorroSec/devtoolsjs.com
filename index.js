const { app, express } = require('./routes.js')
app.use('/project/scripts', express.static('./project/scripts'))
app.use('/project/css', express.static('./project/css'))

app.get('/', (req, res)=>{
    res.sendFile(__dirname + '/project/view/indexx.html')
})