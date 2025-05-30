const process = require('process'); 

console.log(` Olá do script Node.js!`);
console.log(`   Estou rodando como UID (User ID): ${process.getuid()}`);
console.log(`   E como GID (Group ID): ${process.getgid()}`);

setInterval(() => {  
}, 3600 * 1000); 