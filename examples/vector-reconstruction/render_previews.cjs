/* Optional Node.js + Sharp renderer for the component example. */
const fs = require('fs');
const path = require('path');
let sharp;
try { sharp = require('sharp'); }
catch (e) {
  if (!process.env.FIGURE_NODE_MODULES) throw e;
  sharp = require(path.join(process.env.FIGURE_NODE_MODULES, 'sharp'));
}
(async () => {
  const dir = process.argv[2] || __dirname;
  const names = process.argv.slice(3);
  for (const name of names.length ? names : ['region', 'example']) {
    if (!/^[A-Za-z0-9_-]+$/.test(name)) throw Error('Use a simple SVG basename without an extension');
    const output = path.join(dir, name + '-preview.png');
    const png = await sharp(fs.readFileSync(path.join(dir, name + '.svg'))).png().toBuffer();
    fs.writeFileSync(output, png, { flag: 'wx' });
    console.log(path.basename(output));
  }
})().catch(error => { console.error(error.message); process.exitCode = 1; });
