const crypto = require('crypto');
const fs = require('fs');


function decryptAES128(cipherTextHex, key, iv) {
  const decipher = crypto.createDecipheriv('aes-128-cbc', key, iv);
  let decrypted = decipher.update(cipherTextHex, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  return decrypted;
}


if (!fs.existsSync('encrypted_data.json')) {
  console.error('encrypted_data.json not found. Run "node aes128_encrypt.js" first.');
  process.exit(1);
}

const data = JSON.parse(fs.readFileSync('encrypted_data.json', 'utf8'));
const key = Buffer.from(data.key, 'hex');
const iv = Buffer.from(data.iv, 'hex');

console.log('==================== DECRYPTION ====================');
console.log('Ciphertext In   :', data.encrypted);

const decrypted = decryptAES128(data.encrypted, key, iv);

console.log('Decrypted Note  :', decrypted);
console.log('Matches Original?', decrypted === data.originalNote);

module.exports = { decryptAES128 };