# Qr_code_generator_api
API live on: https://qr-generator-kqxv.onrender.com/generate_qr<br>
To call the api with <a href="https://github.com/axios/axios">axios<a/>:<br>
```
const axios = require('axios');
const fs = require('fs');

axios.post('https://qr-generator-kqxv.onrender.com/generate_qr', {
  data: 'Data'
}, {
  responseType: 'stream'
})
.then(response => {
  response.data.pipe(fs.createWriteStream('example.png'));
})
.catch(error => {
  console.error(error);
});
```
