const express = require('express')
const app = express()
const path = require('path')


// 서버가 8080 포트 향하도록 세팅
app.listen(8080, ()=>{
    console.log('listening on 8080')
})

app.use(express.static(path.join(__dirname,'client/build')))

app.get('/', (req,res)=>{
    res.sendFile(path.join(__dirname, 'client/build/index.html'));
})

app.get('*', (req,res)=>{
    res.sendFile(path.join(__dirname, 'client/build/index.html'));
})


// C:\Users\min\Desktop\server\client\build\index.html