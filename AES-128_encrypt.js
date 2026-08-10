
const crypto = require('crypto');
const fs = require('fs');

function generateKeyAndIV() {
  const key = crypto.randomBytes(16); // 16 bytes = 128 bits
  const iv = crypto.randomBytes(16);  // AES block size = 16 bytes
  return { key, iv };
}

function encryptAES128(plainText, key, iv) {
  const cipher = crypto.createCipheriv('aes-128-cbc', key, iv);
  let encrypted = cipher.update(plainText, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  return encrypted;
}


const sampleNote =
  'QA Test Credential -> user: byte_sentinel_07, pass: Tr!ckyPass2026';

const { key, iv } = generateKeyAndIV();
const encrypted = encryptAES128(sampleNote, key, iv);

console.log('==================== ENCRYPTION ====================');
console.log('Original Note   :', sampleNote);
console.log('AES-128 Key(hex):', key.toString('hex'));
console.log('IV (hex)        :', iv.toString('hex'));
console.log('Encrypted Note  :', encrypted);


fs.writeFileSync(
  'encrypted_data.json',
  JSON.stringify({
    originalNote: sampleNote,
    key: key.toString('hex'),
    iv: iv.toString('hex'),
    encrypted,
  }, null, 2)
);
console.log('\nSaved key, IV and ciphertext to encrypted_data.json');
console.log('Now run: node aes128_decrypt.js');

module.exports = { generateKeyAndIV, encryptAES128 };

