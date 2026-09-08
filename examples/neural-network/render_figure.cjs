const fs = require('fs');
const path = require('path');
let sharp;
try { sharp = require('sharp'); } catch (_) {
  if (!process.env.FIGURE_NODE_MODULES) throw new Error('Install sharp or set FIGURE_NODE_MODULES to its parent node_modules directory.');
  sharp = require(path.join(process.env.FIGURE_NODE_MODULES, 'sharp'));
}
const input = process.argv[2] || path.join(__dirname, 'neural-network.svg');
const output = process.argv[3] || path.join(__dirname, 'neural-network.png');
sharp(fs.readFileSync(input), {density:144}).png().toFile(output).then(info => console.log(JSON.stringify(info)));
